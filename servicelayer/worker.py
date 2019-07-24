import signal
import logging
from threading import Thread
from abc import ABC, abstractmethod

from servicelayer import settings
from servicelayer.jobs import JobStage
from servicelayer.cache import get_redis

log = logging.getLogger(__name__)


class Worker(ABC):
    """Workers of all microservices, unite!"""

    def __init__(self, conn=None, stages=None,
                 num_threads=settings.WORKER_THREADS):
        self.conn = conn or get_redis()
        self.stages = stages
        self.num_threads = num_threads
        self._shutdown = False

    def shutdown(self, *args):
        log.warning("Shutting down worker.")
        self._shutdown = True
        if not self.num_threads:
            raise SystemExit()

    def handle_safe(self, task):
        try:
            self.handle(task)
        except (SystemExit, KeyboardInterrupt, Exception):
            self.retry(task)
            raise
        finally:
            task.done()
            if task.job.is_done():
                task.stage.sync()
            if task.job.callback:
                task.job.execute_callback_if_done()

    def init_internal(self):
        self._shutdown = False
        self.boot()

    def retry(self, task):
        retries = int(task.context.get('retries', 0))
        if retries < settings.WORKER_RETRY:
            log.warning("Queue failed task for re-try...")
            task.context['retries'] = retries + 1
            task.stage.queue_task(task)

    def process(self):
        while True:
            self.periodic()
            task = JobStage.get_stage_task(self.conn,
                                           self.get_stages(),
                                           timeout=5)
            if task is None:
                continue
            if self._shutdown:
                self.retry(task)
                return
            self.handle_safe(task)
            if self._shutdown:
                return

    def sync(self):
        """Process only the tasks already in the job queue, but do not
        go into an infinte loop waiting for new ones."""
        self.init_internal()
        while True:
            task = JobStage.get_stage_task(self.conn,
                                           self.get_stages(),
                                           timeout=1)
            if task is None:
                return
            self.handle_safe(task)

    def run(self):
        # Try to quit gracefully, e.g. after finishing the current task.
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        self.init_internal()
        if not self.num_threads:
            return self.process()
        log.info("Worker has %d threads.", self.num_threads)
        threads = []
        for _ in range(self.num_threads):
            thread = Thread(target=self.process)
            thread.daemon = True
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def get_stages(self):
        """Easily allow the user to make the active stages dynamic."""
        return self.stages

    def boot(self):
        """Optional hook for the boot-up of the worker."""
        pass

    def periodic(self):
        """Optional hook for running a periodic task checker."""
        pass

    def after_task(self, task):
        """Optional hook excuted after handling a task"""
        pass

    @abstractmethod
    def handle(self, task):
        raise NotImplementedError

import json

from fakeredis import FakeRedis
from redis import ConnectionPool, Redis

from servicelayer import settings

TASK_PENDING = 'pending'
TASK_RUNNING = 'executing'
TASK_FINISHED = 'finished'
TASK_TOTAL = 'total'


def get_fakeredis():
    if not hasattr(settings, '_redis_fake'):
        settings._redis_fake = FakeRedis(decode_responses=True)
    return settings._redis_fake


def get_redis_pool():
    if not hasattr(settings, '_redis_pool'):
        settings._redis_pool = ConnectionPool.from_url(settings.REDIS_URL,
                                                       decode_responses=True)
    return settings._redis_pool


def get_redis():
    """Create a redis connection."""
    if settings.REDIS_URL is None:
        return get_fakeredis()
    return Redis(connection_pool=get_redis_pool(), decode_responses=True)


def make_key(*criteria):
    """Make a string key out of many criteria."""
    criteria = [c or '' for c in criteria]
    criteria = [str(c) for c in criteria]
    return ':'.join(criteria)


def _serialize(data):
    return json.dumps(data)


def _deserialize(data):
    return json.loads(data)


def push_task(queue, dataset, entity, config):
    assert queue in settings.QUEUES
    conn = get_redis()
    conn.rpush(make_key('ingest', 'queue', queue), _serialize({
        'dataset': dataset,
        'entity': entity,
        'config': config,
    }))
    conn.incr(make_key('ingest', TASK_PEDNING, dataset))


def poll_task():
    conn = get_redis()
    queues = [make_key('ingest', 'queue', q) for q in settings.QUEUES]
    while True:
        task_data_tuple = conn.blpop(queues)
        # blpop blocks until it finds something. But fakeredis has no
        # blocking support. So it justs returns None.
        if task_data_tuple is None:
            return

        key, json_data = task_data_tuple
        task_data = _deserialize(json_data)
        entity = task_data["entity"]
        config = task_data["config"]
        dataset = task_data["dataset"]
        conn.decr(make_key('ingest', TASK_PEDNING, dataset))
        conn.incr(make_key('ingest', TASK_RUNNING, dataset))
        yield (dataset, entity, config)


def get_status(dataset):
    conn = get_redis()
    pending_tasks = int(conn.get(make_key('ingest', TASK_PEDNING, dataset)) or 0)  # noqa
    executing_tasks = int(conn.get(make_key('ingest', TASK_RUNNING, dataset)) or 0)  # noqa
    finished_tasks = int(conn.get(make_key('ingest', TASK_FINISHED, dataset)) or 0)  # noqa
    return {
        TASK_TOTAL: pending_tasks + executing_tasks + finished_tasks,
        TASK_FINISHED: finished_tasks,
    }


def mark_task_finished(dataset):
    conn = get_redis()
    pending = int(conn.get(make_key('ingest', TASK_PEDNING, dataset)) or 0)
    executing = int(conn.decr(make_key('ingest', TASK_RUNNING, dataset)) or 0)
    conn.incr(make_key('ingest', TASK_FINISHED, dataset))
    if pending == 0 and executing == 0:
        reset_status(dataset)



def reset_status(dataset):
    conn = get_redis()
    conn.delete(make_key('ingest', TASK_PEDNING, dataset))
    conn.delete(make_key('ingest', TASK_RUNNING, dataset))
    conn.delete(make_key('ingest', TASK_FINISHED, dataset))

from unittest import TestCase

from servicelayer.cache import get_fakeredis
from servicelayer.rate_limit import RateLimit


class RateLimitTest(TestCase):

    def test_rate(self):
        conn = get_fakeredis()
        limit = RateLimit(conn, 'banana', limit=10)
        assert limit.check()
        limit.update()
        assert limit.check()
        for _ in range(13):
            limit.update()
        assert not limit.check()

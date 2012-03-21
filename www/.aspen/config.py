import os
import redis
import urlparse

if os.environ.has_key('REDIS_TO_GO'):
    urlparse.uses_netloc.append('redis')
    url = urlparse.urlparse(os.environ['REDIS_TO_GO'])
    REDIS = redis.Redis(host=url.hostname, port=url.port, db=0,
            password=url.password)
else:
    REDIS = redis.Redis()

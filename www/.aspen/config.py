import os
import redis
import urlparse

if os.environ.has_key('REDISTOGO_URL'):
    urlparse.uses_netloc.append('redis')
    url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
    REDIS = redis.Redis(host=url.hostname, port=url.port, db=0,
            password=url.password)
else:
    REDIS = redis.Redis()

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

deps = map(lambda d: d.split('==')[0],
        open('../requirements.txt').read().split('\n')[:-1])

def add_deps(request):
    request.deps = deps
    return request

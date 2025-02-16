import os
import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = 'redis://localhost:6379'
connect = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(connect):
        worker = Worker(list(map(Queue, listen)))
        worker.work()



Install Redis (redis-server, redis-sentinel, redis-cli, redis-benchmark, redis-check-aof, redis-check-dump)
```sh
wget http://download.redis.io/redis-stable.tar.gz
tar -xvzf redis-stable.tar.gz
cd redis-stable
make
```

```sh
pyvenv env
source env/bin/activate
# deactive
```

Install Redis Queue, RQ Scheduler
  (get latest version; recommend not installing from package manager)
```sh
pip install rq rq-scheduler
pip install Flask
pip freeze > requirements.txt
```

Redis Worker
```py
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
```

```sh
ssh rh@134.209.227.72
Start Redis server (while running in `pyvenv env`)
$ redis-server & #run in background
$ rq worker &
$ rqscheduler &
```

Use "CaAPI - Cats as a Service" to Get a [random cat photo](https://thecatapi.com/), using a RESTful API GET command:
```sh
https://api.thecatapi.com/v1/images/search?limit=1
```
which returns a random photo from their cat collection with a json response corresponding to the random file like:
```sh
[{"breeds":[],"id":"1vr","url":"https://cdn2.thecatapi.com/images/1vr.jpg","width":500,"height":334}]
```
Serve this with Flask:
```python
from flask import Flask, make_response
import requests

app = Flask(__name__)
@app.route('/')
def hello():
        cat, typ = rand_cat()
	        response = make_response(cat)
		        response.headers.set('Content-Type', 'image/jpeg')
			        return response

pick_cat_url = 'https://api.thecatapi.com/v1/images/search?limit=1'
def rand_cat():
    # PARAMS = {'x-api-key': api_key} # request free api key to get wider range of service
    r = requests.get(url = pick_cat_url)
    data = r.json()
    cat_url = data[0]['url']
    print(cat_url)
    response = requests.get(url = cat_url, stream=True)
    status = response.status_code
    if status != 200:
       print("Error:", status)
    return response.content, cat_url
```

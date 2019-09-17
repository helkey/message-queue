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

if __name__ == '__main__':
        app.run()

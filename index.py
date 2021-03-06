import json
import routes
from flask import Flask, redirect
from storage import load

app = Flask(__name__, static_url_path='')

@app.route('/', methods=["GET"])
def root():
    return redirect('/tandalogin.html')


@app.route('/hook', methods=["POST"])
def hook():
    return routes.hook()


@app.route('/user_data', methods=["POST"])
def user_data():
    return routes.user_data()


@app.route('/fb_auth', methods=['POST'])
def fb_auth():
    return json.dumps(routes.hecking_facebook_auth())


if __name__ == "__main__":
    load()
    app.run(host='0.0.0.0', port=3000)

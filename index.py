import json

from flask import Flask

import routes

app = Flask(__name__)

user_storage = dict()  # This is basically MongoDB, right?


def load():
    with open('user_storage.dat', 'w+') as f:
        data = f.read()
        global user_storage  # I always feel so dirty when I do this
        try:
            user_storage = json.loads(data)
        except ValueError:
            user_storage = dict()


def save():
    data = json.dumps(user_storage)
    with open('user_storage.dat', 'w+') as f:
        f.write(data)


@app.route('/', methods=['GET'])
def main_html():
    with open('views/tandalogin.html', 'r+') as f:
        return f.read()


@app.route('/facebook.html', methods=['GET'])
def facebook_page():
    with open('views/facebook.html', 'r+') as f:
        return f.read()


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

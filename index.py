import json

from flask import Flask, send_from_directory

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


@app.route('/hook', methods=["POST"])
def hook():
    return routes.hook()

@app.route('/fb_auth', methods=['POST'])
def fb_auth():
    return json.dumps(routes.hecking_facebook_auth())

@app.route('/<path:path>')
def public(path):
    print(path)
    return app.send_static_file(path)

if __name__ == "__main__":
    load()
    app.run(port=3000)

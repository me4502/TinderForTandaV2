import json
import routes
from flask import Flask
from storage import load

app = Flask(__name__)


@app.route('/hook', methods=["POST"])
def hook():
    return routes.hook()


@app.route('/fb_auth', methods=['POST'])
def fb_auth():
    return json.dumps(routes.hecking_facebook_auth())


if __name__ == "__main__":
    load()
    app.run(port=3000)

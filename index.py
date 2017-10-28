from flask import Flask
import routes
app = Flask(__name__)


@app.route('/hook', methods=["POST"])
def hook():
    return routes.hook()


if __name__ == "__main__":
    app.run(port=3000)

from flask import Flask
app = Flask(__name__)


@app.route('/hook', methods=["POST"])
def hook():
    return "Hello world!"


if __name__ == "__main__":
    app.run(port=3000)

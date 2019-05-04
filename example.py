from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """Just returns a hello."""
    return "Hello, world!"


if __name__ == "__main__":
    app.run()

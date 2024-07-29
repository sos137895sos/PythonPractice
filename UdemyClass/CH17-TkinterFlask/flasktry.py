from flask import Flask

# create flask app
app = Flask(__name__)


@app.route("/")
def index():
    return "This is my homepage"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template
# create flask app
app = Flask(__name__)


@app.route("/")
@app.route("/hello/<name>")
def home(name=None):
    return render_template('index.html', name=name)


@app.route("/info", methods=['POST'])
def returnSomething():
    # JavaScript Object Notation
    return jsonify({'info': 'You have successfully make a request.'})


if __name__ == '__main__':
    app.run(debug=True)

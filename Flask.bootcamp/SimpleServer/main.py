from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world</h1>"

@app.route("/info")
def info():
    return "<h2>first server on python</h2>"

if __name__ == '__main__':
    app.run()


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hell():
    return "<h1>hello Flash~~!! hahaha<h1>"

@app.route('/test')
def test():
    return "test"

if __name__ == '__main__':
    app.run("0.0.0.0", port=8080)


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello world'

@app.route('/Ivan')
def Ivan():
    return 'Hello Ivan'

@app.route('/about')
def about():
    return '<h1>about<h1>'
if __name__ == '__main__':
    app.run()

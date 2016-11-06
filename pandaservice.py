import os

from flask import Flask, current_app


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__, static_folder='resources')


@app.route('/')
def hello_world():
    return 'Hello Panda World!'


@app.route('/resources/<path:path>')
def get_resource(path):
    current_app.send_static_file('./resources/%s' % path)


if __name__ == '__main__':
    app.run()

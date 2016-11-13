import os

from flask import Flask, current_app


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

# initialize flask application class with static folder override
app = Flask(__name__, static_folder='resources')

# route '/'  to invoke hello_world()
@app.route('/')
def hello_world():
    return '''Hello Panda World! <br />
    You can access you're panda's @ <br/ ><br />
    <a href='/resources/small.png'>/resources/small.png</a><br />
    <a href='/resources/medium.png'>/resources/medium.png</a>
    '''

# route /resources to invoke 'get_resource' with requested file
@app.route('/resources/<path:path>')
def get_resource(path):
    # return the static file with correct MIME type
    current_app.send_static_file('./resources/%s' % path)

# if this file was called manually (usually for debug)
if __name__ == '__main__':
    # use flask's internal (basic) web server for debugging..
    app.run(debug=True)

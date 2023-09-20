import os

from flask import Flask, render_template

app = Flask(__name__)

port = os.environ['port']
environment = os.environ['environment']
hostname = os.environ['hostname']
theme_type = os.environ['theme_type']
debug = os.environ['debug_on']


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        hostname=hostname,
        theme_type=theme_type,
        environment=environment,
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=debug)

from flask import Flask,jsonify
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    json_file = {}
    json_file['query'] = 'hello_world'
    return jsonify(json_file)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()

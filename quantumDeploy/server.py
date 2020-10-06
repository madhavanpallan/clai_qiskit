from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from quantum_wa import intent_caller
import os
import json

app = Flask(__name__)
CORS(app)

port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/api/xplore', methods=['POST'])
def translateTest():
    cmd = request.json['command']
    data = intent_caller(cmd)
    jsonResp = {"result":'success', "response":data}
    return jsonify(jsonResp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
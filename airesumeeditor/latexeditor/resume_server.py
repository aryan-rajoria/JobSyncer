# Resumer server only has generate feature
"""
Has the following features:
1) get segments based on template selected
2) get json format for texts accepted
3) receive json for these segments
4) generate resume
5) send resume to an address??
"""
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_pdf():
    pass

if __name__=='__main__':
    app.run(debug=True, port=9004)
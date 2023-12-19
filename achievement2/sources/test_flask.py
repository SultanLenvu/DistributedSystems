#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from PyLounge and Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

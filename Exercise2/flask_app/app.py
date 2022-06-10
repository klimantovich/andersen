#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route('/')	
def index():
	return ('Hell, world')

# Not used in apache, so it doesn't matter
if __name__ == '__main__':
	app.run(host=None, port=None, debug=True)

from flask import Flask
app = Flask('__main__')

@app.route('/update')
def hello_world():
	return "this is the update endpoint"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
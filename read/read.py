from flask import Flask
app = Flask('__main__')

@app.route('/read')
def hello_world():
	return "this is the read service"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
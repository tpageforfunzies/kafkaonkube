from flask import Flask
app = Flask('__main__')

@app.route('/delete')
def hello_world():
	return "this is the delete endpoint"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
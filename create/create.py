from flask import Flask
app = Flask('__main__')

@app.route('/create')
def create_route():
	return "this is the create endpoint"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
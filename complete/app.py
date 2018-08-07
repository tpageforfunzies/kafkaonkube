from flask import Flask
app = Flask('__main__')

# from rediscluster import StrictRedisCluster

# startup_nodes = [{"host": "192.168.64.5", "port": "30000", "password": "password"}]
# rc = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)


@app.route('/')
def hello_world():
	return "this is the main page"

@app.route('/delete')
def delete():
	return "this is the delete endpoint"

@app.route('/create')
def create():
	# global rc
	# rc.set("foo", "bar")
	return "this is the create endpoint"

@app.route('/read')
def read():
	# global rc
	# return rc.get("foo")
	return "this is the read endpoint"

@app.route('/update')
def update():
	return "this is the update endpoint"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask import Flask
app=Flask(__name__)

@app.route('/hi/<name>')
def hello_name(name):
	return'Hello %s!' %name

@app.route('/hi/<int>')
def hello_in(int):
	return'Hello %d!' %int

@app.route('/hi/<float>')
def hello_flo(float):
	print"type(name)"
	return'Hello %f!' %float

if __name__=="__main__":
	app.run(debug=True)

from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
	return'Helllo world'

@app.route("/about")
def about():
	return'Foslipy C.S Pvt Ltd'

if __name__=="__main__":
	app.run(debug=True)


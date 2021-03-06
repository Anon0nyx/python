from flask import *
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<name>")
def hello(name):
	return render_template("hello.html", name=name)

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080)

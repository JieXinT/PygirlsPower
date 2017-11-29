import os

from flask import Flask, render_template

app = Flask("demoApp")

@app.route("/")
def say_hello():
	return "Hello Code First Girls people!"

@app.route("/<name>")
def say_hello_to(name):
	return f"Hello {name}"

@app.route("/hello/<name>")
def say_hello_the_old_way_with_name(name):
	return render_template("index.html", name=name)

@app.route("/another")
def show_another_template():
	return render_template("another.html")

if 'PORT' in os.environ:
	# app running on Heroku
	app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
	# app running locally (i.e you can see it by)
app.run(debug=True)
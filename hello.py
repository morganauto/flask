from flask import Flask, render_template


# create flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# def index():
# 	return "<h1>Hello World!</h1>"






def index():
	first_name = "John"
	stuff = "This is Bold Text"

	favorite_pizza = {"Peperonni":"best","Cheese": "worst"}
	return render_template("index.html",
		first_name=first_name,
		stuff=stuff,
		favorite_pizza=favorite_pizza)

# localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)


# create custim error pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
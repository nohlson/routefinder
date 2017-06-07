from flask import Flask, render_template, url_for, request
import sys
sys.path.append("classes")
from model import Model

app = Flask(__name__)
model = Model()

@app.route('/')
def index():
	airports = model.getAirports()
	return render_template("app.html", airports=airports)

@app.route('/route', methods=['GET', 'POST'])
def route():
	originAirport = str(request.args['origin'])
	destAirport = str(request.args['destination'])
	valid_routes = model.findRoute(originAirport, destAirport)

	return render_template("routes.html", origin = originAirport, dest = destAirport, valid_routes = valid_routes)

if __name__ == "__main__":
	if model.setup():
		print("Success")
		app.run(debug=True)
	else:
		 print("DATABASE ERROR")
	
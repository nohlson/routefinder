from flask import Flask, render_template, url_for, request
import model

app = Flask(__name__)

@app.route('/')
def index():
	airports = model.getAirports()
	return render_template("app.html", airports=airports)

@app.route('/route', methods=['GET', 'POST'])
def route():
	originAirport = str(request.args['origin'])
	destAirport = str(request.args['destination'])
	model.findRoute(originAirport, destAirport)
	return(str(originAirport) + str(destAirport))

if __name__ == "__main__":
	if model.setup():
		print("Success")
		app.run(debug=True)
	else:
		 print("DATABASE ERROR")
	
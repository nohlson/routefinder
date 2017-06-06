from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
	airports = ['lax', 'mia']
	return render_template("app.html", airports=airports)

@app.route('/route', methods=['GET', 'POST'])
def route():
	originAirport = request.args['origin']
	destAirport = request.args['destination']
	return(str(originAirport) + str(destAirport))

if __name__ == "__main__":
	app.run(debug=True)
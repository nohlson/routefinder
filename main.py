from flask import Flask, render_template, url_for, request
import os, sys
sys.path.append(os.getcwd() + "/classes")

from model import Model

app = Flask(__name__)
m = Model()


@app.route('/')
def index():
    airports = m.getAirportCodes()
    return render_template("app.html", airports=airports)


@app.route('/route', methods=['GET', 'POST'])
def route():
    originAirport = str(request.args['origin'])
    destAirport = str(request.args['destination'])
    if originAirport == destAirport:
        return "Same Airport <a href=\"" + url_for('index') + "\">Return</a>"
    numRoutes = int(request.args['numRoutes'])
    valid_routes = m.findRoute(originAirport, destAirport, numRoutes)

    return render_template("routes.html", origin=originAirport, dest=destAirport, valid_routes=valid_routes)


if __name__ == "__main__":
    if m.verifySetup():
        print("Success")
        app.run(debug=True)
    else:
        print("DATABASE ERROR")

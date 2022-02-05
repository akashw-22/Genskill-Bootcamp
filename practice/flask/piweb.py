from flask import Flask, render_template, request, jsonify
import pi_est
import time
import math


#flask app to run in the browser
app = Flask("Web_App")

#decorator
@app.route("/")
def code():
	return render_template('main.html', pi = math.pi) #the render template renders the html and the parameters passed are being substituted

#this functions acccepts the values from the client using methods = "POST"; by default it is get
@app.route("/estimate", methods = ["POST"])
def estimate():
	time.sleep(1)
	algo = request.form['algo'] #accepts the values from the browser
	itr = request.form['n']
	names = {"mc" : "Monte Carlo", "w" : "Wallis product estimation"}
	
	if(algo == "mc"):
		pi = pi_est.montecarlo(int(itr));
	else:
		pi = pi_est.wallis(int(itr));
	
	if(request.accept_mimetypes.best == "applications/json"):
		return (dict (algorithm = names[algo],
			iterations = itr,
			estimate = pi,
			text = "oombikko"))
	elif(algo == "mc"):
		return render_template('monte.html', n = itr, pi = pi)
	else:
		return render_template('wallis.html', n = itr, pi = pi)
		
if __name__ == "__main__":
	app.run()

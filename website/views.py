from flask import Flask,request,session,redirect,url_for,render_template,flash
from .models import RecoEngine

app= Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
	return render_template("index.html")
	
@app.route('/about')
def about():
	return "The about page"
	
@app.route("/near_you",methods=["GET","POST"])
def near_you():
	if request.method== "POST":
		location=request.form["division"]
		recommendation=RecoEngine.res_near_you(location)
		return render_template("show_near_you.html",recommendation=recommendation,division=location)
	return render_template("near_you.html")

@app.route("/by_month",methods=["GET","POST"])
def by_month():
	if request.method== "POST":
		#return "todo"
		location=request.form["division"]
		month=request.form["month"]
		recommendation=RecoEngine.res_by_month(location,month)
		return render_template("show_by_month.html",recommendation=recommendation,division=location,month=month)
	return render_template("by_month.html")

@app.route("/general_rec",methods=["GET","POST"])
def general_rec():
	if request.method=="POST":
		location=request.form['division']
		category=request.form["category"]
		session['division']=location
		session['category']=category
		recommendation=RecoEngine.res_general_rec(location,category)
		return render_template("show_general_rec.html",recommendation=recommendation,division=location,category=category)
	return render_template("general_rec.html")

@app.route("/show_similiar_search",methods=["GET"])
def show_similiar_search():
	location=session["division"]
	category=session["category"]
	recommendation=RecoEngine.res_similiar_search(location,category)
	return render_template("show_similiar_rec.html",recommendation=recommendation,division=location,category=category)

@app.route("/show_relating_search",methods=["GET"])
def show_relating_search():
	location=session["division"]
	category=session["category"]
	recommendation=RecoEngine.res_relating_search(location,category)
	return render_template("show_relating_rec.html",recommendation=recommendation,division=location,category=category)
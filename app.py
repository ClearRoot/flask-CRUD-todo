from flask import Flask, render_template, redirect, request
import csv
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    f = open("mytodos.csv", "r", encoding="utf-8")
    mytodos = csv.reader(f)
    
    return render_template("index.html", mytodos=mytodos)

@app.route("/new")
def new():
    return render_template("new.html")
    
@app.route("/create", methods=["post"])
def create():
    title = request.form.get("title")
    contents = request.form.get("contents")
    now = datetime.datetime.now()
    
    f = open("mytodos.csv", "a+", encoding="utf-8", newline="")
    csv_w = csv.writer(f)
    csv_w.writerow([title, contents, now])
    f.close
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)    
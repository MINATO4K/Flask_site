from flask import Flask, render_template, Blueprint, flash, g, redirect

app = Flask(__name__) 
@app.route("/") 
def raiz():
  return render_template("index.html")

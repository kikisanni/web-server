from flask import Flask, render_template

app = Flask(__name__)
# print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/blog")
def blogs():
    return "These are my thoughts on blogs"

#First Commit
print("Hello World")
#Importing libraries and packages useful functions
from flask import Flask, render_template
#Creating web app using Flask
app = Flask(__name__)
#creating route to the html file
@app.route('/')
def home():
    return render_template("index.html")
#runs the web app
app.run(
    debug = True
)
#to host online --> render.com
#--> Get Started sign in with GitHub --> New+
#--> web service --> build&deploy from Git repo
#connect 1101-Final --> add name and add file in folder
# requirements.txt
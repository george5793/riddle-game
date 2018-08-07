import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

data = []

def write_to_file(filename, data):
    """ Handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)

@app.route('/', methods = ["GET", "POST"])
def index():
    """ Main landing page """
    
    if request.method == "POST":
        write_to_file("data/players.txt", request.form["player_name"] + "\n")
        return redirect(request.form["player_name"])
    return render_template("index.html")
    
@app.route('/<player_name>')
def riddles(player_name):
    """ Game page """
    return render_template("riddles_game.html")

app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug = True)
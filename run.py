import os
import json
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'worst_kept_secret'

def write_to_file(filename, data):
    """ Handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)
        
def record_incorrect(player_name, guess):
    write_to_file("data/incorrect_answers.txt", "{0} - {1}\n".format(player_name, guess))

@app.route('/', methods = ["GET", "POST"])
def index():
    """ Enter Player Name page """
    if request.method == "POST":
        write_to_file("data/players.txt", request.form["player_name"] + "\n")
        return redirect(request.form["player_name"])
    return render_template("index.html")
    
@app.route('/<player_name>', methods = ["GET", "POST"])
def riddles(player_name):
    """ Game page """
    riddles = []
    # Load riddles.json file and store in list format
    with open("data/riddles.json") as json_riddles:
        riddles = json.load(json_riddles)
        
    riddle_number = 0
    
    if request.method == "POST":
        # Retrieve riddle number from submitted form (hidden field)
        riddle_number = int(request.form["riddle_number"])

        # Retrieve player's answer from submitted form
        player_answer = request.form["guess"]
        
        # Compare player's guess with actual answer in JSON file
        if player_answer == riddles[riddle_number]["solution"]:
            # CORRECT - Move onto next riddle
            riddle_number +=1
        else:
            # INCORRECT - name and score pushed to incorrect_answers.txt
            record_incorrect(player_name, player_answer)
            flash("Sorry {0}, that's an incorrect answer. Try again...".format(player_name))
            
    return render_template("riddles_game.html", riddles = riddles, riddle_number = riddle_number)
        
        
        
app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug = True)
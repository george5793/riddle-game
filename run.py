import os
import json
import csv
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'worst_kept_secret'

################################################################################

def write_to_file(filename, data):
    """ Handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)
        
def get_incorrect_answers():
    """ Returns list of logged incorrect answers """
    with open("data/incorrect_answers.csv", "r") as file:
        csv_reader = csv.reader(file)
        incorrect_answers = []
        for line in csv_reader:
            incorrect_answers.append(line)
        return incorrect_answers
        
def calculate_game_percentage(riddle_number):
    game_percentage = ((riddle_number)*100)//11
    return game_percentage
        
################################################################################

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
    
    with open("data/riddles.json") as json_riddles:
        riddles = json.load(json_riddles)
        
    riddle_number = 0
    
    if request.method == "POST":
        riddle_number = int(request.form["riddle_number"])
        player_answer = request.form["guess"]
        
        if player_answer.lower() == 'quit':
            return render_template("high_scores.html")
            
        elif player_answer.lower() == riddles[riddle_number]["solution"]:
            riddle_number +=1
            
        else:
            flash("INCORRECT ANSWER".format(player_name))
            with open("data/incorrect_answers.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([(riddle_number + 1), player_name, player_answer])
                
        if riddle_number > 10:
            return render_template("celebration.html")
            
    incorrect_answers = get_incorrect_answers()
    
    game_percentage = calculate_game_percentage(riddle_number)
    string_riddle_number = str(riddle_number + 1)
                
    return render_template("riddles_game.html", 
                            riddles = riddles, 
                            riddle_number = riddle_number,
                            incorrect_answers = incorrect_answers,
                            game_percentage = game_percentage,
                            string_riddle_number = string_riddle_number)
        
        
        
app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug = True)
import os
import json
import csv
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

################################################################################
""" Required Functions """

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
        
def get_csv_data(filepath):
    with open(filepath, "r") as file:
        csv_reader = csv.reader(file)
        csv_data = []
        for line in csv_reader:
            csv_data.append(line)
        return csv_data
        
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
            with open("data/high_scores.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([(riddle_number + 1), player_name])
                
            high_scores = get_csv_data("data/high_scores.csv")
            
            return render_template("high_scores.html",
                                    high_scores = high_scores)
            
        elif player_answer.lower().strip() == riddles[riddle_number]["solution"]:
            riddle_number +=1
            
        else:
            flash("INCORRECT ANSWER")
            with open("data/incorrect_answers.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([(riddle_number + 1), player_name, player_answer])
                
        if riddle_number > 10:
            with open("data/high_scores.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([(riddle_number + 1), player_name])
            return render_template("celebration.html")
            
    incorrect_answers = get_csv_data("data/incorrect_answers.csv")
    
    game_percentage = calculate_game_percentage(riddle_number)
    string_riddle_number = str(riddle_number + 1)
                
    return render_template("riddles_game.html", 
                            riddles = riddles, 
                            riddle_number = riddle_number,
                            incorrect_answers = incorrect_answers,
                            game_percentage = game_percentage,
                            string_riddle_number = string_riddle_number)
        
        
        
app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))
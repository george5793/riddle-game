import os
from flask import Flask, render_template

app = Flask(__name__)

# def show_riddle():
    
#     riddles = []
#     solutions = []
    
#     with open('riddle.txt', "r") as file:
#         lines = file.read().splitlines()
        
#     for i, text in enumerate(lines):
#         if i%2 == 0:
#             riddles.append(text)
#         else:
#             solutions.append(text)
            
#     number_of_riddles = len(riddles)
#     riddles_and_solutions = zip(riddles, solutions)
    
#     score = 0
    
#     for riddle, solution in riddles_and_solutions:
#         guess = input(riddle +"> ")
#         if guess == solution:
#             score +=1
#             print("Correct answer!")
#         else:
#             print("Wrong answer :(")
            
def get_riddle():
    
    riddles = []
    
    with open("data/riddle.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
            if i%2 == 0:
                riddles.append(text)
    
    return riddles
    
def get_solutions():
    
    solutions = []
    
    with open("data/riddle.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 != 0:
            solutions.append(text)
        
    return solutions
    

@app.route('/')
def index():
    """ Main Riddle Game Landing Page """
    
    riddles = get_riddle()
    solutions = get_solutions()
    return render_template('index.html', riddles = riddles, solutions = solutions)
    
app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)
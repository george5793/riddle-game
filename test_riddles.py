import os
import unittest
import csv
import run
from run import app
from flask import Flask, url_for, request

class test_riddles_app(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass
        
        
    """ INDEX """    
    # Confirm index page loads
    def test_index_html_return(self):
        index = app.test_client(self)
        response = index.get('/',content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        
    # Confirm player name in form submission
    def test_player_name_response(self):
        post = self.app.post('/', data=dict(player_name='Alice'))
        result = self.app.get('/', query_string=dict(player_name='Alice'))
        self.assertEqual(post.status_code, 302)
        self.assertEqual(result.status_code, 200)
    
    # Confirm player name is written to file
    def test_write_player_to_file(self):
        post = self.app.post('/', data=dict(player_name='George'))
        with open("data/players.txt", "r") as file:
            lines = file.readlines()
            lastEntry = lines[-1]
            self.assertEqual(lastEntry, 'George\n')
            
            
    """ RIDDLES """
    # Confirm riddle page loads
    def test_riddle_html_return(self):
        response = self.app.get('/Steve', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        
    # Confirm first riddle loads
    def test_first_riddle_loads(self):
        response = self.app.get('/Mitch', content_type = 'html/text')
        self.assertTrue(b"What is the worst vegetable to have on a ship?" in response.data)
        
    # Confirm answer submission works    
    def test_answer_submission(self):
        self.app.post('/Craig', data=dict(riddle_number=0, guess='test'))
        response = self.app.get('/Craig', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        
    # Confirm correct answer behaviour    
    def test_correct_answer(self):
        response = self.app.post('/Dave', data=dict(riddle_number=0, guess='leek'), follow_redirects=True)
        self.assertIn(b"Flat as a leaf", response.data)
        
    # Confirm incorrect answer returns to same riddle    
    def test_incorrect_answer(self):
        response = self.app.post('/Michael', data=dict(riddle_number=2, guess='wrong answer'))
        self.assertIn(b"What goes up when the rain comes down?", response.data)
    
    # Confirm incorrect answer logged in csv
    def test_incorrect_answer_logged(self):
        self.app.post('/Daphne', data=dict(riddle_number=2, guess='wrong answer 2'))
        incorrect_answer = []
        with open('data/incorrect_answers.csv', 'r') as f:
            for item in reversed(list(csv.reader(f))[-1]):
                incorrect_answer.append(item)
        self.assertEqual(['wrong answer 2', 'Daphne', '3'], incorrect_answer)
        
    # Confirm that typing quit directs you to high scores page
    def test_quit_redirect(self):
        response = self.app.post('/Velma', data=dict(riddle_number=2, guess='quit'))
        self.assertIn(b"BETTER LUCK NEXT TIME!", response.data)
        
    # Confirm that typing quit logs score to csv
    def test_quit_log(self):
        self.app.post('/Penelope', data=dict(riddle_number=5, guess='quit'))
        high_score = []
        with open('data/high_scores.csv', 'r') as f:
            for item in reversed(list(csv.reader(f))[-1]):
                high_score.append(item)
        self.assertEqual(['Penelope', '6'], high_score)
        
    # Confirm game percentage is calculated correctly
    def test_game_percentage(self):
        response = self.app.post('/Bill', data=dict(riddle_number=1, guess='button'))
        self.assertIn(b">18%</div>", response.data)
        
    # Confirm that completing the game takes you to the celebration page
    def test_complete_game(self):
        response = self.app.post('/Courtney', data=dict(riddle_number=10, guess='coin'))
        self.assertIn(b"YOU HAVE COMPLETED THE RIDDLE GAME", response.data)
        

        
if __name__ == '__main__':
    unittest.main(verbosity = 2)
# [Riddle Game](https://python-riddle-game-ci.herokuapp.com/)

This application uses the Flask micro web framework to allow users to play a riddle game.

The aim of the game is for the user to answer riddles displayed to them on screen. The user must first enter their name to play. Subsequently, riddles are displayed one at a time on the screen with an answer box appearing below. The user can only progress to the next riddle upon submission of a correct answer. There user must answer 11 riddles in total to complete the game. 

Each correct answer increments their score by 1 point. If the user decides they cannot finish the game, they can quit early to view the high scores leaderboard.

 
## UX

As with other projects I have undertaken, my aim with this project was to construct an application that was simple but beautiful in design, allowing the user to easily understand and interact with it. A mobile-first design approach was applied in all aspects of design for this project. From the early stages, I thought a retro theme would suit this project well, and colours, fonts and transitions were chosen to complement this.

### Name Entry Page

<img src="static/img/index.png" width="700">

This is the page that the user first sees when loading the website. In order to proceed with the game, the user must first enter their name. As explained in later sections of this README file, this name is used to log high scores and incorrect answers against.

With it's simplistic design, the user is given clear direction to the name entry field. If the user is unsure, or would like more information about how the game works, an info button which displays a list of instructions as to how the game works can be located at the bottom of the page. This button forms part of the core design for the application and can be accessed on any page of the application.

### Riddle Page

<img src="static/img/riddle.png" width="700">

Once the user has entered their name, they are directed to the first riddle. The background colour of the riddle is a different colour to the familiar input box from the previous page, to quickly guide the user when submitting an answer.

A percentage completion bar gradually increments as the user moves through the game to give the user an indication of their progress.

Hovering over the 'CHECK ANSWER' button on larger screens (clicking on small screens) changes the button fill colour to green feeding back to the user that the button has been clicked.

Below the riddle is a slider button and a prompt to the user that if they slide the slider, they can look at incorrect guesses submitted by other users. This slider is hidden by default to give the users more of a challenge should they desire.

The slider reveals a table of previous incorrect guesses, and the user that submitted the guess in a table that follows the retro colour scheme of the application.

### High Scores Page

If the user cannot complete the game, they can opt to quit halfway through by typing the word quit into the answer box. The user is then directed to the high-scores page where they can see their score in a table along with other users and their scores.

Again, the fonts, colours and themes on this page are closely aligned with the other pages in the application for uniformity.

### Celebration Page

If the user does complete the game, instead of also being directed to the high-scores page, they are directed to a special page with a flashing congratulations image.


## Features

The application primarily uses the Flask framework and Python logic to implement the core functionality. The Bootstrap library is also used to make all the elememnts on the page visually appealing.

### Name Submission

The user starts the game by entering their name into a `form` element. The `POST` method of this form calls on a route within the `app.py` file to access the `player_name` within the `request` object writing the user's name to a `.txt` file.

### JSON Riddles

The riddles are stored in `JSON` format. On page load, the riddles are loaded into the context of the application such that the riddle and answer can be accessed by subsequent code. The current `riddle_number` on the page is hidden within the `form` element, and is consequently used to load the correct riddle on the page. Once the user has submitted an answer, the `riddle_number` is again used to cross reference the user's answer with the correct answer in the `JSON` file. 

If the user's answer is successful, they proceed to the next riddle.

If they are not, a flashing error message shows up on screen. 

<img src="static/img/incorrect.png" width="700">

### CSV's

An entry is also written into a `csv` file denoting their name, incorrect answer and riddle number. Using the information in this `csv` file, the application can identify and show previous incorrect answers for a particular riddle.

If the user decides to `quit` the game, or if the user completes the game, an entry is also written into the high-scores `csv` file, noting the `player_name` and the `riddle_number`.

### Game Percentage

Whilst the user advances through the game, a progress bar can be seen above each riddle detailing the percentage of the game that has been completed. This is calculated in the `calculate_game_percentage()` function, and passed as a context variable to the `riddles_game.html` template. Here, Jinja is used to render the progress bar correctly.


### Features Left to Implement

- The application might benefit from a countdown timer that starts when the user sees the first riddle. This would aim to provide more of a challenge to the user

- More riddles could be added to the current list to make the game more challenging

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation - the only use case in this project is the incorrect answer slider toggle.
    
- [Google Fonts](https://fonts.google.com/)
    - The project uses Google Fonts to beautify the typography

- [Flask](http://flask.pocoo.org/docs/1.0/)
    - The project uses Flask to distinguish routes, redirecting and rendering relevant `html` templates
    
- [Python](https://www.python.org/)
    - Within each route, python logic is used to evaluate context variables, which are then passed to `html` templates to dynamically update webpages


## Testing

### Manual Testing

Lots of manual testing was carried out when designing the application. Context variables were tested by inserting them into dummy html pages, as well as printing values to the console and verifying the output.

The CSS was tested by running the application locally and using Google Chrome Developer Tools to tweak elements on the page.
    
### Automated Testing

The python `unittest` module was used to derive automated tests for the functions in the `run.py` file.

This involved scripting the below tests to test that the actual output matched the expected output:

_test_answer_submission_
_test_complete_game_
_test_correct_answer_
_test_first_riddle_loads_
_test_game_percentage_
_test_incorrect_answer_
_test_incorrect_answer_logged_
_test_index_html_return_
_test_player_name_response_
_test_quit_log_
_test_quit_redirect_
_test_riddle_html_return_
_test_write_player_to_file_
_test_answer_submission_
_test_incorrect_answer_
    

## Deployment

The code has been deployed to GitHub, and is hosted on [Heroku](https://python-riddle-game-ci.herokuapp.com/)


### Content

The riddles were obtained from [Riddles.com](https://www.riddles.com/best-riddles)
    

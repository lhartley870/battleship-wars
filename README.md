# Battleship Wars
Battleship Wars is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The player plays against the computer to try and find all of the computer's battleships before the computer finds all of the player's ships. Each battleship is 2 spaces long on a board and is either placed horizontally or vertically at random. This game will be useful for battleships/game enthusiasts as the computer has been programmed to think like a human when the computer gets a hit, so making the experience as close to playing a real human as possible.  

The live project can be viewed [here](https://battleship-war.herokuapp.com/). 

![Responsive view of live application](/readme-documents/application-screenshots/responsive-view.png)

## UX (User Experience) 
### Users
Users of this application are typically going to be people who are searching for an exciting game experience.

### User Stories
* As a user of the application, I want a personalised game experience. 
* As a user of the application, I want to be reminded of the rules of the game.
* As a user of the application, I want to easily be able to see at a glance where my ships are on my board and the locations where I or the computer have had a hit or a miss on the other's board.
* As a user of the application, I don't want me accidentally entering a row number or column letter that is not on the board to crash the game.
* As a user of the application, if I accidentally enter a coordinate that I've guessed before, I don't want that to 'use up' my guess for that round.
* As a user of the application, I want to know my progress for each round of the game. 
* As a user of the application, I want to be able to start a new game if I'm part way through an existing game.
* As a user of the application, I want playing against the computer to be as close to playing against another human as possible.

## Flow Charts

I used [Lucidchart](https://www.lucidchart.com/pages/) to create flow charts for the logic of my application. 

The main game logic flow chart can be found here: 
* [Main Game Logic flow chart](/readme-documents/logic-flow-charts/game-logic-flow-chart.png)  

Initially I had 5 ships of different sizes created using subclasses of the Ship class. The initial main game logic was just applied so that the computer would pick a random board guess each time, only filtering out its previous guesses. I ensured the main game logic functioned firstly and then amended the code to allow the computer to 'think' like a human whilst playing the game. To make the code work I made all the ships the same size and therefore removed the Ship subclasses. The logic for this second stage of my project is shown in this flow chart:

* [Computer 'thought process' flow chart](/readme-documents/logic-flow-charts/computer-thought-logic-flow-chart.png)

## How to Play
Battleship Wars is based on the classic battleships board game which was originally a pen and paper game but then became popular as a board game by Milton Bradley. You can find out more about the game on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this application the player enters their name and two boards are generated. The boards are 10 spaces by 10 spaces. The columns are marked A-J and the rows are marked 1-10. Each space on each of the boards is represented with a dot. The letters, numbers and board dots all appear in white.

The player and computer each have 5 ships of 2 spaces long on their boards. The player's ships are revealed on the player's board; the computer's ships are concealed on its board. The board spaces occupied by player's ships are represented by the letter 'S' which is coloured green. The ships are randomly placed either horizontally or vertically, never diagonally. The player is also informed that two ships will not be placed directly next to each other either horizontally or vertically on the board.

The player goes first and guesses a coordinate on the board e.g. 1A. The computer then takes a guess. If a guess is a hit, then a red '*' symbol appears at the relevant board space and the player or computer (as applicable) receives 1 point. A miss is represented by a yellow '0' on the relevant board and receives 0 points. 

The player and computer continue to take turns making guesses until one of them sinks all 5 of the other player's battleships, reaching a score of 10 and winning the game. If both the computer and the player reach a score of 10 during the last round of the game, the game is a draw. 

## Features
### Existing Features
* **Board Rows and Columns**

  To make guessing coordinates easier for the player, the columns are given letters instead of numbers to differentiate them from the row numbers. This prevents the user from becoming confused between the row and column and accidentally making a guess they didn't intend to, which could easily happen if both the columns and the rows were numbered. Behind the scenes, within the Python code logic, the letters are converted back into numbers to allow for easier processing of the data. 

* **Random Ship Placement**

  When the player and computer boards are generated at the start of the game, 5 ships of 2 spaces long are placed at random on each board. Each ship is randomly placed either horizontally or vertically (not diagonally) on the relevant board. Also, no two ships are placed next to each other horizontally or vertically. The python code is set up so that when the first ship in a set is created, its coordinates on the board and the immediate horizontal and vertical coordinates around the ship cannot be occupied by another ship. These occupied coordinates are updated as each ship in the set is created so that the next ship cannot occupy the spaces and surrounding coordinates of all the ships created before it in the set of 5. All the ship location coordinates are saved in an instance attribute of the applicable Board class instance so that the ships are printed to the same location during the game every time the player's board is updated with guesses and re-printed. 

  The player can see his/her own ships which are marked with a green 'S' on the player's board. The computer board does not print the location of the computer's ships otherwise the player would know which coordinates to guess.

* **Accepts User Input**

  The user is able to enter a name at the beginning of a new game. This name is used in the game's welcome message, in the heading for the player's board e.g. 'Steve's Board' and in the message printed at the end of the game if the player has won e.g. 'STEVE WINS!', to personalise the player's experience. If the player does not enter a name, the word 'Player' is used instead.

  The player's board position guess is required for each round of the game. The player has to input a row between 1 and 10 (inclusive) and a column between A and J (inclusive) to select their guess. 

  Once a round is completed the player has to enter a 'y' to continue the current game or can alternatively enter an 'n' to start a new game.

* **Input Validation and Error Checking**

  The player is unable to enter a row guess that is not a number or is not a row number on the board (1-10 inclusive). If the player does make an invalid entry they will be prompted to enter a number between 1 and 10. 

  The player is unable to enter a column guess that is not a column letter on the board (A-J inclusive). It does not matter if the column guess made by the player is lowercase or uppercase as the python code will convert it to uppercase. If the player tries to make a guess that is not a letter A-J they will be asked to make a guess between the letters A and J. Also, if the column guess is invalid, the user does not have to enter their guess all over again. Their valid row selection will remain so they will just need to enter a valid column letter. 

  The player is unable to make the same board coordinate guess twice. All of the player's guesses are saved in a 'guesses' attribute for the player board instance of the Board class. When a player makes a guess, this is checked against the player's previous guesses and the player will be told that they have made that guess before and will be prompted to enter an alternative guess. 

  The player is only able to enter a 'y' to continue to the next round of the current game or an 'n' to start a new game when asked whether they want to continue at the end of each round. It does not matter if the player enters a lowercase or uppercase 'y' or 'n' as the python code will convert it to lowercase. If the player makes any entry apart from an 'n' or a 'y' they will be informed and asked to make a valid entry. 

* **Round Updates**

  At the end of each round, once the player and computer have made their guesses, the player is updated with the latest round and game score information. 

  The user is informed of the coordinates of their last guess e.g. 3J and whether this guess was a hit or a miss. The player is also informed of the coordinates of the computer's last guess and whether this guess was a hit or a miss. The player is also given the updated game scores for the player and computer. Printing out the last guess of the player is particularly useful to the player so that they can be reminded of their last guess before continuing to the next round and making a new guess. 

* **Data Maintained in Class Instances**

  See the 'Data Model' section below. 
  

* **Playing Against a 'Human' Computer**

  To make the game experience as close to playing another human as possible, the computer has been programmed to 'think' like a human in the python code. 

  The player is informed at the start of the game that ships cannot be placed next to each other either horizontally or vertically. 

  When the computer has no hits or has only hit complete ships, the computer's guess is generated at random, like a human's guess would be random. However, as with the player's guesses, any previous guesses made by the computer are filtered out so the computer cannot make the same guess twice. When a computer guess is randomly generated, the guess is programmed to be a guess that is a valid coordinate on the board and not a coordinate that sits outside the board. 

  When the computer has hit only half of a ship (ie. has an odd score number such as 3 or 5), the 4 coordinates above, below, to the right and to the left of that hit coordinate are pulled up in a list. The list is then filtered to remove any coordinates that are not on the board e.g. a hit at 1A will have a surrounding coordinate of 0A for example which is not on the board, as well as previous guesses made by the computer. The computer then picks a coordinate at random from the filtered list and so will pick a coordinate horizontally or vertically next to the hit to try and hit the second half of the ship, just like a human would. As the rounds go on, the surrounding coordinates list is narrowed (by removing surrounding coordinates already guessed) until the computer hits the second half of the ship. 

  Once the computer has hit the second half of the ship, the coordinates surrounding that ship are added to the hit barrier coordinates instance attribute list for the player board. When the computer makes any guesses in the future, these coordinates will also be filtered out so that the computer does not guess them. This gives the computer the same advantage as the player who has been told that ships cannot be placed next to each other either horizontally or vertically. 

* **Scores Cleared for a New Game**

  Once a game is finished or the player opts to start a new game, the scores are cleared back to 0-0 and new ship and board instances are created to start the game afresh. 

### Further Feature Ideas
* Allow the player to select the board size within a range of sizes.
* Allow the player to decide the number of ships on the boards.
* Have ships of different sizes.
* Allow the player to enter their row number and column letter guess in one entry instead of two separate entries for row and column.
* Link the application to Google Sheets to record the number of guesses taken by a player when a player has won a game so that the application can report to the player on where they are on the leaderboard when they win a game. The lower the number of guesses taken to win, the higher the place on the leaderboard.
* Programming additional computer logic so that the computer will not guess spaces that do not have an unguessed space next to them and so cannot be part of a ship. 

## Data Model
The python code for this application includes two classes: the Ship class and the Board class. 

The 5 ships created for the player board and the 5 ships created for the computer board are all instances of the Ship class. This class contains the instance attributes length, position, orientation and barrier. Length and orientation are used by various methods within the Ship class. Position and barrier are used to save each ship instance's coordinates on the board and the ship's surrounding horizontal and vertical coordinates, respectively. The ship instances are generated by calling the applicable function which is assigned to a Board class instance attribute. From this attribute a board instance attribute is created for each ship object. The ship locations on the board and their surrounding coordinates for each ship instance can then be accessed for the applicable board via the board's instance attributes.

The Ship class also has various methods that can be utilised by the ship instances to generate each ship's non-clashing coordinates and surrounding coordinates within a ship set of 5. 

The Board class is used to create instances of the player board and computer board for each game. As well as the ship objects being instance attributes for the Board instances as mentioned above, this class has instance attributes of name, type, guesses, hits and misses and hit barrier coordinates. The type attribute is used to save the board type (either player or computer), the name attribute is used to save the player's name or 'computer' for the Computer's board instance. Guesses is used to save the opposing player's guesses against the applicable board (ie. the computer's guesses are saved against the player's board and vice versa). Hits and misses is used to record an 'H' for hit or 'M' for miss so that hits can be easily located and the applicable hit coordinate can be found by using the matching list index. The barrier coordinates attribute is used to save the surrounding coordinates of complete ships once hit by the computer so that the computer does not guess these coordinates for future guesses (described further in the 'Playing Against a 'Human' Computer section above).

The Board class also has various methods that can be utilised by the board instances to add ships to the player board (represented by 2 green 'S' symbols), add guess results to the player and computer board (hits being represented by red '*' symbols and misses by yellow '0' symbols) and print the original boards at the start of the game and the updated boards after each round. 

## Technologies Used

### Languages 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) programming language for the logic of the application.

### Modules and Libraries
* The [inbuilt python random library](https://docs.python.org/3/library/random.html) was used and necessary to generate pseudo-random numbers and choices to represent  
  the computer's choices in playing the game. For example, random.choice was used:
  * in the Ship class get_ship_orientation method to randomly select 'Horizontal' or 'Vertical' for the orientation of each ship instance; and
  * in the get_computer_guess fucntion else statment (where the computer has found half of a ship) to pick a random computer guess from the filtered list of coordinates 
    surrounding the hit coordinate.
  Also random.randrange was used to:
  * generate a random board row and column for the first coordinate location for each ship in the Ship class get_board_row_or_column method; and
  * generate a random board row and column to represent the computer's guess where no ships or only full ships have been found by the computer in the get_computer_guess   
    function. 
* The [colorama module](https://pypi.org/project/colorama/) was used as the developer felt that use of colours in the game was essential to enhance the user experience. This  
  module allows coloured text to be printed to the the terminal. With the board row numbers, column letters, board space dots, hit guesses, miss guesses and the ships all being coloured white against a black background, even though unguessed spaces, hit spaces, missed spaces and ship spaces all have different symbols, it is very difficult for a player to keep track of the updated board with ease. The developer considered that using different colours for the ships, hit spaces and miss spaces, in combination with the different symbols would help the user to more easily interpret the boards at a glance. Green was chosen for the ships as a neutral colour, red was chosen to represent a hit and yellow was chosen to represent a miss. 

### Resources and Programs
* [Git](https://git-scm.com/) was the version control system used via the Gitpod terminal to commit and push code to GitHub.
* [GitHub](https://github.com/) was the git repository hosting service used to store code pushed from Git.
* [Gitpod](https://www.gitpod.io/) was the online IDE (Integrated Development Environment)/editor used to create, modify and preview the project code. 
* [Lucidchart](https://www.lucidchart.com/pages/) was used to prepare all of the Flow Charts for the application. 
* [Am I Responsive?](http://ami.responsivedesign.is/) was used to create the screenshots showing how the application looks on the deployment terminal. 
* [W3 Schools](https://www.w3schools.com/) and [Stack Overflow](https://stackoverflow.com/) were used for general guidance and learning. 
* [This Stack Overflow post](https://stackoverflow.com/questions/48343387/valueerror-and-typeerror-in-python) and [this Built-in Exceptions Python documentation](https://docs.python.org/3/library/exceptions.html) were used for guidance on Python exception handling. 
* [PEP8 Online](http://pep8online.com/), was used for testing the python code for the site.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) and [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) were 
  used for preparing the README.md and TESTING.md files.

## Testing

Please see the separate [TESTING.md file](TESTING.md) for details of the project testing carried out. 

## Deployment

### Heroku

This project was deployed using Code Institute's mock terminal for Heroku. The project was deployed according to the following steps: 

1. Log into Heroku.
2. From the Dashboard, Click on the 'New' button and then the dropdown button called 'Create new app'.
![View of Heroku Dashboard](/readme-documents/deployment-screenshots/heroku-dashboard.png)
3. Enter a unique App name and select your region as either 'Europe' or 'United States'. If the app name is unique you will get a green tick and a message saying that your chosen name is available, otherwise you will see a red exclamation mark and a message that the name is unavailable.
![View of Create new app page](/readme-documents/deployment-screenshots/create-new-app.png)
4. Click on 'Create app'.
5. Click on 'Settings' in the bar across the top of the page. You will then be taken to a page that looks like this:
![View of Settings page](/readme-documents/deployment-screenshots/app-settings.png)
6. Scroll down to where it says 'Config Vars' down the left hand side of the page and click on 'Reveal Config Vars'.
7. Enter 'PORT' in the field for 'Key' and '8000' in the field for 'Value' and click 'Add.
![View of Config Vars section of Settings page](/readme-documents/deployment-screenshots/config-vars.png)
8. Scroll down to where it says 'Buildpacks' down the left hand side of the page and click on 'Add buildpack'. 
9. Select 'python' and click 'Save changes'. 
10. Click on 'Add buildpack' again, select 'nodejs' and click 'Save changes'.
11. The buildpacks must be in the order Python, NodeJs. If they are not you can drag and drop them to change the order. 
12. Your screen should look like this:
![View of Buildpacks section of Settings page](/readme-documents/deployment-screenshots/buildpacks.png)
13. Scroll back up to the top of the screen and this time click on 'Deployment' in the bar across the top of the page. You will then be taken to a page that looks like this:
![View of Deployment page](/readme-documents/deployment-screenshots/app-deployment.png)
14. Where it says 'Deployment Method' on the left hand side of the screen clickon GitHub.
15. Where it says 'Connect to GitHub' down the left hand side of the screen, type your repository name and click 'Search'.
16. Click on 'Connect' next to your repository name
![View of Connect to Github section of Deployment page](/readme-documents/deployment-screenshots/connect-to-github.png)
17. Scroll down to where it says 'Automatic Deploys' and 'Manual Deploy' down the left hand side of the screen. 
18. If you want Heroku to rebuild your app every time any new changes to the code are pushed to GitHub, check that the branch you want to deploy is correct and click on 'Enable Automatic Deploys'. You will then need to check that the branch you want to deploy is correct and click on 'Deploy Branch' in the Manual Deploy' section. When you have clicked on 'Enable Automatic Deploys' your screen will look like this:
![View of Automatic Deploys enabled on Deployment page](/readme-documents/deployment-screenshots/auto-deploys-enabled.png)
19. If you only want to manually deploy, check that the branch you want to deploy is correct and click on 'Deploy Branch' in the 'Manual Deploy' section.
![View of Automatic Deploys and Manual Deploy sections of Deployment page](/readme-documents/deployment-screenshots/auto-manual-deploy.png)
20. When your app has successfully deployed you will see a 'Your app was successfully deployed' message like this:
![View of successful deployment on Deployment page](/readme-documents/deployment-screenshots/successful-deployment.png)
21. Click on 'View' and you will be taken to the deployed application. 

### Forking the GitHub Repository

Forking the GitHub repository allows you to produce a personal copy of the original repository/someone else's project that you can amend without affecting the original repository. To do this:

1. Log in to GitHub.
2. Navigate to the repository that you want to fork. 
3. In the repository header locate the button that says 'Fork' and click on it.  
4. When the repository is copied you will be taken to your copy of the repository. 

### Making a Local Clone

In order to work on a repository you have forked, you will need to clone it to your computer. In order to do this: 

1. Log in to GitHub and locate the repository fork you want to make a local clone of. 
2. Underneath the Settings button at the top of the repository there is a button with a dropdown arrow that says 'Code'. Click on it.  
3. To clone the repository using HTTPS, undeneath 'Clone' select 'HTTPS' so that there is an orange line underneath 'HTTPS'. Click on this button:

![View of local clone button](/readme-documents/screenshots/local-clone-button.png)

4. Open the Terminal in your IDE/editor. 
5. Change the current working directory to the one where you want the cloned directory to be located.  
6. Type 'git clone' and then paste the URL you copied earlier. It will look like this with your username instead of 'YOUR-USERNAME' and the name of the forked repository you are cloning instead of 'NAME OF REPOSITORY YOU ARE CLONING': 

![View of terminal command to clone fork](/readme-documents/screenshots/clone-command.png)

7. Press enter and your local clone will be created. 

For more information on forking and cloning repositories, see [GitHub Docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and this [GitHub Guide](https://guides.github.com/activities/forking/). 

## Credits 

### Code

* The code for importing the colorama module and the use of that module to print coloured text to the terminal was taken from [this youtube video](https://www.youtube.com/watch?v=u51Zjlnui4Y) entitled 'How to Print Colored Text in Python (Colorama Tutorial)' by Tech with Tim. 
* The idea for using a Board class for the player and computer boards and the Board instance attributes of name, type, guesses and ships was taken from the Code Institute example Battleships project.
* The while loop validation structure in the get_player_row_guess and get_player_column_guess functions was taken from the Code Institute Love Sandwiches project.
* The except statement structure in the validate_player_row_guess function was taken from the Code Institute Love Sandwiches project.
* The code for creating alphabet dictionaries of capital letter keys and number values or number keys and capital letter values was taken from an answer given by user10084443 on [this Stack Overflow post](https://stackoverflow.com/questions/453576/is-there-a-fast-way-to-generate-a-dict-of-the-alphabet-in-python) 
* The array-backed grid means of creating the boards was inspired by point 8 (16.2.2 Populating the Grid) in [this Program Arcade Games with Python and Pygame, Chapter 16: Array-Backed Grids article](http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids). 
* Having to use return to make recursive functions work was a bug solved by an answer given by roippi on [this Stack Overflow post](https://stackoverflow.com/questions/17778372/why-does-my-recursive-function-return-none)
      
### Content

* The inventor of the original battleships pen and paper game.
* This [Code Institute sample README file](https://github.com/Code-Institute-Solutions/SampleREADME) was used for guidance in preparing this README file and for the Deployment section as well as the Code Institute sample 'Ultimate Battleships' README file, this [GitHub Docs guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and this [GitHub Guide](https://guides.github.com/activities/forking/). 

### Acknowledgments

Many thanks to:
* My mentor, Gerard McBride, for his help and guidance.
* The Code Institute tutors for their support. 
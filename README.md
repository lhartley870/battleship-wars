# Battleship Wars
Battleship Wars is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The player plays against the computer to try and find all of the computer's battleships before the computer finds all of the player's ships. Each battleship is 2 spaces long on a board and is either placed horizontally or vertically at random. This game will be useful for battleships/game enthusiasts as the computer has been programmed to think like a human when the computer gets a hit, so making the experience as close to playing a real human as possible.  

The live project can be viewed [here](). 

![Responsive view of live website Home page](/readme-documents/screenshots/home-page-screenshot.png)

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

I used [Lucidchart]() to create flow charts for the logic of my application, which can be found here: 
* []()  

## How to Play
Battleship Wars is based on the classic board game which was originally a pen and paper game but then became popular as a board game by Milton Bradley. You can find out more about the game on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this application the player enters their name and two boards are generated. The boards are 10 spaces by 10 spaces. The columns are marked A-J and the rows are marked 1-10. Each space on the boards is represented with a dot. The letters, numbers and board dots all appear in white.

The player and computer each have 5 ships of 2 spaces long on their boards. The player's ships are revealed on the player's board; the computer's ships are concealed on its board. The board spaces occupied by player's ships are represented by the letter 'S' which is coloured green. The ships are randomly placed either horizontally or vertically, never diagonally. The player is also informed that two ships will also not be placed directly next to each other either horizontally or vertically on the board.

The player goes first and guesses a coordinate on the board e.g. 1A. The computer then takes a guess. If a guess is a hit then a red '*' symbol appears at the relevant board space and the player receives 1 point. A miss is represented by a '0' which is coloured yellow and receives 0 points. 

The player and computer continue to take turns making guesses until one player sinks all 5 of the other player's battleships, reaching a score of 10 and winning the game. If both the computer and the player reach a score of 10 during the last round of the game, the game is a draw. 

## Features
### Existing Features
* **Board Rows and Columns**
  To make guessing coordinates easier for the player, the columns are given letters instead of numbers to differentiate them from the row numbers. This prevents the user from becoming confused between the row and column and accidentally making a guess they didn't intend which could be the case if both columns and rows were numbered. Behind the scenes, within the Python code logic, the letters are converted back into numbers to allow for easier processing of the data. 

* **Random Ship Placement**
  When the player and computer boards are generated at the start of the game, 5 ships of 2 spaces long are placed at random on each board. Each ship is randomly placed either horizontally or vertically (not diagonally) on the board. Also, no two ships are next to each other horizontally or vertically. The python code is set up so that when the first ship in a set is created, its coordinates on the board and the immediate horizontal and vertical coordinates around the ship cannot be occupied by another ship. These occupied coordinates are updated as each ship in the set is created so that the next ship cannot occupy the spaces and surrounding coordinates of all the ships created before it in the set of 5. All the ship location coordinates are saved in an instance attribute of the applicable Board class instance so that the ships are printed to the same location during the game, every time the player's board is updated with guesses and re-printed. 

  The player can see his/her own ships which are marked with a green 'S' on the player's board. The computer board does not print the location of the computer's ships. 

* **Accepts User Input**
  The user is able to enter a name at the beginning of a new game. This name is used in the game's welcome message, in the heading for the player's board e.g. 'Steve's Board' and in the message printed at the end of the game if the player has won e.g. 'STEVE WINS!' to personalise the player's experience. 

  The player's board position guess is required for each round of the game. The player has to input a row between 1 and 10 (inclusive) and a column between A and J (inclusive) to select their guess. 

  Once a round is completed the player has to enter a 'y' to continue the current game or can alternatively enter 'n' to start a new game.

* **Input Validation and Error Checking**
  The player is unable to enter a row guess that is not a number or is not a row number on the board (1-10 inclusive). If the player does make an invalid entry they will be prompted to enter a number between 1 and 10. 

  The player is unable to enter a column guess that is not a column letter on the board (A-J inclusive). It does not matter if the column guess made by the player is lowercase or uppercase as the python code will convert it to uppercase. If the player tries to make a guess that is not a letter A-J they will be asked to make a guess between the letters A and J. Also, if the column guess is invalid, the user does not have to enter their guess all over again. Their valid row selection will remain so they will just need to enter a valid column letter. 

  The player is unable to make the same board coordinate guess twice. All of the player's guesses are saved in a 'guesses' attribute for the player board instance of the Board class. When a player makes a guess, this is checked against the player's previous guesses and the player will be told that they have made that guess before and will be prompted to enter an alternative guess. 

  The player is only able to enter a 'y' to continue to the next round of the current game or an 'n' to start a new game when asked whether they want to continue at the end of each round. It does not matter if the player enters a lowercase or uppercase 'y' or 'n' as the python code will convert it to lowercase. If the player makes any entry apart from an 'n' or a 'y' they will be informed and asked to make a valid entry. 

* **Round Updates**
  At the end of each round, once the player and computer have made their guesses, the player is updated with the latest round and game score information. 

  The user is informed of the coordinates of their last guess e.g. 3J and whether this guess was a hit or a miss. The player is also informed of the coordinates of the computer's last guess and whether this guess was a hit or a miss. The player is also given the updated game scores for the player and computer. Printing out the last guess of the player is particularly useful to the player so that they can be reminded of their last guess before continuing to the next round and making a new guess. 

* **Data Maintained in Class Instances**
  The python code for this application includes two classes: the Ship class and the Board class. 

  The 5 ships created for the player board and the 5 ships created for the computer board are all instances of the Ship class. This class contains the instance attributes length, position, orientation and barrier. Length and orientation are used by various methods within the Ship class. Position and barrier are used to save each ship instances coordinates on the board and the ship's surrounding horizontal and vertical coordinates, respectively. The ship instances are generated by calling the applicable function which is assigned to a Board class instance attribute. From this attribute a board instance attribute is created for each ship object. The ship locations on the board and their surrounding coordinates for each ship instance can then be accessed for the applicable board via the board's instance attributes.

  The Ship class also has various methods that can be utilised by the ship instances to generate each ship's non-clashing coordinates and surrounding coordinates within a ship set of 5. 

  The Board class is used to create instances of player board and computer board for each game. As well as the ship objects being instance attributes for the Board instances as mentioned above, this class has instance attributes of name, type, guesses, hits and misses and hit barrier coordinates. The type attribute is used to save the board type (either player or computer), the name attribute is used to save the player's name or 'computer' for the Computer's board instance. Guesses is used to save the opposing player's guesses against the applicable board (ie. the computer's guesses are saved against the player's board and vice versa). Hits and misses is used to record an 'H' for hit or 'M' for miss so that hits can be easily located and the applicable hit coordinate can be found by using the matching list index. The barrier coordinates attribute is used to save the surrounding coordinates of complete ships once hit by the computer so that the computer does not guess these coordinates for future guesses (described further in the 'Playing Against a 'Human' Computer section below). 

### Further Feature Ideas
* 

## Data Model

## Technologies Used

### Languages 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) programming language for the logic of the application.

### Libraries, Resources and Programs
* 

## Testing

Please see the separate [TESTING.md file](TESTING.md) for details of the project testing carried out. 

## Deployment

### Heroku

This project was deployed to Heroku according to the following steps: 

1. 

![View of Heroku when application deployed]()

## Credits 

### Code

* 
      
### Content

* 

### Acknowledgments

Many thanks to:
* My mentor, Gerard McBride, for his help and guidance.
* The Code Institute tutors for their support. 
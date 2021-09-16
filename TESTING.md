# Testing

## Validator
[The PEP8 Online Validator Service](http://pep8online.com/) was used for testing the python code for the site. The following result shows that no errors have been found: 
* [Python code in run.py file result](/readme-documents/validator-results/validator-clear.png)

Initially when the project was run through the validator the following errors were shown:
+ [Python code in run.py file initial result](/readme-documents/validator-results/validator-warnings.png).
* These were all errors for the same issue and stated the issue to be *'line break before binary operator'*. This was resolved by moving the applicable lines breaks to after the binary operators, in all cases the binary operator being a '+'.    

## UX (User Experience) Stories Testing
1. 

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)

    *   

2. 

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)

    * 

3.  

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)
    
    * 

4. 

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)

    *  

5. 

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)

    * 

6. 

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)

    * 

7. 

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)
 
    * 

8.  

    ![Responsive view of live application](/readme-documents/application-screenshots/.png)
    
    * 

## Manual Testing of Functionality of the Game

The manual testing of the application was carried out on the following devices:

1. Mobile phone (Apple iPhone 11)
2. Laptop (Apple MacBook Pro)

The application was tested on the following browsers on both of the above devices:

1. [Google Chrome](https://www.google.co.uk/chrome/?brand=FHFK&gclid=EAIaIQobChMI3b-xi9y38QIVBrTtCh2I1g3AEAAYASAAEgJN5vD_BwE&gclsrc=aw.ds)
2. [Microsoft Edge](https://www.microsoft.com/en-us/edge)
3. [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
4. [Safari](https://www.apple.com/uk/safari/) 


The application was fully tested as it was being developed in the local terminal. The application was then further tested after deployment on the above devices on the above browsers. Even though the appearance of the deployed application was not within the developer's control (as the Code Institute deployment terminal was used), the application was tested on a variety of browsers in any case. The testing comments below apply to all of the above devices and browsers, unless otherwise specified. 

### Manual Testing in the Code Institute Heroku Terminal 

1. When the deployed terminal opens, the 'NEW GAME' message and prompt asking for the player's name comes up as expected.
2. Entering the player name personalises the Welcome message and the Board heading above the player's board e.g. 'Lianne's Board'. Entering the name in lowercase or uppercase does not matter. The name is changed so that only the first letter is capitalised. Entering no name or a name that is just blank spaces means that the word 'Player' is used as the player's name as expected.
3. The Welcome message and rules of the game appear in the terminal as expected.
4. The player and computer boards appear as expected with letters A to J across the top and numbers 1 to 10 down the left hand side. There are no missing dots representing the board spaces and all dots are in alignment.
5. Ships only appear on the player board and ship occupied spaces are shown with a green 'S' as expected. There are 5 ships, 2 spaces long. The ships are randomly placed either horizontally or vertically. None of the ships are next to each other horizontally or vertically. The game is restarted several times to make sure that the ships are appearing in different locations on the player board each time. 
6. The player is prompted to enter a row number as expected.
7. Entering nothing, a symbol or a letter displays the expected 'invalid data' message and the user is asked to try again.
8. Entering a number that is not between 1 and 10 (inclusive) displays the expected 'You must enter a row number between 1 and 10' message and the player is asked to try again.
9. Entering a number between 1 and 10 (inclusive) raises no errors as expected.
10. The player is then prompted to enter a column letter.
11. Entering nothing, a symbol, a number or a letter that is not between A and J (inclusive) displays the expected 'You must enter a column letter between A and J' message and the player is asked to try again.
12. Entering a letter between A and J (inclusive) raises no errors unless the player has already made that guess. It does not matter if the player enters an uppercase or lowercase letter between A and J.
13. The information displayed at the end of the round displays as expected. The message regarding whether the computer has hit or miss a ship was checked against the player board after each round to check that the reporting of a hit or miss was correct. The scores were checked to make sure that the applicable player's score went up by 1 point if they had a hit.
14. The user is asked to enter y to continue or n to start a new game.
15. Entering a variety of letters apart from y or n, a number, a symbol or an empty space displays the message that 'Only y or n are valid entries' as expected and the user is prompted to try again. 
16. Entering n (whether uppercase or lowercase) starts a new game and the player is prompted to enter their name, all as expected. 
17. Entering the same coordinate as guessed for the first game does not raise a message that the player has already made that guess, showing that the guesses for the previous game have been cleared. 
18. Entering y (whether lowercase or uppercase) prints the boards showing the hits and misses from the last round as expected. The boards display the player and computer's guesses correctly with either a yellow '0' for a miss at the applicable coordinate or a red '*' for a hit. This is checked after each round. 
19. The player entering a guess that they have made before displays the message 'You have already made this guess, try another!' as expected and the user is prompted to enter a new guess.
20. If the player has entered a valid row number but an invalid column letter, they are only prompted to re-enter the column letter, not the row number as well, as expected.
21. When the computer gets a hit, the computer should only guess one of the 4 coordinates directly above, to the right, below or to the left of the hit coordinate until it hits the second half of the ship. This was checked with every computer hit to make sure this was happening.
22. As the player has been told that ships cannot be placed next to each other horizontally or vertically (but can be next to each other diagonally), the python code has been written so that once the computer has hit a complete ship it will no longer guess the spaces horizontally or vertically next to that ship. This was monitored throughout playing the game to ensure that the computer was not making guesses in these spaces. The computer behaved as expected.
23. When a player has won the game, the message displays as expected with the player's name being displayed as the winner if the player wins. The scores were checked to make sure they were correct and all was as expected.
24. A new game is automatically started with the 'NEW GAME' message being displayed and the player being asked for their name. If the player chooses to enter their name and begin a new game, the ships should be in a new location, which they were. The scores should be reset back to 0 for each player and entering the same guess as the last game should not raise a message that the player has already made that guess as all previous game data should be wiped and started afresh. This was checked and all was as expected. 
25. The game was run several times on both devices mentioned above on a variety of browsers (Chrome, Firefox, Safari and Microsoft Edge) and worked as expected each time. 

### Manual Testing in the Local Terminal

As well as all of the points tested in the Code Institute Heroku terminal mentioned above, the backend logic was checked using print statements throughout the code at all stages in the local terminal as the application was being built. When the game was complete, the following points in particular were checked to ensure the correct running of the game.

26. The player's ship coordinates were printed at the start of a new game and were checked against the green 'S' symbols printed on the player's board to make sure that they matched up. All was as expected.
27. The computer's ship coordinates were also printed at the start of a new game and were checked against the red '*' symbols printed on the computer's board when the developer entered those coordinates to make sure they matched up. All was as expected.
28. The player's board guesses property, hits_misses property and hit_barrier_coords property values as well as those for the computer's board were printed at the start of a new game to make sure that they were all empty lists. All was as expected. 
29. The number of computer hits was printed for each round to check that this matched up with the computer's score. All was as expected.
29. If the computer had no hits or an even number of hits, print statements were used to check if the guesses generated by the computer were within the guesses already made by the computer or the hit_barrier_coords list and if the guess had to be repeated to generate coordinates that were valid. All was as expected.
30. If the computer had hit half of a ship (so had an odd score overall):
    * a list of the coordinates surrounding that hit was printed and checked to make sure it was correct;
    * a list of all the guesses made so far by the computer was printed and checked to make sure it was correct;
    * a list of hit_barrier_coords was printed and checked to make sure that the coordinates matched up with those surrounding any ships hit by the computer;
    * a list of coordinates surrounding the hit coordinate that were not valid for guessing was printed after checking whether any of the coordinates had already been guessed, were not on the board, or were within the hit_barrier_coords list; 
    * the revised list of coordinates surrounding the hit coordinate was printed after the invalid coordinates were removed to see what the guess options were for the computer;
    * the computer's guess was then printed; 
    * the revised list of coordinates surrounding the hit coordinate was printed each time the computer guessed a wrong surrounding coordinate, to make sure that the list of surrounding coordinates for the computer to guess from was narrowed each time until the computer hit the second half of the ship;
    * if the resulting guess hit the second half of a ship: 
        * the coordinate for the first part of the ship being hit and the coordinate for the second part of the ship being hit were printed and checked to make sure they were correct; 
        * a 'SHIP 1', 'SHIP 2', 'SHIP 3', 'SHIP 4' or 'SHIP 5' statement was printed after print statements were included at the relevant places in the code to indicate the hit ship - this ship number was checked against the ship coordinates noted at the beginning of the game and displayed on the player board;
        * the relevant ship's surrounding coordinates were printed and checked;
        * the overall list of hit_barrier_coords for all ships hit by the computer so far was printed and checked; 
        * the guesses made so far by the computer were printed and checked;
        * the list of hit_barrier_coords was printed again to make sure that the surrounding coordinates for the ship just hit were added to the list; 
        * the computer's list of guesses to date was re-printed to make sure that the barrier coordinates were not added to that list (the barrier coordinates not guessed by the computer could not be added to that list as it would cause issues e.g. those coordinates would be printed as misses on the player board even though the computer hadn't guessed them). 
    * All of the above points were checked as the game progressed and the results were as expected. 
    * A visual check of the player board as the game progressed was also made to ensure that once a ship was hit by the computer, the computer no longer guessed any coordinates horizontally or vertically next to that ship. All was as expected.
    * When the game ended and a new game was started, the coordinates of the new computer ships and player's ships were checked to make sure they were different to the last game and the guesses, hits_misses and barrier_coords board property lists were back to being empty lists.
 
## Further Testing

### Friends and Family

Friends and family were sent a link to the deployed application to highlight any user experience or functionality issues. The following devices and browsers were tested without any issues being flagged:
* iPhone 12 - Safari browser
* Moto G9 Plus - Chrome browser

## Fixed Bugs

* A number of the functions within the python code are recursive. Intially the function calling itself was not working. This was resolved by making sure that the function calling itself was included after a return statement. This bug was solved with the help of an answer given by roippi on [this Stack Overflow post](https://stackoverflow.com/questions/17778372/why-does-my-recursive-function-return-none).
* Initially I was trying to use a variable as the start value in a range function but this did not work so a different approach using an integer start value was taken. 
* Initially I was trying to create a dictionary with 'H' and 'M' keys to represent hits and misses with guess coordinates as the values in the Board class _add_guess_results method. This did not work as the dictionary would only contain one 'H' key and one 'M' key. I then remembered that dictionary keys have to be unique and so that is why only one 'H' key and one 'M' key was being permitted. A different approach was therefore used. 
* Initially I saved the result of running the _get_ship_orientation method of the Ship class orientation as a Ship class attribute. However, I quickly realised that the same orientation was being used for all ships generated. I therefore changed the orientation attribute to an instance attribute instead of a class attribute.
* When I was creating the filter_surrounding_coordinates function, I found that the function was not filtering out all of the coordinates that it should. This was because I had included for invalid coordinates to be removed from the hit_surrounding_coordinates list within the for loop, so the loop was not working properly as the list it was looping through was changing all the time. I fixed this by creating a separate empty list of invalid_coords. I used the loop to add invalid coordinates to that list and then ran a separate for loop to remove the invalid coordinates from the hit_surrounding_coordinates list which resolved the issue.

## Unfixed Bugs

* The developer is not aware of any unfixed bugs. 
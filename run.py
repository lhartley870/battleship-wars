# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

scores = {'Player': 0, 'Computer': 0}


class Ship:
    """
    Ship class. Sets the ship length. Has methods culminating
    in a final get_board_positions method which generates the board
    coordinates for the ship.
    """
    def __init__(self):
        """
        Creates an instance of Ship with the instance attribute length.
        """
        self.length = 2
        self.orientation = None
        self.position = None
        self.barrier = None

    def get_ship_orientation(self):
        """
        Method to generate a random orientation of horizontal or
        vertical used by the get_ship_position method
        """
        orientation = random.choice(('Horizontal', 'Vertical'))
        return orientation

    def get_board_row_or_column(self):
        """
        Method to generate a board row or column number
        used by the get_ship_position method.
        """
        chosen_row_or_column = random.randrange(1, 11)
        return chosen_row_or_column

    def get_ship_position(self):
        """
        Method to generate a board row and starting column number
        for horizontally oriented ships and a board column and starting
        row number for vertically oriented ships used by the
        get_board_positions method.
        Stores the orientation to the orientation instance attribute.
        """
        orientation = self.get_ship_orientation()
        self.orientation = orientation
        # If statement applies where the ship is horizontally oriented.
        if orientation == 'Horizontal':
            row = self.get_board_row_or_column()
            starting_column = self.get_board_row_or_column()
            if (starting_column - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return row, starting_column
        # Else statement applies where the ship is vertically oriented.
        else:
            column = self.get_board_row_or_column()
            starting_row = self.get_board_row_or_column()
            if (starting_row - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return starting_row, column

    def get_board_positions(self):
        """
        Method that uses the ship orientation, board row and starting column
        for horizontally oriented ships and the ship orientation, board column
        and starting row for vertically oriented ships returned by the
        get_ship_position method, along with the ship's length, to generate
        a list of board coordinates for the ship.
        """
        ship_position = self.get_ship_position()
        row, column = ship_position
        board_coordinates = []
        # If statement applies where the ship is horizontally oriented.
        if self.orientation == 'Horizontal':
            column_positions = [column]
            for ind in range(self.length - 1):
                column_position = column_positions[ind]
                column_position += 1
                column_positions.append(column_position)
            for column_position in column_positions:
                board_coordinate = []
                board_coordinate.append(row)
                board_coordinate.append(column_position)
                board_coordinates.append(board_coordinate)
        # Else statement applies where the ship is vertically oriented.
        else:
            row_positions = [row]
            for ind in range(self.length - 1):
                row_position = row_positions[ind]
                row_position += 1
                row_positions.append(row_position)
            for row_position in row_positions:
                board_coordinate = []
                board_coordinate.append(row_position)
                board_coordinate.append(column)
                board_coordinates.append(board_coordinate)
        self.position = board_coordinates
        return board_coordinates

    def horizontal_ship_barrier(self):
        """
        Gets the immediate board coordinates surrounding a horizontal ship.
        Takes a ship's coordinates (ship length of 2 board spaces) and gets
        the immediate surrounding coordinates in the row above, same row and
        row below. Adds all those coordinates to a barrier_coordinates list
        and returns the list.
        """
        row = self.position[0][0]
        column_1 = self.position[0][1]
        column_2 = self.position[1][1]
        above_row = row + 1
        below_row = row - 1
        left_column = column_1 - 1
        right_column = column_2 + 1
        barrier_row_above = [
            [above_row, left_column],
            [above_row, column_1],
            [above_row, column_2],
            [above_row, right_column]
        ]
        barrier_same_row = [
            [row, left_column],
            [row, right_column]
        ]
        barrier_row_below = [
            [below_row, left_column],
            [below_row, column_1],
            [below_row, column_2],
            [below_row, right_column]
        ]
        barrier_coordinates = (barrier_row_above
                               + barrier_same_row
                               + barrier_row_below)

        return barrier_coordinates

    def vertical_ship_barrier(self):
        """
        Gets the immediate board coordinates surrounding a vertical ship.
        Takes a ship's coordinates (ship length of 2 board spaces) and gets
        the immediate surrounding coordinates in the row above, same rows as
        the ship and the row below. Adds all those coordinates to a
        barrier_coordinates list and returns the list.
        """
        column = self.position[0][1]
        row_1 = self.position[0][0]
        row_2 = self.position[1][0]
        above_row = row_1 - 1
        below_row = row_2 + 1
        left_column = column - 1
        right_column = column + 1
        barrier_left_column = [
            [above_row, left_column],
            [row_1, left_column],
            [row_2, left_column],
            [below_row, left_column]
        ]
        barrier_same_column = [
            [above_row, column],
            [below_row, column]
        ]
        barrier_right_column = [
            [above_row, right_column],
            [row_1, right_column],
            [row_2, right_column],
            [below_row, right_column]
        ]
        barrier_coordinates = (barrier_left_column
                               + barrier_same_column
                               + barrier_right_column)

        return barrier_coordinates

    def get_barrier_coordinates(self):
        """
        Gets the coordinates immediately surrounding a ship depending
        upon whether the ship is horizontally or vertically orientated.
        Saves the surrounding coordinates to the ship's barrier instance
        attribute and returns the coordinates.
        """
        if self.orientation == 'Horizontal':
            barrier_coordinates = self.horizontal_ship_barrier()
        else:
            barrier_coordinates = self.vertical_ship_barrier()
        self.barrier = barrier_coordinates
        return barrier_coordinates

    def check_occupied_coordinates(
            self, occupied_coordinates, new_coordinates):
        """
        Checks a list of new coordinates against a list of occupied
        coordinates.
        For each new coordinate checked a True or False value
        is added to the checked_results list (True if there is a match
        and False if there is not). The method returns an integer being the
        sum of the list elements (True being a value of 1 and False a value
        of 0).
        """
        checked_results = []
        for new_coordinate in new_coordinates:
            for occupied_coordinate in occupied_coordinates:
                if new_coordinate == occupied_coordinate:
                    checked_results.append(True)
                else:
                    checked_results.append(False)
        return sum(checked_results)


def create_ship(occupied_coordinates):
    """
    Creates an instance of the Ship class and utilises the class
    get_board_positions method to generate the ship instance's board
    coordinates. Utilises the class method of check_occupied_coordinates to
    make sure that the ship instance's board coordinates do not clash with
    those already taken by another ship on the board or a barrier around
    another ship on the board. If the coordinates are already taken, this
    function calls itself repeatedly until coordinates that do not clash are
    obtained. Once coordinates that do not clash are obtained, the ship's
    barrier coordinates are obtained using the class method of
    get_barrier_coordinates. The unavailable coordinates variable is
    updated with the new ship's coordinates and its barrier coordinates.
    The ship instance object and the updated unavailable coordinates are
    returned.
    """
    unavailable_coordinates = occupied_coordinates
    ship = Ship()
    ship_position = ship.get_board_positions()
    position_clash_result = ship.check_occupied_coordinates(
        occupied_coordinates, ship_position)
    if position_clash_result > 0:
        return create_ship(occupied_coordinates)
    else:
        ship_barrier = ship.get_barrier_coordinates()
        unavailable_coordinates += ship_position + ship_barrier
        return ship, unavailable_coordinates


def create_ship_set():
    """
    Creates a set of 5 ship objects and a list of their coordinates.
    Creates ship_1, ship_1's coordinates and ship_1's barrier coordinates.
    Adds the ship_1 coordinates and ship_1 barrier coordinates to create the
    occupied_coordinates variable to pass to the create_ship function to create
    a non-overlapping ship_2 object. Saves the ship_2 object returned from the
    create_ship function and the updated occupied_coordinates to create ship_3.
    This is repeated until all 5 ships are created. Creates a list of all 5
    ships' coordinates and returns that list together with the 5 ship objects.
    """
    ship_1 = Ship()
    ship_1_position = ship_1.get_board_positions()
    ship_1_barrier = ship_1.get_barrier_coordinates()
    occupied_coordinates = ship_1_position + ship_1_barrier
    ship_2_data = create_ship(occupied_coordinates)
    ship_2 = ship_2_data[0]
    occupied_coordinates = ship_2_data[1]
    ship_3_data = create_ship(occupied_coordinates)
    ship_3 = ship_3_data[0]
    occupied_coordinates = ship_3_data[1]
    ship_4_data = create_ship(occupied_coordinates)
    ship_4 = ship_4_data[0]
    occupied_coordinates = ship_4_data[1]
    ship_5_data = create_ship(occupied_coordinates)
    ship_5 = ship_5_data[0]
    all_ship_coordinates = (ship_1.position
                            + ship_2.position
                            + ship_3.position
                            + ship_4.position
                            + ship_5.position)

    return ship_1, ship_2, ship_3, ship_4, ship_5, all_ship_coordinates


class Board:
    """
    Board class. Sets the board type (player or computer), the player's name,
    the locations of the board's 5 ships and each ship object. Also contains a
    list to store the guesses made in relation to the board and a list to store
    whether the guesses are hits or misses. Has methods culminating in a final
    print_board method which prints the board showing the other player's hits
    and misses and (for the player's board only) the location of the 5 ships.
    """
    def __init__(self, type, name):
        """
        Creates an instance of Board
        """
        self.type = type
        self.name = name
        self.ship_data = create_ship_set()
        self.ships = self.ship_data[5]
        self.ship_1 = self.ship_data[0]
        self.ship_2 = self.ship_data[1]
        self.ship_3 = self.ship_data[2]
        self.ship_4 = self.ship_data[3]
        self.ship_5 = self.ship_data[4]
        self.guesses = []
        self.hits_misses = []

    def create_board(self):
        """
        Creates a list with each nested list representing each row on
        the board. Row 1 contains numbers 1 - 10 representing each column
        on the board. Each subsequent row has a number as its first element
        followed by 10 '.' elements to represent numbers 1 - 10 down the left
        hand side of the board and each '.' representing an available space/
        cell on the board.
        """
        grid = []
        row_one = [column_number for column_number in range(1, 11)]
        # Creates a space to add to the top left hand corner of the board
        row_one.insert(0, ' ')
        grid.append(row_one)
        # Adds the row number and 10 '.' cells for each row on the board
        cells = [cell for cell in range(10)]
        for cell in cells:
            cells[cell] = '.'
        for row_number in range(1, 11):
            grid_row = [row_number]
            for cell in cells:
                grid_row.append(cell)
            grid.append(grid_row)
        return grid

    def add_ships(self):
        """
        Adds the 5 ships to the board. Each board space occupied by a ship
        is represented by an 'S'.
        """
        grid = self.create_board()
        if self.type == 'player':
            for ship in self.ships:
                grid[ship[0]][ship[1]] = 'S'
        return grid

    def add_guess_results(self):
        """
        Adds the results of the guesses to the board. A hit is represented
        by a '*' and a miss is represented by a '0'.
        """
        grid = self.add_ships()
        for i in range(len(self.guesses)):
            row_coordinate = self.guesses[i][0]
            column_coordinate = self.guesses[i][1]
            if self.hits_misses[i] == 'H':
                grid[row_coordinate][column_coordinate] = '*'
            else:
                grid[row_coordinate][column_coordinate] = '0'
        return grid

    def add_column_letters(self):
        """
        Replaces the column numbers along the top of the board with letters
        in readiness for printing the board for the player to view.
        """
        grid = self.add_guess_results()
        alphabet_dictionary = {i: chr(i + 64) for i in range(1, 11)}
        for i in range(1, 11):
            grid[0][i] = alphabet_dictionary[i]
        return grid

    def print_board(self):
        """
        Prints the board for the player to view.
        """
        grid = self.add_column_letters()
        # Converts all items in the grid (the board) to strings
        for row in range(11):
            for item in range(11):
                grid[row][item] = str(grid[row][item])
        """
        Takes each nested list of string elements within the overall grid
        list, concatenates all the string elements within each nested list
        with two spaces added between each element, deletes each nested list
        and then replaces it with the concatenated string. The end result is
        an overall grid/board list containing string elements; one string
        element for each row of the board.
        """
        for row in range(11):
            row_string = '  '.join(grid[row])
            grid[row].clear
            grid[row] = row_string
        """
        Row 10 has one more digit than the other single digit numbered rows
        and so the alignment of the cells on the grid/board is wrong in row
        10. To fix this, one space is removed between the '10' and the first
        cell in the row to bring the cells back into alignment
        """
        double_number_row = grid[10]
        sliced_double_number_row = double_number_row[3:]
        grid[10] = '10' + sliced_double_number_row
        """
        A Board heading is printed to indicate if the board is the player's
        board or the computer's board and the overall grid/board list is then
        looped through using a for loop to print each list element as a line
        on the board for the player to view.
        """
        print(f"\n{self.name}'s Board\n")
        [print(string) for string in grid]
        # Creates a line space underneath the computer board
        if self.type == 'computer':
            print('')


def new_game():
    """
    Starts a new game. Creates two instances of the Board class; one for
    the player's board and one for the computer's board. Prints a personalised
    welcome message, the rules of the game and the player's board and
    computer's board to the terminal for the player to view.
    """
    # Requests the player's name from the player
    print('NEW GAME')
    player_name = input('What is your name?\n')
    player_name = player_name.title()
    computer_name = 'Computer'
    player_board_type = 'player'
    computer_board_type = 'computer'
    # Creates an instance of the Board class for the player's board
    player_board = Board(player_board_type, player_name)
    # Creates an instance of the Board class for the computer's board
    computer_board = Board(computer_board_type, computer_name)
    # Prints a personalised welcome message and rules to the terminal
    line_separator = '---------------------------------------'
    print(f"\nWelcome, {player_name}, to Battleship Wars!")
    print(line_separator)
    print("You and the computer each have 5 ships to find:")
    print("1 x 5 spaces, 1 x 4 spaces, 2 x 3 spaces and 1 x 2 spaces.")
    print("Your ships are represented on your board with an 'S'.")
    print("1 point will be scored for each hit, 0 points for a miss.")
    print("The first player to hit all of the other player's ships and reach")
    print("10 points wins the game!")
    print(line_separator)
    # Prints the player's board and computer's board to the terminal
    player_board.print_board()
    computer_board.print_board()
    return player_board, computer_board


def get_player_row_guess():
    """
    Gets a row guess from the player.
    Runs a while loop to collect a row number from the player, which
    must be a number between 1 and 10. The loop will continue to request
    a row number until a valid number is provided.
    Once a valid row number has been provided, the function returns the
    string number as an integer.
    """
    while True:
        player_row_guess = input("Enter a row number:\n")
        if validate_player_row_guess(player_row_guess):
            break
    return int(player_row_guess)


def validate_player_row_guess(value):
    """
    Inside the try converts the player's row guess from a string into an
    integer. Raises a ValueError if the string cannot be converted into
    an integer or, if the string can be converted into an integer, if the
    integer is not between 1 and 10 (inclusive). Returns True if no exceptions
    are raised or otherwise False to feed back into the get_player_row_guess
    function.
    """
    try:
        rows = [x for x in range(1, 11)]
        row_guess = int(value)
        if row_guess not in rows:
            raise ValueError('You must enter a row number between 1 and 10')
    except ValueError as e:
        print(f'Invalid data: {e}, try again')
        return False
    return True


def get_player_column_guess():
    """
    Gets a column guess from the player.
    Runs a while loop to collect a column letter from the player, which
    must be a letter between A and J. The loop will continue to request
    a column letter until a valid letter is provided.
    Once a valid column letter has been provided, the function returns an
    uppercase version of the letter in case the player has inputted a
    lowercase letter.
    """
    while True:
        player_column_guess = input("Enter a column letter:\n")
        if validate_player_column_guess(player_column_guess):
            break
    return player_column_guess.upper()


def validate_player_column_guess(value):
    """
    Inside the try converts the player's column guess string to uppercase in
    the event the player has entered a lowercase letter. Raises a ValueError
    if the string does not match with an uppercase letter between A and J
    (inclusive). Returns True if no exceptions are raised or otherwise False
    to feed back into the get_player_column_guess function.
    """
    try:
        columns = [chr(i + 64) for i in range(1, 11)]
        column_guess = value.upper()
        if column_guess not in columns:
            raise ValueError
    except ValueError:
        print('You must enter a column letter between A and J')
        return False
    return True


def check_duplicate_answer(board):
    """
    Calls the functions to get the player's or computer's guess.
    If the computer_board is passed as an argument, this function runs the
    functions that obtain and validate the player's row and column guesses.
    The column guess is converted into a number as the column letters are
    there in a superficial capacity only to make guessing easier for the
    player but a column number is used to reference the applicable column
    in the code. Puts the row number and column number into an array and
    runs a while loop to check that the player has not already made the same
    guess. The loop will cause this function to continue to call itself until
    the player makes a guess that they have not already made before.
    If the player_board is the argument, this function runs a while loop to
    check that the computer has not already made the same guess. The loop will
    cause this function to continue to call itself until the computer makes
    a guess that it has not made before.
    """
    if board.type == 'computer':
        row = get_player_row_guess()
        column = get_player_column_guess()
        alphabet_dictionary = {chr(i + 64): i for i in range(1, 11)}
        column_number = alphabet_dictionary[column]
        player_answer = [row, column_number]
        while not validate_player_guess(player_answer, board):
            return check_duplicate_answer(board)
        return player_answer
    else:
        computer_answer = get_computer_guess()
        while computer_answer in board.guesses:
            return check_duplicate_answer(board)
        return computer_answer


def validate_player_guess(list_value, computer_board):
    """
    Inside the try checks whether the list containing the player's row and
    column guess is within the list of lists containing the player's previous
    guesses. Raises a ValueError if the player's guess has been made before.
    Returns True if no exceptions are raised or otherwise False to feed back
    into the check_duplicate_answer function.
    """
    try:
        if list_value in computer_board.guesses:
            raise ValueError
    except ValueError:
        print('You have already made this guess. Try another!')
        return False
    return True


def update_guesses_list(board, guess):
    """
    Updates the list of guesses for the computer board with the player's
    guess and updates the list of the guesses for the player_board with the
    computer's guess.
    """
    board.guesses.append(guess)


def check_guess_result(board, guess):
    """
    Checks whether the player/computer's guess is a hit or a miss and
    updates the list of hits and misses for the computer_board (in the case
    of a player's guess), or the player_board (in the case of the computer's
    guess) with a 'H' for a hit or an 'M' for a miss.
    """
    if guess in board.ships:
        board.hits_misses.append('H')
    else:
        board.hits_misses.append('M')


def get_last_hit(player_board):
    """
    Gets the last computer guess coordinate that was a hit.
    Gets the hits_misses list and the guesses list for the
    player board, saves the lists as local variables, reverses
    the lists and locates the index of the first 'H' for hit in
    the reversed list. Finds the coordinate at the matching index
    in the reversed guesses list and returns it.
    """
    hits_misses = player_board.hits_misses.copy()
    hits_misses.reverse()
    guesses = player_board.guesses.copy()
    guesses.reverse()
    last_hit_index = hits_misses.index('H')
    last_hit_coordinate = guesses[last_hit_index]
    return last_hit_coordinate


def get_hit_surrounding_coordinates(player_board):
    """
    Gets a list of coordinates surrounding the computer's
    last hit coordinate and returns the list.
    """
    last_hit_coordinate = get_last_hit(player_board)
    row = last_hit_coordinate[0]
    column = last_hit_coordinate[1]
    hit_surrounding_coordinates = [
        [row - 1, column - 1],
        [row, column - 1],
        [row + 1, column - 1],
        [row - 1, column],
        [row + 1, column],
        [row - 1, column + 1],
        [row, column + 1],
        [row + 1, column + 1]
    ]
    return hit_surrounding_coordinates


def filter_surrounding_coordinates(player_board):
    """
    Filters coordinates surrounding computer's last hit.
    Obtains the coordinates surrounding the computer's last
    hit and the list of all the computer's guesses made so far.
    Creates a list of all the coordinates on the board.
    Iterates through the surrounding coordinates and creates
    an invalid_coords list of any of those coordinates that have
    either already been guessed or are not on the board.
    Iterates through the invalid_coords list and removes those
    coordinates from the surrounding coordinates list. Returns
    the surrounding coordinates list.
    """
    hit_surrounding_coordinates = get_hit_surrounding_coordinates(player_board)
    guesses_made = player_board.guesses
    all_board_coordinates = []
    for x in range(1, 11):
        for y in range(1, 11):
            coordinate = [x, y]
            all_board_coordinates.append(coordinate)
    invalid_coords = []
    for coord in hit_surrounding_coordinates:
        if coord in guesses_made or coord not in all_board_coordinates:
            invalid_coords.append(coord)
    for coord in invalid_coords:
        hit_surrounding_coordinates.remove(coord)
    return hit_surrounding_coordinates


def get_computer_guess():
    """
    Generates a random row number between 1 and 10 and a random column
    number between 1 and 10 and puts them in a list to represent the
    computer's guess.
    """
    chosen_row = random.randrange(1, 11)
    chosen_column = random.randrange(1, 11)
    computer_guess = [chosen_row, chosen_column]
    return computer_guess


def update_scores(computer_board, player_board):
    """
    Updates the scores.
    Adds 1 to 'Player' score if player's guess was a hit.
    Adds 1 to 'Computer' score if computer's guess was a hit.
    Nothing is added to the existing scores for a miss.
    """
    if computer_board.hits_misses[-1] == 'H':
        scores['Player'] += 1
    if player_board.hits_misses[-1] == 'H':
        scores['Computer'] += 1


def print_round_results(computer_board, player_board):
    """
    Prints the round results to the terminal.
    Gets the player and computer scores and the last player guess and
    computer guess in the format [number, number]. Changes the second
    number (column) to the corresponding board column letter and converts
    the row number to a string. Concatenates the row and column strings to
    create the board reference in the format 5F for both the last player
    guess and last computer guess. Checks whether the last result in the
    hits_misses list for each board is 'H' or not and creates a resulting
    variable with the word 'Hit' or 'Miss' accordingly.
    Prints the score, guess and hit/miss result for the player and the
    computer to the terminal.
    """
    player_score = scores['Player']
    computer_score = scores['Computer']
    alphabet_dictionary = {i: chr(i + 64) for i in range(1, 11)}
    player_guess_numbers = computer_board.guesses[-1]
    player_guess_column = alphabet_dictionary[player_guess_numbers[1]]
    player_guess = str(player_guess_numbers[0]) + player_guess_column
    computer_guess_numbers = player_board.guesses[-1]
    computer_guess_column = alphabet_dictionary[computer_guess_numbers[1]]
    computer_guess = str(computer_guess_numbers[0]) + computer_guess_column
    if player_board.hits_misses[-1] == 'H':
        computer_result = 'Hit!'
    else:
        computer_result = 'Miss'
    if computer_board.hits_misses[-1] == 'H':
        player_result = 'Hit!'
    else:
        player_result = 'Miss'
    print('---------------------------------------')
    print('After the last round the scores are:')
    print('Player:')
    print(f'     Score - {player_score}')
    print(f'     Guess - {player_guess}, {player_result}')
    print('Computer:')
    print(f'     Score - {computer_score}')
    print(f'     Guess = {computer_guess}, {computer_result}')
    print('---------------------------------------')


def check_game_over():
    """
    Checks whether the current game is over.
    If either the player or computer has hit all the battleships on the
    other's board (i.e. if either the player or computer has reached a
    score of 10), the function returns True, else it returns False.
    """
    if scores['Player'] == 10 or scores['Computer'] == 10:
        return True
    else:
        return False


def print_game_results(computer_board, player_board):
    """
    Prints the game results to the terminal.
    Prints a message to inform the player that the game is over.
    Checks whether the game has been won by the player or computer or
    whether the game is a draw and prints confirmation to the terminal.
    Prints the final scores of the player and the computer to the terminal.
    """
    player_wins = scores['Player'] == 10 and scores['Computer'] < 10
    computer_wins = scores['Computer'] == 10 and scores['Player'] < 10
    print('........GAME OVER........')
    if player_wins:
        print(f'{player_board.name.upper()} WINS!')
    elif computer_wins:
        print('COMPUTER WINS!')
    else:
        print("IT'S A DRAW!")
    print('Final scores:')
    print(f"     Player - {scores['Player']}")
    print(f"     Computer - {scores['Computer']}")
    print('---------------------------------------')


def check_continue():
    """
    Checks whether the user wants to continue.
    Runs a while loop to ask the user whether they want to continue to the
    next round or start a new game. The answer must either be a y (to
    continue) or n (to start a new game). If the player provides an uppercase
    Y or N this is converted into lowercase. The while loop will continue to
    request an answer until a valid y or n is provided by the player.
    """
    while True:
        continue_answer = input(
                'Enter y to continue or n to start a new game\n')
        continue_answer = continue_answer.lower()
        if validate_continue(continue_answer):
            break
    return continue_answer


def validate_continue(answer):
    """
    Inside the try checks whether the player's answer is a y or n.
    Raises a ValueError if the string does not match with a lowercase
    y or n. Returns True if no exceptions are raised or otherwise False
    to feed back into the check_continues function.
    """
    try:
        valid_answer = ['y', 'n']
        if answer not in valid_answer:
            raise ValueError
    except ValueError:
        print('Only y or n are valid entries')
        return False
    return True


def process_continue(answer, computer_board, player_board):
    """
    Processes the player's decision to continue or exit the current game.
    When the player was asked whether they wanted to continue the current
    game or start a new game as part of the check_continue function, if
    the player answered 'y' the updated computer and player boards are printed
    and if the player answered 'n', the scores are cleared and the main
    function is called to start a new game.
    """
    if answer == 'y':
        print_updated_boards(computer_board, player_board)
    else:
        clear_scores()
        main()


def print_updated_boards(computer_board, player_board):
    """
    Prints an updated player board and computer board.
    Prints the player board showing the player's ships and all the computer's
    hits and misses.
    Prints the computer board showing all the player's hits and misses.
    """
    player_board.print_board()
    computer_board.print_board()


def clear_scores():
    """
    Sets the scores back to 0.
    """
    scores['Player'] = 0
    scores['Computer'] = 0


def run_next_round(player_board, computer_board):
    """
    Collective function calling the necessary functions to work through
    one round of the game.
    """
    player_guess = check_duplicate_answer(computer_board)
    update_guesses_list(computer_board, player_guess)
    check_guess_result(computer_board, player_guess)
    computer_guess = check_duplicate_answer(player_board)
    update_guesses_list(player_board, computer_guess)
    check_guess_result(player_board, computer_guess)
    update_scores(computer_board, player_board)
    print_round_results(computer_board, player_board)
    is_game_over = check_game_over()
    if is_game_over:
        print_game_results(computer_board, player_board)
    else:
        proceed_next_round = check_continue()
        process_continue(proceed_next_round, computer_board, player_board)


def main():
    """
    Main function.
    Creates a new game. Runs a while loop to keep running the next round
    of the game until either the computer or player hits all the ships on
    the other's board and reaches the maximum score of 10 (or there is a
    draw of 10). Once a score of 10 is reached by either the player, the
    computer or both, the scores are set back to 0 and the function calls
    itself to start a new game all over again.
    """
    player_board, computer_board = new_game()
    while scores['Player'] < 10 and scores['Computer'] < 10:
        run_next_round(player_board, computer_board)
    clear_scores()
    return main()


main()

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class Ship:
    """
    Ship superclass. Sets the ship length. Has methods culminating
    in a final get_board_positions method which generates the board
    coordinates for the ship.
    """
    def __init__(self, length):
        """
        Creates an instance of Ship with the instance attribute length.
        """
        self.length = length

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
        """
        orientation = self.get_ship_orientation()
        # If statement applies where the ship is horizontally oriented.
        if orientation == 'Horizontal':
            row = self.get_board_row_or_column()
            starting_column = self.get_board_row_or_column()
            if (starting_column - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return orientation, row, starting_column
        # Else statement applies where the ship is vertically oriented.
        else:
            column = self.get_board_row_or_column()
            starting_row = self.get_board_row_or_column()
            if (starting_row - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return orientation, starting_row, column

    def get_board_positions(self):
        """
        Method that uses the ship orientation, board row and starting column
        for horizontally oriented ships and the ship orientation, board column
        and starting row for vertically oriented ships returned by the
        get_ship_position method, along with the ship's length, to generate
        a list of board coordinates for the ship.
        """
        ship_position = self.get_ship_position()
        orientation, row, column = ship_position
        board_coordinates = []
        # If statement applies where the ship is horizontally oriented.
        if orientation == 'Horizontal':
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
        return board_coordinates


class OccupiedCoordinatesMixin:
    """
    Mixin to check a list of new coordinates against a list
    of occupied coordinates.
    """
    def check_occupied_coordinates(
            self, occupied_coordinates, new_coordinates):
        """
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


class AircraftCarrier(Ship):
    """
    Subclass of Ship superclass. Sets the ship
    length of an aircraft carrier to 5.
    """
    def __init__(self):
        """
        Creates an instance of AircraftCarrier subclass utilising the
        superclass initialiser method and passing it a ship length
        of 5.
        """
        super().__init__(5)


class Battleship(Ship, OccupiedCoordinatesMixin):
    """
    Subclass of Ship superclass. Sets the ship
    length of a battleship to 4. Also inherits from
    OccupiedCoordinatesMixin class.
    """
    def __init__(self):
        """
        Creates an instance of Battleship subclass utilising the
        superclass initialiser method and passing it a ship length
        of 4.
        """
        super().__init__(4)


class Submarine(Ship, OccupiedCoordinatesMixin):
    """
    Subclass of Ship superclass. Sets the ship
    length of a submarine to 3. Also inherits from
    OccupiedCoordinatesMixin class.
    """
    def __init__(self):
        """
        Creates an instance of Submarine subclass utilising the
        superclass initialiser method and passing it a ship length
        of 3.
        """
        super().__init__(3)


class Cruiser(Ship, OccupiedCoordinatesMixin):
    """
    Subclass of Ship superclass. Sets the ship
    length of a cruiser to 3. Also inherits from
    OccupiedCoordinatesMixin class.
    """
    def __init__(self):
        """
        Creates an instance of Cruiser subclass utilising the
        superclass initialiser method and passing it a ship length
        of 3.
        """
        super().__init__(3)


class Destroyer(Ship, OccupiedCoordinatesMixin):
    """
    Subclass of Ship superclass. Sets the ship
    length of a destroyer to 2. Also inherits from
    OccupiedCoordinatesMixin class.
    """
    def __init__(self):
        """
        Creates an instance of Destroyer subclass utilising the
        superclass initialiser method and passing it a ship length
        of 2.
        """
        super().__init__(2)


def create_ship_type(ship_subclass, occupied_coordinates):
    """
    Creates an instance of the applicable Ship subclass and utilises
    the Ship superclass get_board_positions method to generate the
    ship instance's board coordinates. Utilises the OccupiedCoordinatesMixin
    class method of check_occupied_coordinates to make sure that the
    ship instance's board coordinates do not clash with those already taken
    by another ship on the board. If the coordinates are already taken,
    this function calls itself repeatedly until coordinates that do not
    clash are obtained.
    """
    unavailable_coordinates = occupied_coordinates
    ship_type = ship_subclass()
    ship_type_position = ship_type.get_board_positions()
    position_clash_result = ship_type.check_occupied_coordinates(
        occupied_coordinates, ship_type_position)
    if position_clash_result > 0:
        return create_ship_type(ship_subclass, occupied_coordinates)
    else:
        for ship_type_coordinate in ship_type_position:
            unavailable_coordinates.append(ship_type_coordinate)
        return ship_type_position, unavailable_coordinates


def create_ship_set():
    """
    Creates one of each type of ship together with non-overlapping board
    coordinates for each ship type and returns an overall list of all board
    coordinates for all the ships.
    """
    aircraft_carrier = AircraftCarrier()
    aircraft_carrier_position = aircraft_carrier.get_board_positions()
    occupied_coordinates = aircraft_carrier_position
    battleship_data = create_ship_type(Battleship, occupied_coordinates)
    occupied_coordinates = battleship_data[1]
    submarine_data = create_ship_type(Submarine, occupied_coordinates)
    occupied_coordinates = submarine_data[1]
    cruiser_data = create_ship_type(Cruiser, occupied_coordinates)
    occupied_coordinates = cruiser_data[1]
    destroyer_data = create_ship_type(Destroyer, occupied_coordinates)
    occupied_coordinates = destroyer_data[1]

    return occupied_coordinates


class Board(OccupiedCoordinatesMixin):
    """
    Board class. Sets the board type (player or computer), the player's name,
    and the locations of the board's 5 ships. Also contains a list to store the
    guesses made in relation to the board and a list to store whether the
    guesses are hits or misses. Has methods culminating in a final print_board
    method which prints the board showing the other player's hits and misses
    and (for the player's board only) the location of the 5 ships. Also
    inherits from the OccupiedCoordinatesMixin class to allow comparisons
    of board coordinates.
    """
    def __init__(self, type, name):
        """
        Creates an instance of Board
        """
        self.type = type
        self.name = name
        self.ships = create_ship_set()
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
    print("17 points wins the game!")
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
    If the player_board is passed as a parameter, this function runs the
    functions that obtain and validate the player's row and column guesses.
    The column guess is converted into a number as the column letters are
    there in a superficial capacity only to make guessing easier for the
    player but a column number is used to reference the applicable column
    in the code. Puts the row number and column number into an array and
    runs a while loop to check that the player has not already made the same
    guess. The loop will cause this function to continue to call itself until
    the player makes a guess that they have not already made before.
    """
    if board == player_board:
        row = get_player_row_guess()
        column = get_player_column_guess()
        alphabet_dictionary = {chr(i + 64): i for i in range(1, 11)}
        column_number = alphabet_dictionary[column]
        player_answer = [row, column_number]
        while not validate_player_guess(player_answer, board):
            return check_duplicate_answer(board)
        return player_answer


def validate_player_guess(list_value, player_board):
    """
    Inside the try checks whether the list containing the player's row and
    column guess is within the list of lists containing the player's previous
    guesses. Raises a ValueError if the player's guess has been made before.
    Returns True if no exceptions are raised or otherwise False to feed back
    into the check_duplicate_answer function.
    """
    try:
        if list_value in player_board.guesses:
            raise ValueError
    except ValueError:
        print('You have already made this guess. Try another!')
        return False
    return True


def run_next_round(player_board, computer_board):
    """
    Collective function calling the necessary functions to work through
    one round of the game
    """
    check_duplicate_answer(player_board)


player_board, computer_board = new_game()
run_next_round(player_board, computer_board)

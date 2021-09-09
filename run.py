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

    orientation = random.choice(('Horizontal', 'Vertical'))

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
        # If statement applies where the ship is horizontally oriented.
        if self.orientation == 'Horizontal':
            row = self.get_board_row_or_column()
            starting_column = self.get_board_row_or_column()
            if (starting_column - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return self.orientation, row, starting_column
        # Else statement applies where the ship is vertically oriented.
        else:
            column = self.get_board_row_or_column()
            starting_row = self.get_board_row_or_column()
            if (starting_row - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return self.orientation, starting_row, column

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

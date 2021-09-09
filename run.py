# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class Ship:
    def __init__(self, length):
        self.length = length

    orientation = random.choice(('Horizontal', 'Vertical'))

    def get_board_row_or_column(self):
        chosen_row_or_column = random.randrange(1, 11)
        return chosen_row_or_column

    def get_ship_position(self):
        if self.orientation == 'Horizontal':
            row = self.get_board_row_or_column()
            starting_column = self.get_board_row_or_column()
            if (starting_column - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return self.orientation, row, starting_column
        else:
            column = self.get_board_row_or_column()
            starting_row = self.get_board_row_or_column()
            if (starting_row - 1) + self.length > 10:
                return self.get_ship_position()
            else:
                return self.orientation, starting_row, column

    def get_board_positions(self):
        ship_position = self.get_ship_position()
        orientation, row, column = ship_position
        board_coordinates = []
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

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class Ship:
    def __init__(self, length):
        self.length = length

    orientation = random.choice(('Horizontal', 'Vertical'))

    def get_horizontal_ship_start(self):
        all_columns = [x for x in range(1, 20)]
        odd_columns = [x for x in all_columns if x % 2 != 0]
        column_start_position = random.choice(odd_columns)
        return column_start_position

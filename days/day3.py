from base_test import BaseUnitTest, run_tests
from functools import reduce
import re

class Part:

    def __init__(self, x, y, number):
        self.start_x = x
        self.y = y
        self.number = number
        self.end_x = None
    
    def add_number(self, number):
        self.number += number

    def finalize(self, end_x):
        self.end_x = end_x
        self.number = int(self.number)

    def __key(self):
        return (self.start_x, self.end_x, self.y, self.number)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Part):
            return self.__key() == other.__key()
        return NotImplemented

    def is_coord_adjacent(self, x, y):
        return self.y == y and self.start_x <= x and self.end_x >= x

    @property
    def finished(self):
        return self.end_x is not None


class Symbol:

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.parts = set()

    def add_adjacent_parts(self, direction, parts):
        x_value = self.x + direction["x"]
        y_value = self.y + direction["y"]
        for part in parts:
            if part.is_coord_adjacent(x_value, y_value) and part not in self.parts:
                self.parts.add(part)

    def calculate_sum(self, part_2=False):
        if part_2:
            if len(self.parts) <= 1 or self.symbol != "*":
                return 0
            return reduce(lambda x, y: x*y, [part.number for part in self.parts])
        
        return sum([part.number for part in self.parts])
        

class Day3(BaseUnitTest):

    day = "3"
    expected_part_1_sample_result = 4361
    expected_part_1_input_result = 539637
    expected_part_2_sample_result = 467835
    expected_part_2_input_result = 82818007

    directions = [{ "x": -1, "y": 0 }, { "x": 1, "y": 0 }, { "x": 0, "y": -1 }, { "x": 0, "y": 1 }, { "x": 1, "y": 1 }, { "x": -1, "y": 1 }, { "x": 1, "y": -1 }, { "x": -1, "y": -1 }]

    def get_grid_data(self, input):

        grid = [[char for char in line] for line in input.split("\n")]
        number_regex = re.compile("\d")

        symbols = []
        parts = []

        current_part = None
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if number_regex.match(cell):
                    if not current_part:
                        current_part = Part(x, y, cell)
                        parts.append(current_part)
                    else:
                        current_part.add_number(cell)
                else:
                    if cell != ".":
                        symbols.append(Symbol(x, y, cell))

                    if current_part and not current_part.finished:
                        current_part.finalize(x-1)
                        current_part = None

            if current_part and not current_part.finished:
                current_part.finalize(len(row)-1)
                current_part = None

        return parts, symbols

    def run_part_1(self, input):

        parts, symbols = self.get_grid_data(input)

        for symbol in symbols:
            for direction in self.directions:
                symbol.add_adjacent_parts(direction, parts)

        return sum([symbol.calculate_sum() for symbol in symbols])

    def run_part_2(self, input):

        parts, symbols = self.get_grid_data(input)

        for symbol in symbols:
            for direction in self.directions:
                symbol.add_adjacent_parts(direction, parts)
                    
        return sum([symbol.calculate_sum(True) for symbol in symbols])



if __name__ == "__main__":
    run_tests()
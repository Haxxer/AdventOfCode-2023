from base_test import BaseUnitTest, run_tests
from functools import reduce

class Day2Part2(BaseUnitTest):

    day = "2"
    part = "2"
    expected_sample_result = 2286
    expected_input_result = 70387

    def run_day(self, input):

        total_value = 0

        for string in input.split("\n"):

            games = [cube_pair for substr in string.split(": ")[-1].split("; ") for cube_pair in substr.split(", ")]
            
            cubes_present = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for game in games:
                color = game.split(" ")[1]
                number = int(game.split(" ")[0])
                cubes_present[color] = max(cubes_present[color], number)
            
            total_value += reduce(lambda x, y: x*y, cubes_present.values())

        return total_value



if __name__ == '__main__':
    run_tests()
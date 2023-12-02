from base_test import BaseUnitTest, run_tests
import re

class Day2Part1(BaseUnitTest):

    day = "2"
    part = "1"
    expected_sample_result = 8
    expected_input_result = 1734

    cube_limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def run_day(self, input):
        total_value = 0
        for string in input.split("\n"):
            game_id = int(string.split("Game ")[1].split(": ")[0])
            revealed_cubes = [{
                "number": int(cube_pair.split(" ")[0]),
                "color": cube_pair.split(" ")[1]
            } for substr in string.split(": ")[-1].split("; ") for cube_pair in substr.split(", ")]

            over = any([cube_set["number"] > self.cube_limits[cube_set["color"]] for cube_set in revealed_cubes])

            if not over:
                total_value += game_id

        return total_value



if __name__ == '__main__':
    run_tests()
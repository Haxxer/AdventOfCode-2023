from base_test import BaseUnitTest, run_tests
from functools import reduce

class Day2(BaseUnitTest):

    day = "2"
    expected_part_1_sample_result = 8
    expected_part_1_input_result = 1734
    expected_part_2_sample_result = 2286
    expected_part_2_input_result = 70387

    cube_limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def run_part_1(self, input):
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

    def run_part_2(self, input):

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
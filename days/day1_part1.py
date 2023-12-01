from base_test import BaseUnitTest, run_tests
import re

class Day1Part1(BaseUnitTest):

    day = "1"
    part = "1"
    expected_sample_result = 142
    expected_input_result = 54081

    def run_day(self, input):
        regex = re.compile("\\d")
        inputs = input.split("\n")
        input_groups = [regex.findall(input) for input in inputs]
        results = [int(group[0] + group[-1]) for group in input_groups]
        return sum(results)



if __name__ == '__main__':
    run_tests()
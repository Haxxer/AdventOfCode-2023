from base_test import BaseUnitTest, run_tests
import re

class Day1(BaseUnitTest):

    day = "1"

    expected_part_1_sample_result = 142
    expected_part_1_input_result = 54081

    expected_part_2_sample_result = 281
    expected_part_2_input_result = 54649

    valid_text_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def run_part_1(self, input):
        regex = re.compile("\\d")
        inputs = input.split("\n")
        input_groups = [regex.findall(input) for input in inputs]
        results = [int(group[0] + group[-1]) for group in input_groups]
        return sum(results)

    def run_part_2(self, input):

        inputs = input.split("\n")

        regexes = [re.compile("\\d")] + list(map(lambda x: re.compile(x), self.valid_text_numbers.keys()))

        input_groups = []
        for input_group in inputs:
            unsorted_group = []
            for regex in regexes:
                for digit in regex.finditer(input_group):

                    value = digit.group()
                    if value in self.valid_text_numbers:
                        value = self.valid_text_numbers[value]

                    unsorted_group.append((digit.span()[0], value))
                
            sorted_group = sorted(unsorted_group, key=lambda x: x[0])
            input_groups.append([group[1] for group in sorted_group])

        results = []

        for group in input_groups:
            first = group[0]
            last = group[-1]
            results.append(int(str(first) + str(last)))

        return sum(results)



if __name__ == '__main__':
    run_tests()
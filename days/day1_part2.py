from base_test import BaseUnitTest, run_tests
import re

class Day1Part2(BaseUnitTest):

    day = "1"
    part = "2"
    expected_sample_result = 281
    expected_input_result = 54649

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

    def run_day(self, input):

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

    def test_sample(self):
        sample_result = self.run_day(self.sample)
        self.validate_sample(sample_result)

    def test_input(self):
        input_result = self.run_day(self.input)
        self.validate_input(input_result)



if __name__ == '__main__':
    run_tests()
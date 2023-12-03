import unittest
unittest.TestLoader.sortTestMethodsUsing = None

class BaseUnitTest(unittest.TestCase):

    day = "1"

    part_1_sample = ""
    part_1_input = ""
    part_2_sample = ""
    part_2_input = ""

    expected_part_1_sample_result = 0
    expected_part_1_input_result = 0
    expected_part_2_sample_result = 0
    expected_part_2_input_result = 0

    def run_part_1(self, input):
        return 0

    def run_part_2(self, input):
        return 0

    def setUp(self):

        try:
            with open("days/{}/sample_part{}.txt".format(self.day, 1)) as f:
                self.part_1_sample = f.read()
        except FileNotFoundError:
            pass
        
        try:
            with open("days/{}/input_part{}.txt".format(self.day, 1)) as f:
                self.part_1_input = f.read()
        except FileNotFoundError:
            pass

        try:
            with open("days/{}/sample_part{}.txt".format(self.day, 2)) as f:
                self.part_2_sample = f.read()
        except FileNotFoundError:
            pass
        
        try:
            with open("days/{}/input_part{}.txt".format(self.day, 2)) as f:
                self.part_2_input = f.read()
        except FileNotFoundError:
            pass

    def test_part_1_sample(self):
        if not self.part_1_sample:
            return
        sample_result = self.run_part_1(self.part_1_sample)
        self.assertEqual(sample_result, self.expected_part_1_sample_result, "Part 1 sample result is not correct, expected {} but got {}".format(self.expected_part_1_sample_result, sample_result))

    def test_part_1_input(self):
        if not self.part_1_input:
            return
        input_result = self.run_part_1(self.part_1_input)
        self.assertEqual(input_result, self.expected_part_1_input_result, "Part 1 input result is not correct, expected {} but got {}".format(self.expected_part_1_input_result, input_result))

    def test_part_2_sample(self):
        if not self.part_2_sample:
            return
        sample_result = self.run_part_2(self.part_2_sample)
        self.assertEqual(sample_result, self.expected_part_2_sample_result, "Part 2 sample result is not correct, expected {} but got {}".format(self.expected_part_2_sample_result, sample_result))

    def test_part_2_input(self):
        if not self.part_2_input:
            return
        input_result = self.run_part_2(self.part_2_input)
        self.assertEqual(input_result, self.expected_part_2_input_result, "Part 2 input result is not correct, expected {} but got {}".format(self.expected_part_2_input_result, input_result))

def run_tests():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
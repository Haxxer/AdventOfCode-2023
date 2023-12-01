import unittest
unittest.TestLoader.sortTestMethodsUsing = None

class BaseUnitTest(unittest.TestCase):

    day = "1"
    part = "1"
    sample = ""
    input = ""
    expected_sample_result = 0
    expected_input_result = 0

    def run_day(self, input):
        return 0

    def setUp(self):

        try:
            with open("days/{}/sample_part{}.txt".format(self.day, self.part)) as f:
                self.sample = f.read()
        except FileNotFoundError:
            pass
        
        try:
            with open("days/{}/input_part{}.txt".format(self.day, self.part)) as f:
                self.input = f.read()
        except FileNotFoundError:
            pass

    def test_loaded(self):
        self.assertNotEqual(self.sample, "", "Sample input is empty")
        self.assertNotEqual(self.input, "", "Input is empty")

    def validate_sample(self, input):
        self.assertEqual(input, self.expected_sample_result, "Sample result is not correct, expected {} but got {}!".format(self.expected_sample_result, input))
    
    def validate_input(self, input):
        self.assertEqual(input, self.expected_input_result, "Input result is not correct, expected {} but got {}!".format(self.expected_input_result, input))

    def test_sample(self):
        sample_result = self.run_day(self.sample)
        self.validate_sample(sample_result)

    def test_input(self):
        input_result = self.run_day(self.input)
        self.validate_input(input_result)

def run_tests():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
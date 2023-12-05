from base_test import BaseUnitTest, run_tests
from collections import OrderedDict

class Mapping:

    def __init__(self, name, values):

        self.name = name
        self.values = values
        self.maps = None    

    def transpose_value(self, value):

        for data in self.values:
            dest_start, source_start, range_length = data

            source_end = source_start + range_length

            in_range = value >= source_start and value < source_end

            if in_range:
                value = (value-source_start)+dest_start
                break

        return self.maps[self.name].transpose_value(value) if self.name in self.maps else value

    @staticmethod
    def create_maps(input, paired=False):

        parts = [part.split("\n") for part in input.split("\n\n")]
        
        seeds = list(map(lambda x: int(x), parts[0][0].split(": ")[-1].split(" ")))

        if paired:
            index = 0
            new_seeds = []
            while index < len(seeds)-1:
                new_seeds.append(range(seeds[index], seeds[index]+seeds[index+1]))
                index += 2
            seeds = new_seeds

        print("Seeds calculated")
        
        maps = OrderedDict()

        for part in parts[1:]:

            source = part[0].split("-")[0]
            name = part[0].split("-")[2].split(" ")[0]
            values = [list(map(lambda x: int(x), section.split(" "))) for section in part[1:]]

            mapping = Mapping(name, values)
            mapping.maps = maps

            maps[source] = mapping

        print("Maps calculated")

        return maps, seeds
        

class Day5(BaseUnitTest):

    day = "5"
    dual=True
    expected_part_1_sample_result = 35
    expected_part_1_input_result = 289863851
    expected_part_2_sample_result = 46
    expected_part_2_input_result = 4541234123


    def run_part_1(self, input):
        maps, seeds = Mapping.create_maps(input)
        return min([maps["seed"].transpose_value(seed) for seed in seeds])

    def run_part_2(self, input):
        maps, seeds = Mapping.create_maps(input, True)
        solved_seeds = {}
        for ranges in seeds:
            print("Solving range {}-{}".format(ranges[0], ranges[-1]))
            for seed in ranges:
                if seed in solved_seeds:
                    continue
                solved_seeds[seed] = maps["seed"].transpose_value(seed)
        return min(solved_seeds.values())


if __name__ == "__main__":
    run_tests()
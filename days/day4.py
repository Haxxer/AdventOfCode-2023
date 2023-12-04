from base_test import BaseUnitTest, run_tests
import re

class Card:

    def __init__(self, card_number, numbers, winnings):
        self.card_number = card_number+1
        self.numbers = numbers
        self.winnings = winnings
        self.times_to_check = 1
        self.deck = None

    @classmethod
    def make_deck(self, input):
        regex = re.compile("\d+")
        cards = [card.split(": ")[1].split(" | ") for card in input.split("\n")]
        deck = [Card(index, regex.findall(card[0]), regex.findall(card[1])) for index, card in enumerate(cards)]
        for card in deck:
            card.deck = deck
        return deck

    def get_score(self):
        card_total = 0
        for number in self.numbers:
            if number in self.winnings:
                card_total = 1 if not card_total else card_total*2
        return card_total

    def get_compounding_score(self):

        card_score = 0
        for number in self.numbers:
            if number in self.winnings:
                card_score += 1

        if card_score:
            higher_cards = self.deck[self.card_number:min(len(self.deck), self.card_number + card_score)]

            for card in higher_cards:
                card.times_to_check += self.times_to_check

        return self.times_to_check


class Day4(BaseUnitTest):

    day = "4"
    expected_part_1_sample_result = 13
    expected_part_1_input_result = 21158
    expected_part_2_sample_result = 30
    expected_part_2_input_result = 6050769

    def run_part_1(self, input):
        return sum([card.get_score() for card in Card.make_deck(input)])

    def run_part_2(self, input):
        return sum([card.get_compounding_score() for card in Card.make_deck(input)])

if __name__ == "__main__":
    run_tests()
from card import Card
from enums import CardDigit, CardColor
from dataclasses import dataclass, field
from typing import List

@dataclass
class DeckConfig:
  colors: List = field(default_factory=lambda: [CardColor.RED, CardColor.BLUE, CardColor.YELLOW, CardColor.GREEN])
  digit_one_cards: int = 3
  digit_two_cards: int = 2
  digit_three_cards: int = 2 
  digit_four_cards: int = 2 
  digit_five_cards: int = 1

  def card_numbers(self):
    return [self.digit_one_cards, self.digit_two_cards, self.digit_three_cards, self.digit_four_cards, self.digit_five_cards]

class Deck():
  def __init__(self, deck_config=DeckConfig):
    self.cards = []
    self.deck_config = DeckConfig()
    self.init_deck()

  def init_deck(self):
    card_numbers = self.deck_config.card_numbers()
    for color in self.deck_config.colors:
      for index, num in enumerate(card_numbers):
        self.cards.extend([Card(color, index+1) for _ in range(num)])

  def get_all_cards(self):
    return self.cards

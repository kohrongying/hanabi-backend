from card import Card
from enums import CardDigit, CardColor

@dataclass(frozen=True)
class DeckConfig:
  colors: list[CardColor] = [CardColor.RED, CardColor.BLUE, CardColor.YELLOW, CardColor.GREEN]
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
    self.deck_config = deck_config

  def init_deck(self):
    for color in self.deck_config.colors:
      card_numbers = self.deck_config.card_numbers()
      self.cards.append(Card(color, index + 1) for _ in range(x) for x, index in enumerate(card_numbers))


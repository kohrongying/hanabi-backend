import unittest
from deck import Deck, DeckConfig
from enums import CardStatus, CardColor, CardDigit

class TestDeckConfig(unittest.TestCase):
  def test_card_numbers(self):
    deck_config = DeckConfig()
    self.assertEqual([3,2,2,2,1], deck_config.card_numbers())

class TestDeck(unittest.TestCase):

  def test_deck_init(self):
      deck = Deck()
      cards = deck.get_all_cards()
      self.assertEqual(40, len(cards))


if __name__ == "__main__":
    unittest.main()
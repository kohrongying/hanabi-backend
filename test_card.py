import unittest
from card import Card
from enums import CardStatus, CardColor, CardDigit

class TestCard(unittest.TestCase):

  def test_card_init(self):
      card = Card(CardColor.RED, CardDigit.ONE)
      self.assertEqual(card.get_status(), CardStatus.IN_DECK)
      self.assertEqual(card.color, CardColor.RED)
      self.assertEqual(card.digit, CardDigit.ONE)

  def test_card_set_status(self):
      card = Card(CardColor.RED, CardDigit.ONE)
      card.set_status(CardStatus.ON_TABLE)
      self.assertEqual(card.get_status(), CardStatus.ON_TABLE)

if __name__ == "__main__":
    unittest.main()
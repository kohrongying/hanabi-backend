from enum import Enum

class CardStatus(Enum):
  IN_DECK = "DECK"
  IN_DISCARD = "DISCARD"
  ON_TABLE = "TABLE"
  ON_HAND = "HAND"

class CardColor(Enum):
  RED = "RED"
  BLUE = "BLUE"
  YELLOW = "YELLOW"
  GREEN = "GREEN"

class CardDigit(Enum):
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
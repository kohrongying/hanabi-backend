from enums import CardStatus

class Card():
  
  def __init__(self, color, digit):
    self.status = CardStatus.IN_DECK
    self.color = color
    self.digit = digit

  def get_status(self):
    return self.status

  def set_status(self, new_status):
    self.status = new_status

  def __str__(self):
    return f'Card color is {self.color}, digit is {self.digit}, status is {self.status}'

  def __repr__(self):
    return f'Card(color={self.color}, digit={self.digit}, status={self.status})'
  
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


  
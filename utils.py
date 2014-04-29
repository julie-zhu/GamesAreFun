class User(object):
  def __init__(self, username, nickname):
    self.username = username
    self.nickname = nickname
    
________________________________________
#unsure if to make separate classes for pieces or to just make one
#______________________CHESSMEN_______________________________
class Pawn(object):
  def __init__(self, x, y, color, promo): #promo(tion) is there in case it gets promoted
    self.x = x
    self.y = y #location
    self.color = color #team side
    self.promo = promo
    
class Rook(object):
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    
class Knight(object):
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    
class Bishop(object):
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    
class Queen(object):
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    
class King(object):
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    

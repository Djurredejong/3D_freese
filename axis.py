from motor import Motor

class Axes:
  def __init__(self):
    self.m_x=Motor(11,12,15,16)
    self.m_y=Motor(31,32,35,36)
    # Both axes start in the middle
    self.x = 0.
    self.y = 0.
    # Both axes can move 100 mm to both sides.
    self.x_max = 100.
    self.y_max = 100.
    # pitch is the movement in mm induced by a 360 degree turn
    self.pitch = 1.

  def angle(self,distance):
    return distance / self.pitch * 360 

  def move_x(self,dist=1):
    if abs(self.x + dist) <= self.x_max:
      self.x += m
      self.m_x.rotate( self.angle(distance) )

  def move_y(self,dist=1):
    if abs(self.y + dist) <= self.y_max:
      self.y += m
      self.m_y.rotate( self.angle(distance) )

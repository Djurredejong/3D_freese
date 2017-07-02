from motor import Motor
class RangeError(RuntimeError):
   def __init__(self, arg):
      self.args = arg

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

  def __print__(self):
    print("(%s, %s)mm" % self.position)

  def position(self):
    return (self.x, self.y)

  def angle(self,distance):
    return distance / self.pitch * 360 

  def move_x(self,dist=1):
    if abs(self.x + dist) <= self.x_max:
      self.x += m
      self.m_x.rotate_degrees( self.angle(dist) )
    else:
      raise RangeError("X-axis has moved to it's maximum extension") 

  def move_y(self,dist=1):
    if abs(self.y + dist) <= self.y_max:
      self.y += m
      self.m_y.rotate_degrees( self.angle(dist) )
    else:
      raise RangeError("Y-axis has moved to it's maximum extension") 

  def move(self,dist=1.,x=1.,y=1.):
    norm = (x**2+y**2)**.5
    x/=norm
    y/=norm
    if abs(self.x+dist*x) > self.x_max: 
      raise RangeError("X-axis has moved to it's maximum extension") 
    if abs(self.y+dist*y) > self.y_max: 
      raise RangeError("Y-axis has moved to it's maximum extension") 

    x_steps = self.angle(dist*x)//0.18
    y_steps = self.angle(dist*y)//0.18

    # use Bresenham algorithm to interleave X- and Y-steps

    # Determining which 'Octant' the current angle is in
    if x_steps < 0:
      x = -1
      x_steps *= -1
    if x_steps < 0:
      y = -1 
      y_steps *= -1
    if x_steps < y_steps:
      x,y = y,x
      x_steps,y_steps = y_steps,x_steps

    # Start of the actual algorithm
    deltaErr = abs(y_steps/float(x_steps))
    error = deltaErr - 0.5

    for sx in range(x_steps):
      self.m_x.rotate_steps(x)
      error = error+deltaErr
      if error >= 0.5:
        self.m_x.rotate_steps(y)
        error -= 1.0
      sleep(delta_t)


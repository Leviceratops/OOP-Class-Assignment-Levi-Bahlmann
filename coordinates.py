class Coordinates:
  def __init__(self, point = []):
    self.location = point

  def get_point(self):
    return self.location

  def set_point(self, x, y, z):
    self.location = [x, y, z]
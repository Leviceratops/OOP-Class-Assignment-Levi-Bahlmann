from coordinates import Coordinates
class ShapethreeD:
  def __init__(self, type, color, coords):
    self.shape_type = type
    self.shape_color = color
    self.coordinates = Coordinates(coords) 
  def volume(self):
    return None
      
  def surface_area(self):
    return None
      
  def get_type(self):
    return self.shape_type
      
  def get_color(self):
    return self.shape_color
      
  def set_type(self, type):
    self.shape_type = type
      
  def set_color(self, color):
    self.shape_color = color

  def get_point(self):
    return self.coordinates
      
  def set_point(self, coords):
    self.coordinates = coords

  def draw(self):
      print("""   
         
           """)
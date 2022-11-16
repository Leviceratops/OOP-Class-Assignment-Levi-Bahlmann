from threeDShape import ShapethreeD

class Cube(ShapethreeD):
    def __init__(self, type, color, s, coords):
        super().__init__(type, color, coords)
        self.cb_side = s

    def volume(self):
        return (self.cb_side)**3

    def surface_area(self):
        return ((self.cb_side)**2)*6

    def get_side(self):
        return self.cb_side

    def draw(self):
        print("""   
        
        
   .+------+     +------+     +------+     +------+     +------+.
 .' |    .'|    /|     /|     |      |     |\     |\    |`.    | `.
+---+--+'  |   +-+----+ |     +------+     | +----+-+   |  `+--+---+
|   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
|  ,+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+   |
|.'    | .'    |/     |/      |      |      \|     \|    `. |   `. |
+------+'      +------+       +------+       +------+      `+------+



""")
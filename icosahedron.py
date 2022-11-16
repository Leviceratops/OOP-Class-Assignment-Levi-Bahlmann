from threeDShape import ShapethreeD
from math import sqrt

class Icosahedron(ShapethreeD):
    def __init__(self, type, color, e, coords):
        super().__init__(type, color, coords)
        self.ic_edge = e

    def volume(self):
        return (5*(3+sqrt(5))/12) * (self.ic_edge**3)

    def surface_area(self):
        return 5 * sqrt(3) * (self.ic_edge**2)

    def get_edge(self):
        return self.ic_edge

    def draw(self):
        print("""
        
        
        _-_.
     _-',^. `-_.
 ._-' ,'   `.   `-_ 
!`-_._________`-':::
!   /\        /\::::
;  /  \      /..\:::
! /    \    /....\::
!/      \  /......\:
;--.___. \/_.__.--;; 
 '-_    `:!;;;;;;;'
    `-_, :!;;;''
        `-!'         mn""")
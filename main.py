from threeDShape import ShapethreeD
from cube import Cube
from icosahedron import Icosahedron

# test shape / base class
new_shape = ShapethreeD("test", "black", [])

print(new_shape.get_type())
print(new_shape.get_color())
print(new_shape.volume())
print(new_shape.surface_area())
print(new_shape.set_point([None]))
print(new_shape.get_point())
new_shape.draw()


# cube (yes I picked the easiest shape, fight me)
cb = Cube("cube", "purple", 5, [])

print(cb.get_type())
print(cb.get_color())
print("The volume of this cube is %.f units cubed." % cb.volume())
print("The surface area of this cube is %.f units squared." % cb.surface_area())
print("The side length of this cube is %.f units." % cb.get_side())
print(cb.set_point([2 ,4 , 6]))
print(cb.get_point())
cb.draw()


# icosahedron (I chose this because it's a D20 dice from DnD haha)
ic = Icosahedron("icosahedron", "green", 20, [])

print(ic.get_type())
print(ic.get_color())
print("The volume of this icosahedron is %.3f units cubed." % ic.volume())
print("The surface area of this icosahedron is %.3f units squared." % ic.surface_area())
print("The edge length of this icosahedron is %.3f units." % ic.get_edge())
print(ic.set_point([7 ,21 ,11]))
print(ic.get_point())
ic.draw()
# add in draw function ASCII

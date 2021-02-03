from Graphics.rectangle import area as rectArea
from Graphics.dgraphics.sphere import spherearea 
from Graphics.dgraphics.cuboid import area as cuboidArea,perimeter as cuboidPerimeter
from Graphics.circle import *

print("\n\n Area of Sphere:\t",spherearea(5))
print("Area of Rectangle:\t",rectArea(5,3))
print("Area of Cuboid:\t",cuboidArea(5,3,10))
print("Area of circle:\t",area(5))
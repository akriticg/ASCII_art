#Version 1
#September 26, 2018
#Input from the user 'radius' defines the radius of the circle
#Diameter of a circle is twice the radius
#Going from top to bottom, and drawing chords of a circle at a  perpendicular distance from the center

import sys
import math

def main():
    radius = int(sys.argv[1])
    dia = 2 * radius
    SPACE = ' '
    CIRCLE = 'o'
    for k in range(-radius, radius, 1):
        chord_length = 2 * round(math.sqrt(math.fabs(radius*radius - k*k)))
        spaces = round((dia-chord_length) / 2)
        print(SPACE*spaces + CIRCLE*chord_length + SPACE*spaces)
        

main()



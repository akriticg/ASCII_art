# Version 1
# September 25, 2018
# Input from the user 'height' defines the height of the diamond
# Using one loop, number of stars in each line is determined depending
# on whether the line is above or below the mid line.
 
import sys

def main():
    height = int(sys.argv[1])
    SPACE = ' '
    STAR = '*'

    for i in range(1, height+1):

        if(i <= round(height/2)):
            no_star =  2*i - 1
            no_space = int((height - no_star) / 2)
            print(SPACE*no_space + STAR*no_star + SPACE*no_space)

        else:
            no_star =  2*(height + 1 - i) - 1
            no_space = int((height - no_star) / 2)
            print(SPACE*no_space + STAR*no_star + SPACE*no_space)

main()


#Version 1
#September 26, 2018
#Three inputs from the user - symbol, width and height
#Print full lines of symbol for the top and bottom, else just the left and right edge


def main():

    symbol = input("Enter the character you would like to use to draw the rectangle : ")
    SPACE = ' '
    width = int(input("Enter the width of the rectangle (>2) : "))
    while(width <= 2):
        width = int(input("Too small. Enter value >2 : "))
    height = int(input("Enter the height of the rectangle (>2) : "))
    while(height <= 2):
        height = int(input("Too small. Enter value >2 : "))

    for k in range(height):
        if(k == 0 or k == (height - 1)):
            print(symbol * width)
        else:
            print(symbol + (SPACE*(width-2)) + symbol)

main()
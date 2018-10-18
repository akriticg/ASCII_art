#Version 1
#September 26, 2018
#Input from the user 'base' defines the base of the tree
#Divide the tree into three parts in height direction - when at height, at base and the remaining
#Divide the three into two parts width wise - left and right


def main():
    base = int(input("Enter an odd integer >3 for length of base : "))
    while(base%2 == 0):
        base = int(input("Wrong input! Enter an odd number value for base : "))

    height = int((base+1) / 2)
    UNDERSCORE = '_'
    SPACE = ' '
    STAR = '*'
    FRONT_SLASH = '/'
    BACK_SLASH = '\\'

    for k in range(height, 0, -1):

        if(k == height):
            print(SPACE * int((base-2) / 2), STAR)

        elif (k < height and k > 1):
            for j in range(1, base+2):
                if(j < (base+2) / 2):
                    if(j == k):
                        print(FRONT_SLASH, end="")
                    else: print(SPACE, end="")
                else:
                    if(j == base+1-k):
                        print(BACK_SLASH, end="")
                    else : print(SPACE, end="")
            print()

        elif (k == 1):
            print(FRONT_SLASH + (UNDERSCORE*(base - 2)) + BACK_SLASH)



main()
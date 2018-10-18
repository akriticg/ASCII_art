'''
Version 1
Author : Akriti Chadda
October 11, 2018
This code contains three functions as follows :
1) cone : to draw the nose cone of the rocket
2) tail : to draw the tail of the rocket
3) body : to draw the fuselage body
'''
import sys

STAR = '*'
SPACE = ' '
EX = 'X'
UNDERSCORE = '_'
width = 0
segments = 0
nature = ''


def cone(base):

    '''
    input parameters : base = width of base of the cone
    (it is two less than the width of the fuselage)
    I start with 2 stars, if the base is even, else 1, and then go down one
    line at a time by 2 stars to make the nose.
    '''
    width = base + 2
    l = base % 2

    height_cone = base // 2 + l
    # num_stars is 2 when the base is even, 1 if odd
    num_stars = 2 if l == 0 else 1
    for k in range(height_cone):
        print(SPACE * ((width - num_stars) // 2) + STAR * num_stars)
        num_stars += 2


def tail(base):
    '''
    input parameters : base = width of tail of the cone
    Start with number of stars equal to half the width, and then add
    two stars until reaching the width.
    Then add one full row of stars equal to the base
    '''
    k = base // 2
    while k <= base:
        print(SPACE * ((base - k) // 2) + STAR * k)
        k += 2
    print(STAR * base)


def body(width, segments, nature):
    '''
    input parameters : width : the width of the fuselage,
    segment : the number of segment of squares in the fuselage and
    nature : whether the pattern will be 'striped' or 'nothing'
    This function draws the 'segments' number of squares of Xs of
    width 'width' if the nature is 'nothing'; otherwise, print alternating
    '_' and 'X'
    '''
    if nature == 'nothing':
        for k in range(segments * width + 1):
            print(EX * width)

    if nature == 'striped':
        l = width % 2
        for m in range(segments):
            for k in range(width // 2):
                print(UNDERSCORE * width)
            for k in range(width // 2 + l):
                print(EX * width)


def parameters():
    '''
    calculating the parameters needed for calling the functions
    '''
    global width
    global segments
    global nature
    width = int(sys.argv[1])
    segments = int(sys.argv[2])
    if len(sys.argv) == 4:
        nature = sys.argv[3]
    else:
        nature = 'nothing'


def main():

    global width
    global segments
    global nature

    parameters()
    cone(width - 2)
    body(width, segments, nature)
    tail(width)

main()

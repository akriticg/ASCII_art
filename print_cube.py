'''
Version 1
Author : Akriti Chadda
This program uses three functions, cube_top, cube_mid and cube_bottom to
draw the top, mid and bottom of the cube respectively.
'''

PLUS = '+'
SPACE = ' '
DIAGONAL = '/'
HORIZONTAL = '-'
VERTICAL = '|'


def cube_top(n):
    '''
input = n
output = top of the cube
'''
    print(SPACE * (n//2 + 1) + PLUS + (HORIZONTAL * (n*2) + PLUS))
    for k in range(n//2):
        print(SPACE * (n//2 - k) + DIAGONAL + SPACE * 2 * n + DIAGONAL +
              SPACE * k + VERTICAL)

    print(PLUS + HORIZONTAL * (n*2) + PLUS + SPACE * (n//2) + VERTICAL)


def cube_mid(n):
    '''
input = n
output = front face and mid of the cube
'''
    for _ in range(n//2 - 1):
        print(VERTICAL + SPACE * (2*n) + VERTICAL + SPACE * (n//2) + VERTICAL)

    print(VERTICAL + SPACE * (2*n) + VERTICAL + SPACE * (n//2) + PLUS)


def cube_bottom(n):
    '''
input = n
output = bottom part of the cube
'''
    for k in range(n//2, 0, -1):
        print(VERTICAL + SPACE * (2*n) + VERTICAL +
              SPACE * (k - 1) + DIAGONAL)

    print(PLUS + (HORIZONTAL * (n*2) + PLUS))


def main():
    n = int(input("Input cube size (multiple of 2): "))
    cube_top(n)
    cube_mid(n)
    cube_bottom(n)

main()

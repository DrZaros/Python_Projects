#A small program to find the area of a triangle with Heron's formula

import math
    
def heron():
    a = float(input('Put your first side here: '))
    b = float(input('Put your second side here: '))
    c = float(input('Put your third side here: '))

    s = float((a + b + c)/2)

    area = s * (s-a) * (s-b) * (s-c)

    area = math.sqrt(area)

    return area

print(heron(), 'units squared')

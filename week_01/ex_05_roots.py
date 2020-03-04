#https://www.coursera.org/learn/diving-in-python/programming/nxYyA/korni-kvadratnogho-uravnieniia
#запускать из консоли с параметрами 'python solution.py 1 -3 -4'
#в результате будут вывкдены корни квадратного уравнения

import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

root_D = (b ** 2 - 4 * a * c) ** 0.5
print(int((-b + root_D) / (2 * a)))
print(int((-b - root_D) / (2 * a)))

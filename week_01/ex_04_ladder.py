#https://www.coursera.org/learn/diving-in-python/programming/Lg9Hb/risuiem-liestnitsu
#запускать из консоли с параметрами 'python solution.py 5'
#в результате будет отрисована лестница в 5 ступеней

import sys


steps = int(sys.argv[1])
for step in range (0, steps):
    print('_' * (steps - 1) + 's' * (step + 1))
    steps -= 1

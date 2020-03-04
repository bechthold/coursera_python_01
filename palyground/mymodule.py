#https://www.coursera.org/learn/diving-in-python/programming/Mcs6i/summa-tsifr-v-strokie
#запускать из консоли с параметрами 'python solution.py 123'
#в результате будет посчитана сумма цифр в числе 123
import sys

digit_sum = 0;
for digit in sys.argv[1]:
    digit_sum += int(digit)
print(digit_sum)
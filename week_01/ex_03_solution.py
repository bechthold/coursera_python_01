import sys

digit_sum = 0;
for digit in sys.argv[1]:
    digit_sum += int(digit)
print(digit_sum)
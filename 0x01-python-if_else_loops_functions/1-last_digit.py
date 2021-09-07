#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    un_number = -number
else:
    un_number = number
last_digit = un_number

while last_digit > 10:
    last_digit  %= 10

if last_digit > 5:
    print('Last digit of', number, 'is', last_digit, 'and is greater than 5')
elif last_digit == 0:
    print('Last digit of', number, 'is', last_digit, 'and is 0')
elif last_digit < 6 and last_digit != 0:
    print('Last digit of', number, 'is', last_digit, 'and is less than 6 and not 0')

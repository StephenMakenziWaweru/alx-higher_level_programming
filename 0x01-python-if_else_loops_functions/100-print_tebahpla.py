#!/usr/bin/python3
for i in range(122, 96, -1):
    alt = True
    if i % 2 != 0:
        alt = False
    print("{}".format(chr(i) if alt else chr(i - 32)), end='')

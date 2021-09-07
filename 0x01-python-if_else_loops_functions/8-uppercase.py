#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            lower = True
        else:
            lower = False
        print("{}".format((chr(ord(str[i]) - 32)) if lower else
              str[i]), end="")
    print("")

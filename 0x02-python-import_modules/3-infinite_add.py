#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    sum = 0
    for i in range(len):
        sum += int(sys.argv[i + 1])
    print(sum)

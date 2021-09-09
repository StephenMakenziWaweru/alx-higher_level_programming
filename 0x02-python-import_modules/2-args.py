#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(len, "" if len == 1 else "s", "." if len == 0 else ":"))
    i = 1
    while i <= len:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

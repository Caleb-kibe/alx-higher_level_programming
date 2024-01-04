#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumation = 0
    for i in range(1, len(argv)):
        sumation += int(argv[i])
    print("{}".format(sumation))

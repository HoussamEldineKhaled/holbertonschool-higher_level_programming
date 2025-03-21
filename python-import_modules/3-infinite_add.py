#!/usr/bin/python3
import sys
if __name__ == "__main__":
    summation = 0
    for i in range(1, len(sys.argv)):
        summation += int(sys.argv[i])
print(summation)

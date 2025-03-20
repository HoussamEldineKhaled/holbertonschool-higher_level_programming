#!/usr/bin/python3
def uppercase(s):
    result = ""
    for i in range(0, len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            result += chr(ord(s[i]) - 32)
        else:
            result += s[i]
    print("{}".format(result))

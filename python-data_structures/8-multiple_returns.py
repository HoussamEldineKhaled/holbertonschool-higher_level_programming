#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), 0)
    return (len(sentence), sentence[0])

#!/usr/bin/python3
for alphabet in reversed(range(ord('a'), ord('z') + 1)):
    if (alphabet % 2 == 1):
        alphabet -= 32
    print("{:c}".format(alphabet), end="")

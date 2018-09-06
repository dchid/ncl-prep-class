import sys

def verify(guess):
    vals = [
        74,
        79,
        73,
        78,
        32,
        85,
        83,
        32,
        73,
        78,
        32,
        70,
        79,
        82,
        68
    ]

    for i, c in enumerate(guess):
        if ord(c) != vals[i]:
            return False
    return True


if len(sys.argv) != 1:
    print "Usage: python check.pyc"
    exit(1)

guess = raw_input("Enter your guess: ");

if verify(guess):
    print "That's correct!"
else:
    print "Wrong."

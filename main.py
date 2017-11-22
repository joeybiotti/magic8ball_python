import sys
import random

answer = True

while answer:
    question = raw_input("Ask a yes or no question. Press 'enter' to exit: ")

    answers = random.randint(1,5)

    if question == "":
        print "exiting program..."
        sys.exit()
    elif answers == 1:
        print "Yes!"
    elif answers == 2:
        print "Nope!"
    elif answers == 3:
        print "Maybe"
    elif answers == 4:
        print "I doubt it."
    elif answers == 5:
        print "Hell no!"
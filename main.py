import sys
import random

answer = True

while answer:
    question = raw_input("Ask a question: ")

    answers = random.randint(1,5)

    if question == "":
        sys.exit()
    elif answers == 1:
        print "yeah"
    elif answers == 2:
        print "nope"
    elif answers == 3:
        print "maybe"
    elif answers == 4:
        print "i doubt it"
    elif answers == 5:
        print "hell nah"
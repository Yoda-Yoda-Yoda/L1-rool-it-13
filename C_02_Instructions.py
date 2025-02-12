def yes_no(question):
    """checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:



        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":

            return "no"
        else:
            print("enter yes/no")


def instructions():
    """PRINTS INSTRUCTIONS"""

    print('''
**** Instructions ****

Roll the dice and try to win!
    ''')


#main routine

#testing loop
want_instructions = yes_no("do you want to read the instruction ").lower()

#display the instructions
if want_instructions == "yes":
    instructions()

print()
print("program continues ")
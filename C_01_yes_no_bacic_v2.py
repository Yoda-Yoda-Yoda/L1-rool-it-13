def yes_no(question):
    while True:

        """checks user response to a question is yes/no (y/n), returns 'yes' or 'no' """

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":

            return "no"
        else:
            print("enter yes/no")


#main routine

want_instructions = yes_no("\ndo you want to read the instruction ").lower()
want_coffee = yes_no("do you want coffee?")

print("we done")

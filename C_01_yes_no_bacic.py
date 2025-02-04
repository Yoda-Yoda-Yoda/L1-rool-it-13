want_instructions = input("\ndo you want to read the instruction ").lower()

if want_instructions == "yes" or want_instructions == "y":
    print("you said yes")
elif want_instructions == "no" or want_instructions == "n":
    print("you said no")
else:
    print("enter yes/no")



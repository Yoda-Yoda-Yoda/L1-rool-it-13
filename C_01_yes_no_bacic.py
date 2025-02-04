while True:
    want_instructions = input("\ndo you want to read the instruction ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("you said no")
        break
    else:
        print("enter yes/no")
        continue


print("we dpne")

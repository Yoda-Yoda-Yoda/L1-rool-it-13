import random

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

def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter and integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal?"))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one}  \t|  Roll 2: {roll_two}  \t  |  Total:  {total}")

    return total, double



def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f" {ends}  {statement} {ends}")

make_statement("Welcome to the Roll it 13 Game", "🍀")

# Main Starts here....

# at the start of the game. the computer / user score are both 0
comp_score = 0
user_score = 0
round_played = 0

game_history = []

want_instructions = yes_no("do you want to read the instruction ").lower()

#display the instructions
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()

while comp_score < game_goal and user_score < game_goal:

    round_played += 1

    # start of the loop
    make_statement(f"Round {round_played}", "🎲")

    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they qualify for double points
    if double_user == "yes":
        print("Great news  -  if you win, you will earn double points!!")

    # assume user goes first...
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    if user_points < comp_points:
        print("You start because your initial roll was less then the computer\n")

    if user_points == comp_points:
        print("The initial rolls were the same, the user starts!")

    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        if player_1_points >= 13:
            break

        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points}    | {second} {player_2_points}")

    # end of round

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # work out who won...
    if user_points > comp_points:
        winner = "user"
    else:
        winner = "computer"

    round_feedback = f"The {winner} won."


    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0

    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s points have been reset to zero"

    # double points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # output round results
    make_statement("Round Results", "=")
    print(f"User Points: {user_points}  |  Computer points: {comp_points} ")
    print(round_feedback)

    comp_score += comp_points
    user_score += user_points

    game_results = (f"Round {round_played}: User points: {user_points} | "
                    f"Computer points: {comp_points}, {winner} wins"
                    f" ({user_score}  |  {comp_score})")

    game_history.append((game_results))

    print("*** Game Update***")
    print(f"User Score: {user_score}  |  Computer Score {comp_score}")

# end of the game, output the final results
print()


make_statement("Game Over", "🏁")

print()
if user_score > comp_score:
    make_statement("The user won", "👍")
else:
    make_statement("The computer won", "👍")

print()
print()
print()


print("Game History")

make_statement("Game History", "🎲")

for item in game_history:
    print(item)
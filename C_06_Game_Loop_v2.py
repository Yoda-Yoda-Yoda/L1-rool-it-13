# at the start of the game. the computer / user score are both 0
comp_score = 0
user_score = 0

game_goal = int(input("Game Goal"))

while comp_score < game_goal and user_score < game_goal:
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round"))

    comp_score += comp_points
    user_score += user_points

    print("*** Game Update***")
    print(f"User Score: {user_score}  |  Computer Score {comp_score}")


print()
if user_score > comp_score:
    print("The user won!!!")
else:
    print("The computer won")
right_count = 0                                             
left_count = 0

def scene(mood):
    return (                                                              "You are in the Lost Forest\n"
        "****************************************\n"
        "*        ***           ******           *\n"                     f"*          {mood:<10}                *\n"                       "****************************************\n"
        "****************************************\n"
        "Go left or right? "                                          )
                                                                  mood = ":)"                                                       choice = input(scene(mood)).strip().lower()                                                                                         while True:                                                           if choice == "right":
        right_count += 1                                                  if right_count == 1:
            mood = ":|"                                                   elif right_count == 2:                                                mood = ":("
        elif right_count == 3:
            mood = "(╯°□°）╯︵ ┻━┻"
            print("Relax bro, that table had a family.\n")                else:
            mood = "💀"
            print("You're basically wandering out of spite now.\n"
)

    elif choice == "left":
        left_count += 1
        if left_count == 1:
            mood = ":)"
        elif left_count == 2:
            mood = ":D"
        else:
            print("\nYou found a path bathed in sunlight. You’re o
ut of the forest. ✨\n\\o/")
            break

    else:
        print("\nYou mumbled some nonsense and a tree judged you.
Try again.\n")

    if right_count >= 4:
        print("\nYou flipped too many tables and angered the fores
t spirits.\nA squirrel banishes you.\nGame over.\n")
        break

    choice = input(scene(mood)).strip().lower()

print("Thanks for playing.")

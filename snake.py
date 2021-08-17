import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
print("\033[1;37;40m\n")
print(" \n\t\t\t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")
# making the game in while
while no_of_chance < chance:
    print('Choose snake, water or gun:')
    _input = input()
    _random = random.choice(lst)

    if _input == _random:
        print("\033[1;31;40m\n")
        print("Tie,Both points are 0")
    
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("\033[1;32;40m")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print("\033[1;33;40m\n")
        print(f"your guess {_input} and computer guess is {_random} ")
        print("You win 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("\033[1;34;40m\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("\033[1;31;40m\n")
        print("You win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"you guess {_input} and computer guess is {_random} \n")
        print("\033[1;32;40m\n")
        print("You win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("\033[1;33;40m\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("\033[1;34;40m\n")
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print("\033[1;35;40m\n")
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("\033[1;35;40m\n")
print("Game over")

if computer_point==human_point:
    print("\033[1;352;40m\n")
    print("Tie")

elif computer_point > human_point:
    print("\033[1;35;40m\n")
    print("Computer wins and you loose")

else:
    print("\033[1;35;40m\n")
    print("you win and computer loose")
    print("\033[1;36;40m\n")

print(f"your point is {human_point} and computer point is {computer_point}")

  
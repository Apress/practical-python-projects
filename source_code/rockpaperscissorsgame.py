import random

while True:
    print("Enter your choice \n1. rock \n2.paper \n3.scissor\n")
    choice=int(input("user's turn.."))
    while choice>3 or choice<1:
        choice=int(input("enter valid number"))
    if choice==1:
        choice_name="rock"
    elif choice==2:
        choice_name="paper"
    else:
        choice_name="scissor"

    print("user choice:",choice_name)
    print("computer's turn now")

    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name="rock"
    elif comp_choice==2:
        comp_choice_name="paper"
    else:
        comp_choice_name="scissor"

    print("computer choice is"+comp_choice_name)
    print(choice_name+"V/S"+comp_choice_name)

    if((choice==1 and comp_choice==2) or (choice==2 and comp_choice==1)):
        print("paper wins")
        result="paper"

    elif((choice==1 and comp_choice==3) or (choice==3 and comp_choice==1)):
        print("rock wins")
        result="rock"

    elif((choice==1 and comp_choice==1) or (choice==2 and comp_choice==2) or (choice==3 and comp_choice==3)):
        print("Game draw")
        result="Draw"
    else:
        print("scissor wins")
        result="scissor"

    if result=="Draw":
        print("game draw")
    if result==choice_name:
        print("user wins")
    if result==comp_choice_name:
        print("computer wins")

    print("do you want to play again? (Y/N)")
    ans=input()

    if ans=='n' or ans=='N':
        break
print("thanks for playing..")













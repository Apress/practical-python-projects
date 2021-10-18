import random
print("guess the number")

number=random.randint(1,10)
#computer will select a number between 1 and 10

chances=0
print("please guess a number between 1 and 10")

while(chances<5):
    guess=int(input())
    if guess==number:
        print("user won")
        break

    elif guess<number:
        print("your guess is low and please select a higher number",guess)

    else:
        print("your guess is high and please select a lower number",guess)

    chances+=1

if not chances<5:
    print("You lose,the number is",number)

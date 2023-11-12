import random

random_num = random.randint(1,10)
guess = ""
guess_count = 5

while (guess != random_num) and (guess_count >= 1):
    guess = int(input("Enter a number: "))
    guess_count -= 1
    if guess != random_num:
        print("Incorrect guess. You have "+str(guess_count)+" attemps left.")

if guess_count > 0:
    print("You win. The correct number is, "+str(random_num))
else:
    print("You lose. The correct number was, "+str(random_num))
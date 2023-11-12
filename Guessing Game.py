
secret_word = "cake"
guess = ""
guess_count = 5

while (guess != secret_word) and (guess_count >= 1):
    guess = input("Enter a guess: ")
    guess_count -= 1
    if guess != secret_word:
        print("Incorrect guess. You have "+str(guess_count)+" attempts left.")

if guess_count > 0:
    print("You win. The secret word was, "+secret_word)
else:
    print("You lose")

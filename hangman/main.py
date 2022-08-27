
from random import choice
score = 6
word_list = ["google", "github", "stackoverflow"]
word = choice(word_list)
word_length = len(word)


dash = []
for x in range(word_length):
    dash += "_"


def replace(dash_replaced):
    for position in range(word_length):
        if user_guess == word[position]:
            dash_replaced[position] = user_guess
    return ''.join(dash_replaced)


guess_again = True
while guess_again:
    print("hint: " + word)
    user_guess = input("Guess a letter: ")
    display = replace(dash)
    print(display)
    if user_guess not in word:
        score -= 1
        print(f"Life: {score}")
        print(f"You guessed {user_guess}, that is not in the word, you lose a life.")
        if score == 0:
            guess_again = False



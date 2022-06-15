from ast import Not
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Start Hangman
print(logo)
game_is_finished = False
lives = len(stages) - 1

# generate random word from list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# create array for displaying revealed word
display = []
for _ in range(word_length):
    display += "_"

while game_is_finished == False:
    # take user input
    guess = input("Guess a letter: ").lower()

    # check if letter already guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # iterate each letter of the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        # if letter matches guess, reveal the letter in the corresponding position
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # if letter is not in the word, subtract one life
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # if lives is zero, user loses
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    # if all blanks filled, user wins
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
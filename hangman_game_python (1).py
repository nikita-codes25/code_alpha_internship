import random

# Task 1: Hangman Game
# CodeAlpha Python Programming Internship

# Small list of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 35)
print("        HANGMAN GAME")
print("=" * 35)
print("Guess the word one letter at a time.")
print(f"You can make {max_wrong_guesses} incorrect guesses.\n")

while wrong_guesses < max_wrong_guesses:
    # Display the current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the whole word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! 🎉 You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess! ✅\n")
    else:
        wrong_guesses += 1
        print("Incorrect guess! ❌\n")

else:
    print("Game Over! 😔")
    print("The correct word was:", word)

print("\nThank you for playing!")

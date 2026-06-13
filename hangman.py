import random

# List of predefined words
words = ["python", "laptop", "college", "engineer", "network"]

# Select random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while attempts > 0:

    display_word = ""

    # Create display word
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", attempts)

else:
    print("\n💀 Game Over!")
    print("The word was:", word)
    
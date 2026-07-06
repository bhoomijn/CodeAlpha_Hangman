import random

# Word list
words = ["apple", "banana", "orange", "grapes", "mango"]

# Random word select
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")
print("Word:", " ".join(guessed))

# Game loop
while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct:", " ".join(guessed))
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

# Result
if "_" not in guessed:
    print("🎉 You Win! The word was:", word)
else:
    print("❌ Game Over! The word was:", word)

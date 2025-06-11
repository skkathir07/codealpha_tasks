import random

# List of predefined words
words = ["apple", "python", "code", "alpha", "intern"]
word = random.choice(words)

guessed = ['_'] * len(word)
attempts = 6
used_letters = []

while attempts > 0 and '_' in guessed:
    print("Word:", ' '.join(guessed))
    print("Used letters:", ', '.join(used_letters))
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("Already guessed!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

if '_' not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("You lost! The word was:", word)

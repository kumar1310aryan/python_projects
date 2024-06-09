

def hangman():
    words = ["python", "programming", "hangman", "computer", "code"]
    word = random.choice(words)
    guessed = "_" * len(word)
    tries = 6
    guessed_letters = []

    print("Let's play Hangman!")
    print(guessed)

    while tries > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            guessed = "".join([char if char in guessed_letters else "_" for char in word])
            print(guessed)
        else:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")
    if "_" not in guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Out of tries! The word was {word}.")

if __name__ == "__main__":
    hangman()

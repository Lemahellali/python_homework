def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        result = ""

        for char in secret_word:
            if char in guesses:
                result += char
            else:
                result += "_"

        print(result)

        if "_" not in result:
            return True
        else:
            return False

    return hangman_closure



secret = input("Enter secret word: ")

game = make_hangman(secret)

finished = False

while not finished:
    guess = input("Guess a letter: ")
    finished = game(guess)

print("You guessed the word!")
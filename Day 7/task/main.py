import random
from hangman_const import word_list, HANGMANPICS

chosen_word = random.choice(word_list)
print(chosen_word)
length_of_word = len(chosen_word)

blank_word_list = ["_"] * length_of_word
blank_word = "".join(blank_word_list)
print(blank_word)
no_of_chances = 7
final_word = ""
count = 0
game_over = False
guessed_letter = []

while not game_over:
    if final_word == chosen_word:
        game_over = True
        print("**************************************************")
        print("Congratulations You Won!!!")
        break
    else:
        if no_of_chances > 0:
            print("**********************************************")
            guess = input("Enter a letter: ").lower()
            if guess in guessed_letter:
                print("You already guessed this letter")

            if guess in chosen_word:  # Check if the guessed letter is in the word
                for i in range(length_of_word):
                    if chosen_word[i] == guess:
                        blank_word_list[i] = guess
                        guessed_letter.append(guess)
                        print(HANGMANPICS[count])
            else:
                print(f"you guessed {guess} it is not in word..")
                no_of_chances -= 1  # Decrease chances only for incorrect guesses
                print(HANGMANPICS[count])
                count += 1

            print(f"You have {no_of_chances} chances left.")
            final_word = "".join(blank_word_list)
            print(final_word)
        else:
            print("You Lost")
            game_over = True
            break

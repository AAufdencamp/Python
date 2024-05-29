#Step 5
#we need to import modules to use external files hangman_art.py and hangman_words.py
#ref https://www.askpython.com/python/python-import-statement
import random
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

# alternatively import: hangman_words then you have to call hangman_words.word_list every time 
#the from hangman_words import word_list names the alias word_list inside the import statement; to access the variable word_list, you have to use the alias name instead of the module name hangmans_words.word_list
# import hangman_words 
# chosen_word = random.choice(hangman_words.word_list)
# word_length = len(chosen_word)

from replit import clear #so we can clear the Console when we want

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear() #after every guess we clear the Console to make room for new output
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter      
               
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    #alternatively if we call more than one module we can import them both in the same statement
    # as: from hangman_art import logo, stages
    from hangman_art import stages
    print(stages[lives])
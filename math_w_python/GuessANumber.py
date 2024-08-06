#exercise from MathWPython
# guess a number!
# write code to generate a random integer and then input user guesses of that integer.
# The code should tell the user to guess higher or lower until they get the right answer.


from IPython.display import display, Math
#from numpy import random
import random


def randomint():
    return random.randint(1,100)

def guessTheNumber():
    
    mysterynum = randomint()
    
    display(Math('%g'%(mysterynum)))
    display(Math('\\text{Guess a number between %g and %g:}'%(1,100)))
    
    which = int(input(' '))  #our function switch
    
    while mysterynum != which:
        if which < mysterynum:
            display(Math('\\text{Guess higher!}'))
            display(Math('\\text{Guess again}'))
            which = int(input(' '))
        elif which > mysterynum:
            display(Math('\\text{Guess lower!}'))
            display(Math('\\text{Guess again}'))
            which = int(input(' '))
       
    display(Math('\\text{Got it! The right numbers was %g and your final guess was %g}' %(mysterynum, which)))

guessTheNumber()
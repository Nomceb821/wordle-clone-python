import random

#create a function that will welcome the user to the game

def welcome():
    print("Welcome to Worlde")
    print("You have five chance to guess the word of the day")
    print("Please have fun!!!!")
welcome()

#Create the list of words


terms = ['stars','blues', 'green', 'saved', 'fault', 'books', 'likes', 'paper'
         'loves', 'death', 'peace', 'tutor', 'plant', 'crisp','mouse', 'techs'
         'shine', 'grave', 'brave', 'track','glass', 'sugar', 'blend', 'Truck',
         'quaff', 'zebra', 'knack', 'plumb', 'whelp','askew', 'loath', 'surly',
         'tacit', 'vexed']

#Function for the word of the day

def todays_word(terms):
    return random.choice(terms)                          # choosing random name on the list

hidden_word = todays_word(terms).upper()                        #Assigning the result to a variable


def wordle():
    attempt = 5
    i = 1
    guessed = False 

    while i < attempt:
        guess_word = input("Please guess a word: ").upper()

        if len(guess_word) != 5:
            print("Invalid. Please enter exactly five letters")
            continue

        if guess_word == hidden_word:
            print(f"You've guessed correctly in {i} attempt(s)!")
            guessed = True
            break
        else:
            todays_word = [""]*5          #Used to create a list with a length of 5
            hidden_letters = list(hidden_word)     # make a mutable copy

            #Pass 1 : check for the correct letters in correct place
            for j in range(len(guess_word)):
                if guess_word[j] == hidden_word[j]:
                    todays_word[j]= "#"           # for example if the first letter is correct ["#", "","", "", ""] 
                    hidden_letters[j] = None     # mark as used e.g if the first letter is correct[None, "d", "c", "n", "a"]
                    
            #Pass 2 : check for the correct letters in wrong place
            for j in range(len(guess_word)):
                if todays_word[j] == "":  # checks if the string is empty
                     if guess_word[j] in hidden_letters:
                         todays_word[j] = "@"            # For example ["#", "@", "@", "", ""]
                         # remove first occurrence of that letter
                         hidden_letters[hidden_letters.index(guess_word[j])] = None # [None,None, None, "n", "a"] 
                     else:
                        todays_word[j] = "-"  # Should be something like ["#", "@", "@", "-", "-"]
                        
            print("".join(todays_word))   # Output: "#@@--"
        i += 1

    if not guessed:
        print(f"You lose! The word was {hidden_word}")
wordle()




import random

def load_word() -> str:
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word: str, letters_guessed: list) -> bool:
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word: str, letters_guessed: list) -> str:
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word


def is_guess_in_word(guess: str, secret_word: str) -> bool:
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    return True if guess in secret_word else False


def snowman(secret_word: str):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    guesses = len(secret_word)
    print(f'Welcome to Snowman!\nThe Secret word contains: {len(secret_word)} letters')
    print(f'You have {str(guesses)} incorrect guesses before your guesses run out! Please enter ONE letter per round!')
    print('----------------------------------------------')
    guessed_letters = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_guess = input('Enter a letter: ')
    while True:
        if len(letter_guess) > 1:
            print('Please only enter ONE letter at a time.')
            letter_guess = input('Enter a letter: ')
            continue
        elif letter_guess in guessed_letters:
            print('You have already guessed that letter! Try again')
            letter_guess = input('Enter a letter: ')
            continue
        if is_guess_in_word(letter_guess, secret_word):
            guessed_letters.append(letter_guess)
            letters = letters.replace(letter_guess, '')
            print('Your guess appears in the word!')
        else:
            guessed_letters.append(letter_guess)
            letters = letters.replace(letter_guess, '')
            guesses -= 1
            if guesses == 0:
                print('Sorry you did not win, try again')
                print(f'The word was: {secret_word}')
                break
            print('Sorry your guess was not in the word, try again')
            print(f'You have {str(guesses)} incorrect guesses left')

        word_so_far = get_guessed_word(secret_word, guessed_letters)
        print(f'Guessed so far: {word_so_far}')
        print(f'These letters have not been guessed yet: {letters}')
        if is_word_guessed(secret_word, guessed_letters):
            print('You won!!!!')
            break
        else:
            print('----------------------------------------------')
            letter_guess = input('Enter a letter: ')



#These function calls that will start the game
secret_word = load_word()
snowman(secret_word)

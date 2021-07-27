from os import system, name
import random

GAME_OVER = 6
PATH_FILE = './files/data.txt'
BOARD = (
    """
     +---+
     |   |
     |   
     |
     |
     |
     |
    ===
    """,
    """
     +---+
     |   |
     |   0
     |
     |
     |
     |
    ===
    """,
    """
     +---+
     |   |
     |   0
     |   |
     |   |
     |
     |
    ===
    """,
    """
     +---+
     |   |
     |   0
     |  /|
     |   |
     |
     |
    ===
    """,
    """
     +---+
     |   |
     |   0
     |  /|\\
     |   |
     |
     |
    ===
    """,
    """
     +---+
     |   |
     |   0
     |  /|\\
     |   |
     |  /
     |
    ===
    """,
    """
     +---+
     |   |
     |   X
     |  /|\\
     |   |
     |  / \\
     |
    ===
    """
)


def getListWords():
    words = []
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        for word in f:
            words.append(word)

    return words


def getRandomWord(words):
    value = random.randint(1, len(words))

    return words[value][:-1]


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def generateHiddenWord(word):
    return list(map(lambda w: '-' ,word))


def showImage(fails):
    print(BOARD[fails])


def updateHiddenWord(letter,hidden_word,word,fails,list_letter):
    index = 0
    updateLetter = list(filter(lambda w: w==letter,word))
    if len(updateLetter)>0:
        for ltter in word:
            if ltter == letter:
                hidden_word[index] = letter   
            index+=1 
    else:
        fails+=1

    list_letter.append(letter)
    return fails


def showBoard(fails,letters):

    print("*"*20, " HANGMAN GAME ", "*"*20)
    showImage(fails)
    print("Fails: ",fails)
    print('Used letters: ', letters)



def isWinner(hidden_word):
    return '-' in hidden_word


def endGame(word,fails):
    if fails >= GAME_OVER:
        print('Do you lost, the word was:', word)
    else:
        print("congratz, you are winner, the word is: ", word)


def run():
    fails = 0;
    game = True
    words = getListWords()
    word = getRandomWord(words)
    hidden_word = generateHiddenWord(word)
    list_letter = []
    
    while game==True and fails<GAME_OVER:
        
        showBoard(fails,list_letter)
        print(hidden_word)
        try:
            letter = input('Enter a letter: ')
            clear()
            if letter.isnumeric():
                raise ValueError('You must enter a letter')
            elif letter in list_letter:
                raise ValueError('The letter has already been entered')
            else:    
                fails = updateHiddenWord(letter,hidden_word,word,fails, list_letter)
                game = isWinner(hidden_word)
        except ValueError as ve:
            print(ve)
    clear()
    showBoard(fails,list_letter)
    endGame(word,fails)
    



if __name__ == '__main__':
    run()
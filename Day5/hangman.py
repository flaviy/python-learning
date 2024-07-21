from random import choice, shuffle


def get_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'php', 'ruby', 'c', 'swift', 'go', 'r', 'rust',
             'scala', 'perl', 'lua', 'typescript', 'html', 'css', 'sql', 'bash', 'powershell', 'objective-c', 'matlab',
             'groovy', 'fortran', 'cobol', 'ada', 'dart', 'erlang', 'elixir', 'haskell', 'julia', 'kotlin', 'lisp',
             'pascal', 'prolog', 'smalltalk', 'scheme', 'tcl', 'verilog', 'vhdl', 'vba', 'vbscript', 'abap', 'apex',
             'awk', 'brain']
    return choice(words)


def show_dashes(word):
    return ['_' for _ in word]


def enter_letter():
    letter = input('Enter a letter: ')
    if not letter.isalpha() or len(letter) != 1:
        print('Please enter a single letter')
        return enter_letter()
    return letter


def play_hangman():
    word = get_word()
    dashes = show_dashes(word)
    print(' '.join(dashes))
    entered_letters = []
    attempts = 0
    while attempts < 6:
        letter = enter_letter()
        if letter in entered_letters:
            print('You already entered this letter')
            continue
        entered_letters.append(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    dashes[i] = letter
            print(' '.join(dashes))
            if '_' not in dashes:
                print('You won!')
                break
        else:
            attempts += 1
            print('No such letter in the word')
            print(f'Attempts left: {6 - attempts}')
    else:
        print('You lost!')
        print(f'The word was: {word}')
    print(word)


play_hangman()

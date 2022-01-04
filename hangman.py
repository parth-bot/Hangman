from stuff import *

attempts = 0
hangman = [' '] * 25
hangman_dead = [' '] * 25
hangman_dead[2] = '|'
hangman_dead[7] = 'O'
hangman_dead[12] = '|'
hangman_dead[16] = '|'
hangman_dead[18] = '|'
hangman_dead[11] = '|'
hangman_dead[13] = '|'

def display(l):
    result = ''
    count = 0
    for s in l:
        result += s
        count += 1
        if count == 5:
            count = 0
            result += '\n'
    return result

def main():
    clear()
    dialogue(f'HANGMAN!\n\n{display(hangman_dead)}(Press enter to continue)')
    while True:
        while True:
            word = dialogue('Enter word: ').lower()
            if len(word) < 3:
                print('error: word must have 3 or more letters')
            elif not word.isalpha():
                print('error: word must contain only letters')
            else:
                break
        attempts = 0
        hangman = [' '] * 25
        guessed_letters = []
        word_frame = ['- '] * len(word)
        while True:
            if attempts == 0:
                hangman[2] = '|'
            elif attempts == 1:
                hangman[7] = 'O'
            elif attempts == 2:
                hangman[12] = '|'
            elif attempts == 3:
                hangman[16] = '/'
            elif attempts == 4:
                hangman[18] = '\\'
            elif attempts == 5:
                hangman[11] = '/'
            elif attempts == 6:
                hangman[13] = '\\'
            elif attempts == 7:
                win = False
                break
            word_frame_display = ''
            for l in word_frame:
                word_frame_display += l
            if word_frame_display.replace(' ', '') == word:
                win = True
                break
            print(word_frame_display)
            print(f'Guessed Letters: {guessed_letters}\n')
            print(display(hangman))
            guess = dialogue('Guess a letter: ')
            if not guess.isalpha():
                print('error: not a letter')
                continue
            elif len(guess) > 1:
                print('error: one letter at a time')
                continue
            elif guess in guessed_letters:
                print('error: letter already guessed')
            elif guess in word:
                index = 0
                for l in word:
                    if guess == l:
                        word_frame[index] = f'{l} '
                    index +=1
                guessed_letters.append(guess)
            else:
                attempts += 1
                guessed_letters.append(guess)

        if win:
            print(f'You guessed the word with {attempts} failed guesses!\n{word}\n{display(hangman)}')
            if dialogue('Play again? ').lower() == 'no':
                break
        else:
            print(f'You lost...\nThe word was {word}\n{display(hangman_dead)}')
            if dialogue('Play again? ').lower() == 'no':
                break
if __name__ == '__main__': 
    main()

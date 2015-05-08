import random
import re
import sys
# read in the file contents
def read_file_content( file_path ):
    '''return all lines in the file as list, if file not found, return None'''
    file_words = ''
    try:
        with open(file_path) as file_content:
            return file_content.readlines(100)
    except FileNotFoundError:
        return None

def get_word_list_from_file(list_of_lists):
    words = []
    for word in list_of_lists:
        words.extend(word.lower().strip().rsplit(','))
    return words

def open_file(file_path):
    pass

def read_file_data():
    pass

def get_easy_words(word_list):

    easy_words = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_words.extend(word.lower().rsplit(','))
    return easy_words

def get_medium_words(word_list):
    medium_words = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_words.extend(word.lower().rsplit(','))
    return medium_words

def get_hard_words(word_list):
    hard_words = []
    for word in word_list:
        if len(word) >= 8:
            hard_words.extend(word.lower().rsplit(','))
    return hard_words

def pick_random_word(word_list):
    index = random.choice(range(len(word_list)))
    return word_list[index]

def display_word(word, char_list = []):
    string = []
    index = 0
    if len(char_list) == 0:
        #print('_ '*len(word))
        return ' '.join(['_']*len(word))
    else:
        for char in word:
            if char in char_list:
                string.extend(char.upper().split(','))
            else:
                string.extend('_')
            index += 1
        #print(' '.join(string).strip())
        return ' '.join(string).strip()

def is_word_complete(word, char_list = []):
    #word = list(word)
    for char in char_list:
        #for wchar in word:
        word = re.sub(re.escape(char),'',word)
            #if char == wchar:

                #word.remove(wchar)

    if len(word) == 0:
        return True
    else:
        print("Used: {}".format(char_list))
        print("You still have {}".format(word))
        return False

def get_level(word_list):
    """Return the difficulty level"""
    print("Please Select the Difficulty Level\n \
    1 - Easy (Words between 4 and 6 characters)\n \
    2 - Medium (words up to 8 characters)\n \
    3 - Hard (Words longer than 8 characters)")

    user_level_choice = int(input("Please select the level of difficulty: "))
    if user_level_choice == 1:
        return get_easy_words(word_list)
    elif user_level_choice == 2:
        return get_medium_words(word_list)
    elif user_level_choice == 3:
        return get_hard_words(word_list)

def get_user_guess():
    return input("Guess a character: ")


def game_continue():
    user_choice = input("Do you want to continue? Y/N ").lower()
    if user_choice == 'y':
        return user_choice
    else:
        print("You are supposed to type Y/y to continue")
        sys.exit()

def play(word_list):
    print("Welcome to Hangman!!!")
    print("You can quit the game anytime by typing EXIT")
    user_choice = game_continue()
    if user_choice == 'y':
        print("Please Select the Difficulty Level\n \
        1 - Easy (Words between 4 and 6 characters)\n \
        2 - Medium (words up to 8 characters)\n \
        3 - Hard (Words longer than 8 characters)")

        user_level_choice = int(input("Please select the level of difficulty: "))
        while user_level_choice not in [1, 2, 3]:
            user_level_choice = int(input("Please select the level of difficulty: "))
        if user_level_choice == 1:
            words = get_easy_words(word_list)
        elif user_level_choice == 2:
            words = get_medium_words(word_list)
        elif user_level_choice == 3:
            words = get_hard_words(word_list)

    elif user_choice == 'n' or user_choice == 'exit':
        sys.exit()
    picked_word = pick_random_word(words)
    print("Picked {}".format(picked_word))

    guess = get_user_guess()
    if guess != 'exit':
        print("guess is not exit")
        guessed_characters = []
        wrong_guess_counts = 0
        wrong_guess = []
        counter = 0
        while counter < len(picked_word.strip()):
            if guess not in picked_word:
                if guess in wrong_guess:
                    print("You already guessed this and it was not there!")
                    guess = get_user_guess()
                else:
                    print("You lost! ".format(guess))
                    wrong_guess_counts += 1
                    if wrong_guess_counts < 8:
                        pass
                    else:
                        print("You lost this round.")
                        user_choice = game_continue()
                    wrong_guess.extend(guess.split(','))
                    guess = get_user_guess()
            else:
                print("Correct guess")
                guessed_characters.extend(guess.split(','))
                print(guessed_characters)
                display = display_word(picked_word.strip(), guessed_characters)
                built_string = re.sub(r'[^A-Za-z]','',display)
                counter = len(built_string)
                print("Built word is now {} chars long".format(counter))
                print(display)
                if is_word_complete(picked_word.strip(), guessed_characters):
                    print("Whoa! You skinned it!")
                    user_choice = game_continue()
                else:
                    guess = get_user_guess()

    else:
        sys.exit

if __name__ == '__main__':
    file_words = read_file_content('/usr/share/dict/words')
    play(file_words)

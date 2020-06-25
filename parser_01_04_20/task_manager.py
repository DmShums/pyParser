import time
from web_driver import driver
from file_manager import write_to_file, is_translated, delete_word_from_file, edit_word, clear_file, read_file, gen_read_file


def add_new_word():
    while True:
        word = input('Please enter a word to translate\n')
        if word == 'mm':
            break
        if not is_translated(word):
            url = f'https://translate.google.com.ua/#view=home&op=translate&sl=uk&tl=en&text={word}'
            driver.get(url)
            element = driver.find_element_by_class_name("tlid-translation").find_element_by_tag_name('span')
            print(element.text)
            write_to_file(word, element.text)
            time.sleep(3)
            driver.refresh()
        else:
            print(f'Word {word} has already translated')

def delete_word():
    while True:
        word = input('Please enter a word to delete\n')
        if word == 'mm':
            break
        if is_translated(word):
            delete_word_from_file(word)
        else:
            print(f'Word {word} does not exist in file')

def edit():
    while True:
        word = input('Please enter a word to edit\n')
        if word == 'mm':
            break
        translation = input('Please enter a new translation of the word\n')
        if is_translated(word):
            edit_word(word, translation)
        else:
            print(f'Word {word} does not exist in file')

def clear():
    word = input('Please input YES if you want to clear the file or NO to return in main menu\n')
    if word.lower() == 'yes':
        clear_file()
        print('File has been cleared')
    else:
        print('File clearing is canceled')

def show():
    lines = read_file()
    for line in lines:
        print(line)

def show_lines():
    number = int(input('Please input number of lines to show\n'))
    start = 0
    lines = gen_read_file(start, number)
    for line in lines:
        print(line)
    while True:
        word = input('Please input NEXT or PREVIOUS or MM\n')
        if word == 'mm':
            break
        elif word.lower() == 'next':
            start += number
            lines = gen_read_file(start, number + start)
        elif word.lower() == 'previous':
            start -= number
            if start < 0:
                print("It's start")
                continue
            lines = gen_read_file(start, number + start)
        else:
            print('Try better')
            continue
        if lines:
            for line in lines:
                print(line)
        else:
            print("It's the end of file")
            break

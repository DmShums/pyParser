import os
from itertools import islice


def check_and_create_file():
    if not os.path.exists('translate.txt'):
        translate_file = open('translate.txt', 'w').close()

def write_to_file(word, translated_word='EMPTY'):
    with open('translate.txt', 'a') as translated_file:
        translated_file.write(f'{word} --- {translated_word}\n')

def is_translated(word):
    with open('translate.txt', 'r') as translated_file:
        for line in translated_file:
            if line.startswith(word):
                return True
    return False

def read_file():
    with open('translate.txt', 'r') as translated_file:
        return translated_file.readlines()

def gen_read_file(start, stop):
    with open('translate.txt', 'r') as translated_file:
        line_gen = islice(translated_file, start, stop)
        return [line for line in line_gen]

def delete_word_from_file(word):
    lines = read_file()
    with open('translate.txt', 'w') as translated_file_w:
        for line in lines:
            if not line.startswith(word):
                translated_file_w.write(line)
            else:
                print(f'Word {word} has been deleted successfully')

def edit_word(word, new_translated_word):
    lines = read_file()
    with open('translate.txt', 'w') as translated_file_w:
        for line in lines:
            if line.startswith(word):
                translated_file_w.write(f'{word} --- {new_translated_word}\n')
            else:
                translated_file_w.write(line)

def clear_file():
    open('translate.txt', 'w').close()

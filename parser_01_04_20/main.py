from file_manager import check_and_create_file
from task_manager import add_new_word, delete_word, edit, clear, show, show_lines

def main():

    check_and_create_file()
    while True:
        user_input = input('Enter the number:\n')
        try:
             user_input = int(user_input)
        except Exception:
            print('Please enter a number')
            continue
        else:
            if user_input == 0:
                break
            elif user_input == 1:
                add_new_word()
            elif user_input == 2:
                delete_word()
            elif user_input == 3:
                edit()
            elif user_input == 4:
                clear()
            elif user_input == 5:
                show()
            elif user_input == 6:
                show_lines()
            else:
                print('Please enter a valid number')
                continue

main()

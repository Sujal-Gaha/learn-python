import os
from projects.calculator import calculator_main
from projects.temp_converter import temperature_converter_main
from projects.quiz_game import quiz_game_main
from projects.snake_game import snake_game

clear = lambda: os.system('clear');

def print_line_divider():
        print("*" * 30)
        
def print_formatted_title(serial_num, project_title):
        print(f"{serial_num + 1}: {project_title}")

def exit_screen():
    user_input = input("Do you want to go to the main menu? (Y/n): ").strip().lower()

    if user_input == "" or user_input == "y":
        main_menu()
    elif user_input == "n":
        print("Exiting...")
        exit(0)
    else:
        print("Invalid input, please enter 'Y' or 'n'.")
        exit_screen()

def main_menu():
    projects = ["Calculator", "Temp Converter", "Quiz Game", "Snake Game"]

    print("List of Projects")
    print_line_divider()

    for i, project in enumerate(projects):
        print_formatted_title(i, project)
    
    print_line_divider()
        
    project_num = input("Choose a project: ").strip()

    match project_num:
        case "1":
            calculator_main()
            exit_screen()
        case "2":
            temperature_converter_main()
            exit_screen()
        case "3":
            quiz_game_main()
            exit_screen()
        case "4":
            snake_game()
            exit_screen()
        case _:
            clear()
            print("Invalid Option!!!")
            main_menu()
            
main_menu()

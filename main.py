from projects.calculator import calculator_main

def print_line_divider():
        print("*" * 30)
        
def print_formatted_title(serial_num, project_title):
        print(str(serial_num + 1) + ": "+ str(project_title))

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
    projects = ["Calculator", "Temp Converter", "Quiz Game"]

    print("List of Projects")
    print_line_divider()

    for i, project in enumerate(projects):
        print_formatted_title(i, project)
    
    print_line_divider()
        
    project_num : int = int(input("Choose a project: ").strip())

    match project_num:
        case 1:
            calculator_main()
            exit_screen()
        case 2:
            print("Temp Converter")
        case 3:
            print("Quiz Game")
        case _:
            print("Invalid Number")
            
            
main_menu()

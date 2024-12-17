def get_inputs():
    first_num = float(input("Enter the first number: ").strip())
    second_num = float(input("Enter the second number: ").strip())
    
    return first_num, second_num

def calculator_main():
    operator = input("Enter your operator (+, -, *, /): ").strip()
    
    match operator:
        case "+":
            first_num, second_num = get_inputs()
            result = first_num + second_num
            print(f"The sum is {result}")
        case "-":
            first_num, second_num = get_inputs()
            result = first_num - second_num
            print(f"The difference is {result}")
        case "*":
            first_num, second_num = get_inputs()
            result = first_num * second_num
            print(f"The product is {result}")
        case "/":
            first_num, second_num = get_inputs()
            result = first_num / second_num
            print(f"The division is {result}")
        case _:
            print("Invalid Operator!!!")
            calculator_main()


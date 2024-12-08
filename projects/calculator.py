def get_inputs():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    
    return first_num, second_num

def calculator_main():
    operator = input("Enter your operator (+, -, *, /): ").strip()
    
    match operator:
        case "+":
            first_num, second_num = get_inputs()
            result = first_num + second_num
            print("The sum is " + str(result))
        case "-":
            first_num, second_num = get_inputs()
            result = first_num - second_num
            print("The difference is " + str(result))
        case "*":
            first_num, second_num = get_inputs()
            result = first_num * second_num
            print("The product is ", str(result))
        case "/":
            first_num, second_num = get_inputs()
            result = first_num / second_num
            print("The division is ", str(result))
        case _:
            print("Invalid Operator!!!")
            calculator_main()


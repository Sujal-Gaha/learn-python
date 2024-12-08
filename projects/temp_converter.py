def check_unit_input(unit):
    if unit not in ["c", "k", "f"]:
        print("Invaid unit entry!!!")
        return False
    return True
        
        
def get_input_unit_from_user():
    unit = input("Is your temperature in celcius, kelvin or fahrenheit? (C, K, F): ").strip().lower()
    return unit

def get_output_unit_from_user():
    unit = input("Choose the unit to convert to: (C, K, F): ").strip().lower()
    return unit

def convert_to_celcius(temp, unit):
    output_temp = 0
    
    if unit == "k":
        output_temp = temp - 273.15
    else:
        output_temp = (temp - 32) * (5 / 9)
    
    print(f"The converted temperature is {output_temp}°C")

def convert_to_kelvin(temp, unit):
    output_temp = 0
    
    if unit == "f":
        output_temp = (temp - 32) * (5 / 9) + 273.15
    else:
        output_temp = temp + 273.15
    
    print(f"The converted temperature is {output_temp}°K")
    
def convert_to_fahrenheit(temp, unit):
    output_temp = 0
    
    if unit == "c":
        output_temp = temp * (9 / 5) + 32
    else:
        output_temp = (temp - 273.15) * (9 / 5) + 32
        
    print(f"The converted temperature is {output_temp}°F")

def temperature_converter_main():
    input_temp_unit = get_input_unit_from_user()
    while not check_unit_input(input_temp_unit):
        input_temp_unit = get_input_unit_from_user()

    output_temp_unit = get_output_unit_from_user()
    
    while input_temp_unit == output_temp_unit:
        print("Please select a different unit to convert to.")
        output_temp_unit = get_output_unit_from_user()
    
    while not check_unit_input(output_temp_unit):
        output_temp_unit = get_output_unit_from_user()

    temperature = float(input("Enter your temperature: "))
            
    match output_temp_unit:
        case "c":
            convert_to_celcius(temperature, output_temp_unit)
        case "k":
            convert_to_kelvin(temperature, output_temp_unit)
        case "f":
            convert_to_fahrenheit(temperature, output_temp_unit)
        case _:
            print("Invalid Entry!!!")
            temperature_converter_main()
    

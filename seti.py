binary = []
def decimal_to_binary_activted():
    user_input = int(input("Please provide a number to convert: "))
    decimal_to_binary(user_input)
    print(binary)

def decimal_to_binary(user_input):
    """Returns the array of digits in binary representation of a decimal number"""
    if user_input > 1:
        decimal_to_binary(user_input//2)
    binary.append(user_input % 2)


def binary_to_decimal_activted():
    user_input = input("Please provide a number to convert: ")
    input_numbers = []
    for i in user_input:
        if i.isdigit():
            input_numbers.append(int(i))
    result = binary_to_decimal(input_numbers)
    print(result)

def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    result = 0 
    exponent = 0
    for element in reversed(binary_digits):
        result += element*pow(2, exponent)
        exponent += 1
    return result


def decimal_to_base_activated():
    user_input = int(input("Please provide a number "))
    destination_base = int(input("Enter base: "))
    decimal_to_base(user_input, destination_base)
    print(binary)

def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    if decimal_number > (destination_base-1):
        decimal_to_base(decimal_number // destination_base, destination_base)
    binary.append(decimal_number % destination_base)


def base_to_decimal_activated():
    user_input = input("Please provide a number to convert: ")
    destination_base = int(input("Please provide a base number "))
    input_numbers = []
    for i in user_input:
        if i.isdigit():
            input_numbers.append(int(i))
    result = base_to_decimal(input_numbers, destination_base)
    print(result)

def base_to_decimal(input_numbers, destination_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    result = 0 
    exponent = 0
    for element in reversed(input_numbers):
        result += element*pow(destination_base, exponent)
        exponent += 1
    return result


def digits_as_string_activated():
    user_input = input("Please provide a number to convert: ")
    destination_base = int(input("Please provide a number base: "))
    max_base = 16
    if (destination_base > 16):
        raise ValueError(f"Base number cannot be greater than {max_base}")
    input_numbers = user_input.replace("[","").replace("]","").split(",")
    input_number_as_int = list(map(int,input_numbers))
    result = digits_as_string(input_number_as_int)
    print(result)

def digits_as_string(input_numbers):
    """Returns the string representation of an array of digits given in base"""
    dictionary = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    results_list = []
    for i in input_numbers:
        results_list.append(dictionary[i])
    return "".join(results_list)

def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass

digits_as_string_activated()
binary = []
def decimal_to_binary_activted():
    user_input = int(input("Please provide a number to convert: "))
    decimal_to_binary(user_input)
    print(binary)

def binary_to_decimal_activted():
    user_input = input("Please provide a number to convert: ")
    input_numbers = []
    for i in user_input:
        if i.isdigit():
            input_numbers.append(int(i))
    result = binary_to_decimal(input_numbers)
    print(result)

def decimal_to_base_activated():
    user_input = int(input("Please provide a number "))
    destination_base = int(input("Enter base: "))
    decimal_to_base(user_input, destination_base)
    print(binary)

def base_to_decimal_activated():
    user_input = input("Please provide a number to convert: ")
    destination_base = int(input("Please provide a base number "))
    input_numbers = []
    for i in user_input:
        if i.isdigit():
            input_numbers.append(int(i))
    result = base_to_decimal(input_numbers, destination_base)
    print(result)

def decimal_to_binary(user_input):
    """Returns the array of digits in binary representation of a decimal number"""
    if user_input > 1:
        decimal_to_binary(user_input//2)
    binary.append(user_input % 2)

def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    result = 0 
    exponent = 0
    for element in reversed(binary_digits):
        result += element*pow(2, exponent)
        exponent += 1
    return result

def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    if decimal_number > (destination_base-1):
        decimal_to_base(decimal_number // destination_base, destination_base)
    binary.append(decimal_number % destination_base)

def base_to_decimal(input_numbers, destination_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    result = 0 
    exponent = 0
    for element in reversed(input_numbers):
        result += element*pow(destination_base, exponent)
        exponent += 1
    return result


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass

base_to_decimal_activated()
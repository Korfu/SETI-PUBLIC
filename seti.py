binary = []
def main():
    #user_input = int(input("Please provide a number to convert:"))
    #decimal_to_binary(user_input)
    #print(binary)
    user_input = input("Please provide a number to convert: ")
    destination_base = int(input("Please provide a number base: "))
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
    result = 0 
    exponent = 0
    for element in reversed(binary_digits):
        result += element*pow(2, exponent)
        exponent += 1
    return result
    


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    result = 0 
    exponent = 0
    for element in reversed(digits):
        result += element*pow(original_base, exponent)
        exponent += 1
    return result

def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass

main()

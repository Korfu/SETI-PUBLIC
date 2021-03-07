binary = []

def decimal_to_binary(user_input):
    """Returns the array of digits in binary representation of a decimal number"""
    if user_input > 1:
        decimal_to_binary(user_input // 2)    
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


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass

def main():
    user_input = int(input("Please provide a number: "))
    destination_base = int(input("Enter base: "))    
    decimal_to_base(user_input, destination_base)
    print(binary)
    # user_input = input("Enter number: ")
    # input_numbers = []
    # for i in user_input:
    #     if i.isdigit():
    #         input_numbers.append(int(i))
    # result = binary_to_decimal(input_numbers)
    # print(result)

main()
max_base = 16
binary = []
def main():
    #user_input = int(input("Please provide a number to convert:"))
    #decimal_to_binary(user_input)
    #print(binary)
    user_input = input("Please provide a number to convert: ")
    destination_base = int(input("Please provide a number base: "))

    if (destination_base > 16):
        raise ValueError(f"Base number cannot be greater than {max_base}")
    input_numbers = user_input.replace("[","").replace("]","").split(",")
    input_number_as_int = list(map(int,input_numbers))
    result = digits_as_string(input_number_as_int, destination_base)
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
    dictionary = {0:"0", 1: "1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    result_list = []
    for i in digits:
        if i > max_base:
               raise ValueError(f"given number ({i}) cannot be greater than {max_base}")
        result_list.append(dictionary[i])
    return "".join(result_list)

def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass

main()

import sys
import string

'''
    # Initialize counters
    # Analyze each character in the input string
    # Print the results
    # Check the number of arguments provided
    # If no arguments or None is provided, prompt the user for input
    # Analyze the provided input string

'''


def analyze_string(input_string):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    punctuation_count = 0
    digit_count = 0
    space_count = 0

    # Analyze each character in the input string
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    # Print the results
    print(f"{uppercase_count} upper letters")
    print(f"{lowercase_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    # Check the number of arguments provided
    assert len(sys.argv) <= 2, "AssertionError: Too many arguments provided."

    # If no arguments or None is provided, prompt the user for input
    if len(sys.argv) == 1 or sys.argv[1] == "None":
        input_string = input("Please provide a string: ")
    else:
        input_string = sys.argv[1]

    # Analyze the provided input string
    analyze_string(input_string)


if __name__ == "__main__":
    main()

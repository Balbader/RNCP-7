import sys


def main():
    '''
    Ensure only one argument is provided
    Try to convert the argument to an integer
    Check if the number is even or odd and print the result
    '''
    assert len(sys.argv) == 2, "AssertionError: Please provide exactly one argument."

    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: Argument is not an integer.")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()

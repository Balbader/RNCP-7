from ft_filter import ft_filter
import sys


'''
    Check for the correct number of arguments
    Assign the arguments to S and N
    Ensure the first argument is a string
    Use list comprehension and a lambda to filter words
    longer than N characters
    Print the result

'''


def main():
    # Check for the correct number of arguments
    assert len(sys.argv) == 3
    "AssertionError: The program requires exactly two arguments."

    # Assign the arguments to S and N
    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("AssertionError: The second argument must be an integer.")

    # Ensure the first argument is a string
    assert isinstance(S, str)
    "AssertionError: The first argument must be a string."

    # Use list comprehension and a lambda
    # to filter words longer than N characters
    result = list(ft_filter(lambda word: len(word) > N, [word for word in S.split()]))

    # Print the result
    print(result)


if __name__ == "__main__":
    main()

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    This function takes a 2D array and two integers as
    input and returns a 2D array that is a slice of the input array.
    The slice is taken from the start index to the end index (exclusive)
    of each list in the input array.
    The input array is a list of lists, where each list represents a person
    and contains the height and weight of the person.
    '''
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print("print 1: ", slice_me(family, 0, 2))
    print("\n")
    print("print 2: ", slice_me(family, 1, -2))
    print(slice_me.__doc__)


if __name__ == "__main__":
    main()

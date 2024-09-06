def slice_me(family: list, start: int, end: int) -> list:
    '''
    This function takes a 2D array and two integers as
    input and returns a 2D array that is a slice of the input array.
    The slice is taken from the start index to the end index (exclusive)
    of each list in the input array.
    The input array is a list of lists, where each list represents a person
    and contains the height and weight of the person.
    '''
    # Check if family is a list
    if not isinstance(family, list):
        raise TypeError("family must be a list")

    # Check if all elements in family are lists
    if not all(isinstance(person, list) for person in family):
        raise TypeError("all elements in family must be lists")

    # Check if all lists in family have the same length
    if len(set(len(person) for person in family)) != 1:
        raise ValueError("all lists in family must have the same length")

    # Check if start and end are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    # Check if start and end are within the valid range
    if start < 0 or end > len(family[0]):
        raise ValueError("start must be non-negative and\
        end must be less than or equal to the\
        length of the lists in family")

    # Print the shape of the array
    print("My shape is : ", "(", len(family), ",", len(family[0]), ")")

    # Return the truncated version of the array
    return [person[start:end] for person in family]


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print("print 1: ", slice_me(family, 0, 2))
    print("\n")
    print("print 2: ", slice_me(family, 1, -2))


if __name__ == "__main__":
    main()

# NOTE: The code above needs to be refactored as the output is not as expected.

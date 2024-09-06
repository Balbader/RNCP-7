def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''
    give_bmi.doc

    This module contains functions that calculate the BMI of a person and
    checks if the BMI is greater than a certain limit.

    . The function is defined using the def keyword, followed by the name
    of the function (give_bmi), the arguments it takes (height and weight),
    and the type hints for those arguments (list[int | float]).
    The type hints indicate that the height and weight arguments
    should be lists of numbers (either integers or floats).

    . The function uses a list comprehension to calculate the BMI values.
    The zip function is used to iterate over the height and weight lists
    simultaneously. For each pair of height and weight values,
    the BMI is calculated by dividing the weight by the height squared.

    . The calculated BMI values are returned as a list.
    '''
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    apply_limit.doc

    This function takes a list of BMI values and a limit value as arguments
    and returns a list of boolean values indicating whether each BMI values
    is greater than the limit.
    '''
    return [b > limit for b in bmi]


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == '__main__':
    main()

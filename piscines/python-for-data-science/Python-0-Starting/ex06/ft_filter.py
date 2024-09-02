def ft_filter(function, iterable):
    '''
    ft_filter(function or None, iterable) --> ft_filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    '''
    # If function is None, filter out all falsy values
    if function is None:
        function = bool

    # Use list comprehension to filter elements based on the function's result
    return [item for item in iterable if function(item)]

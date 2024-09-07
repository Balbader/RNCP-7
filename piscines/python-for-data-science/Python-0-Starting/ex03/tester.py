from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)

# ! Can't pass a string to NULL_not_found and get type not found
# print(NULL_not_found("Brian"))
print(NULL_not_found({}))

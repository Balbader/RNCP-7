def NULL_not_found(object: any) -> int:
	if isinstance(object, type(None)):
		print("Nothing: None ", type(object))
	elif isinstance(object, float):
		print("Cheese: nan", type(object))
	elif isinstance(object, str):
		print("Empty: ", type(object))
	elif isinstance(object, bool):
		print("Fake: False ", type(object))
	elif isinstance(object, int):
		print("Zero: 0", type(object))
	else:
		print("Type not found")
	return 1

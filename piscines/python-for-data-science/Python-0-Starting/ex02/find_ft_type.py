def all_thing_is_obj(object: any) -> int:
	if isinstance(object, list):
		print("List : ", type(object))
	elif isinstance(object, tuple):
		print("Tulpe : ", type(object))
	elif isinstance(object, set):
		print("Set : ", type(object))
	elif isinstance(object, dict):
		print("Dict : ", type(object))
	elif isinstance(object, str):
		print(f"{object} is in the kitchen")
	else:
		print("Type not found")
	return 42

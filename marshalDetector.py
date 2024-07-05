if (__name__ == '__main__'):
	raise SyntaxError("this tool must import, not run as main file (using: import marshalDetector)")

print(">>>>>> Marshal Detector <<<<<<")
print(">> Author:  KhanhNguyen9872 <<")

err = []
push = err.append

import marshal

# library
obj = marshal

if not (str(obj) == "<module 'marshal' (built-in)>"):
	push("marshal: module is not <built-in>")
else:
	if not (obj.__loader__ == __import__('sys').__loader__):
		push("marshal: module is not <built-in>")

if not ((str(type(obj)) == "<class 'module'>") and (type(obj) == obj.__class__)):
	push("marshal: not a module object")

try:
	if not (str(obj.__name__) == "marshal"):
		push("marshal: wrong __name__")
except Exception as e:
	push("marshal: __name__ not found")

try:
	if not (str(obj.__doc__) == 'This module contains functions that can read and write Python values in\na binary format. The format is specific to Python, but independent of\nmachine architecture issues.\n\nNot all Python object types are supported; in general, only objects\nwhose value is independent from a particular invocation of Python can be\nwritten and read by this module. The following types are supported:\nNone, integers, floating point numbers, strings, bytes, bytearrays,\ntuples, lists, sets, dictionaries, and code objects, where it\nshould be understood that tuples, lists and dictionaries are only\nsupported as long as the values contained therein are themselves\nsupported; and recursive lists and dictionaries should not be written\n(they will cause infinite loops).\n\nVariables:\n\nversion -- indicates the format that the module uses. Version 0 is the\n    historical format, version 1 shares interned strings and version 2\n    uses a binary format for floating point numbers.\n    Version 3 shares common object references (New in version 3.4).\n\nFunctions:\n\ndump() -- write value to a file\nload() -- read value from a file\ndumps() -- marshal value as a bytes object\nloads() -- read value from a bytes-like object'):
		push("marshal: wrong __doc__")
except Exception as e:
	push("marshal: __doc__ not found")

try:
	if not (str(obj.__package__) == ""):
		push("marshal: wrong __package__")
except Exception as e:
	push("marshal: __package__ not found")

try:
	if not (type(obj.__dict__) == type({})):
		push("marshal: found __dict__ but wrong type")
except Exception as e:
	if (type(e) == AttributeError):
		push("marshal: __dict__ not found")
	else:
		push("marshal: found __dict__ but wrong Exception")

allAttr = ['__name__', '__doc__', '__package__', '__loader__', '__spec__', 'dump', 'load', 'dumps', 'loads', 'version']
for i in allAttr:
	try:
		p = getattr(obj, i)
	except Exception as e:
		push("marshal: {} not found".format(i))

try:
	if not (obj.__dir__() == allAttr):
		push("marshal: __dir__ is replaced")
except Exception as e:
	push("marshal: __dir__ not found")

try:
	if not (list(obj.__dict__) == allAttr):
		push("marshal: __dict__ abnormally")
except Exception as e:
	push("marshal: __dict__ not found")

# .loads
obj = marshal.loads

if (obj != None):
	if not (str(obj) == "<built-in function loads>"):
		push("marshal.loads: function is not <built-in>")

	try:
		if not (str(obj.__name__) == "loads"):
			push("marshal.loads: wrong __name__")
	except Exception as e:
		push("marshal.loads: __name__ not found")

	try:
		if not (str(obj.__qualname__) == "loads"):
			push("marshal.loads: wrong __qualname__")
	except Exception as e:
		push("marshal.loads: __qualname__ not found")

	try:
		if not (str(obj.__doc__) == 'Convert the bytes-like object to a value.\n\nIf no valid value is found, raise EOFError, ValueError or TypeError.  Extra\nbytes in the input are ignored.'):
			push("marshal.loads: wrong __doc__")
	except Exception as e:
		push("marshal.loads: __doc__ not found")

	try:
		if not (str(obj.__reduce_ex__(0)) == "loads"):
			push("marshal.loads: wrong __reduce_ex__")
	except Exception as e:
		if (type(e) == AttributeError):
			push("marshal.loads: __reduce_ex__ not found")
		else:
			push("marshal.loads: found __reduce_ex__ but wrong Exception")

	try:
		if not ("<built-in method __reduce__ of builtin_function_or_method object at " in str(obj.__reduce__)):
			push("marshal.loads: __reduce__ is replaced")
		else:
			if not (str(obj.__reduce__()) == "loads"):
				push("marshal.loads: wrong __reduce__")
	except Exception as e:
		push("marshal.loads: __reduce__ not found")


	try:
		if not (str(obj.__module__) == "marshal"):
			push("marshal.loads: wrong __module__")
	except Exception as e:
		push("marshal.loads: __module__ not found")

	if not ((str(type(obj)) == "<class 'builtin_function_or_method'>") and (type(obj) == obj.__class__)):
		push("marshal.loads: not a function object")

	try:
		obj.__dict__
		push("marshal.loads: found __dict__")
	except Exception as e:
		if (type(e) == AttributeError):
			if ("'builtin_function_or_method' object has no attribute '__dict__'" in str(e)):
				pass
			else:
				push("marshal.loads: not found __dict__ but wrong Exception")
		else:
			push("marshal.loads: found __dict__ but wrong Exception")

	allAttr = ['__repr__', '__hash__', '__call__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce__', '__module__', '__doc__', '__name__', '__qualname__', '__self__', '__text_signature__', '__new__', '__str__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
	for i in allAttr:
		try:
			p = getattr(obj, i)
		except Exception as e:
			push("marshal.loads: {} not found".format(i))

	try:
		if not (obj.__dir__() == allAttr):
			push("marshal.loads: __dir__ is replaced")
	except Exception as e:
		push("marshal.loads: __dir__ not found")

	try:
		obj.__globals__
		push("marshal.loads: found __globals__")
	except Exception as e:
		if (type(e) == AttributeError):
			if ("'builtin_function_or_method' object has no attribute '__globals__'" in str(e)):
				pass
			else:
				push("marshal.loads: not found __globals__ but wrong Exception")
		else:
			push("marshal.loads: found __globals__ but wrong Exception")

	try:
		p = marshal.dumps(compile("'1'", '', 'eval'))
		if not ((str(type(obj(p))) == "<class 'code'>") and (eval(obj(p)) == "1")):
			push("marshal.loads: function not working properly!")
	except Exception as e:
		push("marshal.loads: function not working properly!")

	try:
		obj(b'', b'')
		push("marshal.loads: argument is modified")
	except Exception as e:
		if (type(e) == TypeError):
			if (" takes exactly one argument " in str(e)):
				pass
			else:
				push("marshal.loads: argument is modified")
		else:
			push("marshal.loads: argument is modified")
else:
	push("marshal.loads: function is None")

# .dumps

# .load

# .dump

# result

if not err:
	print(">> Result: marshal is not modified!")
else:
	print(">> Result: marshal is modified!")
	for i in err:
		print(" - {}".format(i))

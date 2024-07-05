def a(*args):
	return __import__('marshal').b(*args)

__import__('marshal').b = __import__('marshal').loads
__import__('marshal').loads = a

import marshalDetector
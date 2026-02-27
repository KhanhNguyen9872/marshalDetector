## modify your marshal.loads here
""" // this is comment //
import marshal

original_loads = marshal.loads

def hooked_loads(data):
    print("[+] marshal.loads called")    
    result = original_loads(data)
    return result

marshal.loads = hooked_loads
"""

## let's detect it, you will get the output
import marshalDetector
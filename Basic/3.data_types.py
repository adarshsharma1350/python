# Setting the Data Types
print("\n-----Setting the Data Types-----\n")

# commonally used 
_string = "Adarsh"
_integer = 234
_float = 45.22
_complex = 10j
_boolean = True
_tuple = ("ISRO", "NASA", "ROSCOSMOS")
_list = ["Apple", 54, 44.22, 34j]
_dictionary = {"name":"Adarsh", "age":22}
_set = {"Machine Learning", "Big Data", "Data Analytics"}

# less used 
_frozenset = frozenset({"Keras", "TensorFlow", "NumPy"})
_bytes = b"Adarsh"
_range = range(8)
_bytearray = bytearray(8)
_memoryview = memoryview(bytes(8))
_nonetype = None

print(_string)
print(_integer)
print(_float)
print(_complex)
print(_boolean)
print(_tuple)
print(_list)
print(_dictionary)
print(_set)

print(_frozenset)
print(_range)
print(_bytes)
print(_bytearray)
print(_memoryview)
print(_nonetype)

# Setting the Specific Data Type
print("\n-----Setting & Getting the Specific Data Type-----\n")

String = str("Adarsh")
Integer = int(234)
Float = float(45.55)
Complex = complex(10j)
Boolean = bool(8)
Tuple = tuple(("ISRO", "NASA", "ROSCOSMOS"))
List = list(["Apple", 54, 44.22, 34j])
Dictionary = dict({"name":"Adarsh", "age":22})
Set = set({"Machine Learning", "Big Data", "Data Analytics"})
Frozenset = frozenset({"Keras", "TensorFlow", "NumPy"})
Range = range(8)
Bytes = bytes(8)
Bytearray = bytearray(8)
Memoryview = memoryview(bytes(8))

print(String, type(String))
print(Integer, type(Integer))
print(Float, type(Float))
print(Complex, type(Complex))
print(Boolean, type(Boolean))
print(Tuple, type(Tuple))
print(List, type(List))
print(Dictionary, type(Dictionary))
print(Set, type(Set))
print(Frozenset, type(Frozenset))
print(Range, type(Range))
print(Bytes, type(Bytes))
print(Bytearray, type(Bytearray))
print(Memoryview, type(Memoryview))
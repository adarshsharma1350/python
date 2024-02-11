# Numbers
print("\n-----Numbers & their data type before type conversion-----\n")
Integer = 34
Float = 34.43
Complex = 3+10j

print(Integer, type(Integer))
print(Float, type(Float))
print(Complex, type(Complex))

# Type Conversion
print("\n-----Numbers after type conversion-----\n")
Int2Float = float(Integer)
Float2Int = int(Float)
Int2Complex = complex(Integer)
Float2Complex = complex(Float)

# After type conversion 
print(Int2Float, type(Int2Float))
print(Float2Int, type(Float2Int))
print(Int2Complex, type(Int2Complex))
print(Float2Complex, type(Float2Complex))

# Random Numbers
print("\n-----It's an example of Random Numbers-----\n")

# importing the random(built-in) module
import random

random_value1, random_value2 = random.randrange(2, 33)
print(random_value1, random_value2)

# Type Casting in Python
print("\n-----Before type casting-----\n")
Cast_Integer = 12
Cast_Float = 23.23
Cast_String = "66"

print(Cast_Integer, type(Cast_Integer))
print(Cast_Float, type(Cast_Float))
print(Cast_String, type(Cast_String))

# Into Integer
print("\n-----Type casting into integer-----\n")
int2int = int(Cast_Integer)  
float2int = int(Cast_Float)
string2int = int(Cast_String)

print(int2int, type(int2int))
print(float2int, type(float2int))
print(string2int, type(string2int))

# Into Float
print("\n-----Type casting into float-----\n")
int2float = float(Cast_Integer)    
float2float = float(Cast_Float)   
string2float = float("4.2")

print(int2float, type(int2float))
print(float2float, type(float2float))
print(string2float, type(string2float))

# Into String
print("\n-----Type casting into string-----\n")
int2string = str(Cast_Integer) 
float2string = str(Cast_Float)   
string2string= str(3.0)  

print(int2string, type(int2string))
print(float2string, type(float2string))
print(string2string, type(string2string))
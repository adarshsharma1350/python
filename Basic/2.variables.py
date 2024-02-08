# Creating Variables
integer_var = 5
string_var = "ISRO"
print(integer_var)
print(string_var)

# Get the Type of variables
check_var_type1 = 32
check_var_type2 = "Adarsh"
check_var_type3 = 34.44
check_var_type4 = True

print("\n",type(check_var_type1), "\n",type(check_var_type2), "\n",type(check_var_type3), "\n",type(check_var_type4))

# Variable using Single and Double Quotes
single_quotes = 'Adarsh(single quotes)'
double_quotes = "Adarsh(double quotes)"

print(single_quotes)
print(double_quotes)

# Case-Sensitivity of variable
case_sens_var = 54
Case_sens_var = "case sensitive variable"

# Ways for create Valid variables  
myvar = MYVAR = my_var = _my_var = myVar = MYVAR = myvar2 = "ISRO"
print(myvar, my_var, _my_var, myvar2, myVar, MYVAR)

# Invalid variables
"""
2myvar = "ISRO"
my-var = "ISRO" , my var = "ISRO

"""

# Multi Words Variable Names
myVariableName = "ISRO" # Camel Case
MyVariableName = "ISRO" # Pascal Case
my_variable_name = "ISRO" # Snake Case

var1 , var2  = "Adarsh", 4 # Many Values to Multiple Variables
print(var1, var2)

Var1 = Var2 = "one to multiple variables" # One Value to multiple Variables
print(Var1, Var2)

# Unpack a Collection
unpack_list = ["one", 11]
VAR1, VAR2 = unpack_list
print(VAR1, VAR2)

# Global Variables 
# Normally
var_global = "It's a normal global variable"
def Globle(): 
    print(var_global)
Globle()

# globle keyword 
def globle():
    global glob
    glob = "It's a global variable using global keyword."
globle()
print(glob)
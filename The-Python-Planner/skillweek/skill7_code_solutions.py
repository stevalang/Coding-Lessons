def addtwo(mynum):
   result = mynum + 2
   return(result)

a = 2
addtwo(a)

# Exercise 1 Example

def firstletter(mystring):
    result = mystring[0]
    return(result)
    
a = "Hello"
firstletter(a)
firstletter("Hello")

a = 2
b = 3

def subtract(num1,num2):
   result = num1 - num2
   return(result)

subtract(a,b)
subtract(2,3)

# Exercise 2

subtract(b,a)

subtract(num1 = a, num2 = b)
subtract(num1 = b, num2 = a)

# Exercise 3

mystringdict = {}
def firstletter(mystring):
    letter1 = mystring[0]
    mystringdict[mystring] = letter1
    return(mystringdict)
    
firstletter('ThisString')

def firstletter(mystring):
   firstletter = mystring[0]
   return(firstletter)
   
firstletter('ThisString')

a = ['cat','dog','turtle']

for i in a:
   print(firstletter(i))
    
    
    

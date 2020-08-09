# If

a = 2
b = 4

if a == b:
   print(a)
   
# Exercise 1
   
if a < b:
    print(a)
    
    
if a == b:
   print(a)
else:
   print("Not equal")
   
# Exercise 2

a = 1
b = 2
c = 3

if a > b:
   a = a + b
   print(a)
else:
   print(b)
print(a)

# Elif

if a == b:
   print(a+b)
elif a < b:
   print(a)
else: 
   print(b)

# For Loops
   
a = [1,2,3,4,5,6]

for i in a:
   print(i)
   
for i in a:
   print(i + 2)
   
# Exercise 3
   
for i in a[:3]:
    print(i)
    
    
for i in a:
   if i > 2:
      print(i)

b = [4,5]

for i in a:
   if i not in b:
      print(i)
    
# Exercise 4
      
a = [1,2,3,"Hello",4,5,"Hi",6]

for i in a:
    if type(i) == str:
        print(i)
        
# Exercise 5
        
b = []
for i in a:
    if type(i) == str:
        b.append(i)
        
b
        
# Exercise 6

b = []
for i in a:
    if type(i) == str:
        b.append(i)
        a.remove(i)
        
b
a

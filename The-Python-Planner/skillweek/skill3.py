# Lists

[1,5,6,4,8]
["hi", "hello","hey"]
["hi", 5, "hello", 8,"hey"]

# Exercise 1

a = [1,5,6,4,8]

# List Operations

[1,2,3] + [4,5,6]

a = [1,2,3]
b = [4,5,6]
c = a+b
c

a+[4,5,6]

a = []
a.append("Hey")
a.append("Hi")
a

a.remove("Hey")
a

# Indexing

a = ["Hi","Hello","Hey","Howdy"]

a[0] #first element of list a
a[0:1] #index 0 through 1, not including 1
a[0:2] #index 0 through 2, not including 2
a[:2] #up to index 2, not including 2
a[1:3] #index 1 through 3, not including 3

a[-1] #last element of list a
a[-3:-1] #start at 3rd from end, not including last
a[-3:] #start at 3rd from end, including last


a = [1,2,3,8,8]
a.index(8)

# Exercise 2 Example

b = [2,4,8,8]
c = b[-2:]
c

# Nested Lists

[ [1,2,3], [4,5,6],  [7,8,9] ]

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = [a,b,c]
d

d[1]  # the same as list b 

d[1][0]

# Exercise 3

d[0][1]

#or

e = d[0]
e
f = e[1]
f


# String Indexing

a = "Hello, how are you?"
a[0]
a[0:5]

a[0:5] + a[-5:]

# Exercise 4

a = ["hi","hello","hey","howdy"]

b = a[0][:2] + a[1][:2] + a[2][:2] + a[3][:2]
b


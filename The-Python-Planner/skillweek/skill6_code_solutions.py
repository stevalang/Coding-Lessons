# Open/Close

mytxt = open("mytxtfile.txt","w")

mytxt.write("Hello.\n") 
mytxt.write("I made a new text file.")
mytxt.close()

# Exercise 1 Example

mytxt = open("mytxtfile.txt","w")
a = "This is the end of my text file."
mytxt.write(a)
mytxt.close()

mytxt.close()

mytxt = open("mynewtextfile.txt", "r") 
a = mytxt.read()
mytxt.close()
a

# Input

name = input("Enter your name: ")
print(name)

name = input("Enter your name: ")
greeting = "Welcome, " + name
print(greeting)

# Exercise 2

petnames = {'daisy' : 'cat', 'fluffy' : 'dog', 'speedy' : 'turtle'}

pet = input("Enter your pet's name: ")
pettype = petnames[pet]
print(pettype)

# Exercise 3

petnames = {'daisy' : ['cat', 1, 'gray'], 
            'fluffy' : ['dog', 5, 'black'], 
            'speedy' : ['turtle', 5, 'green']}

pet = input("Enter your pet's name: ")
pettype = petnames[pet][0]
print(pettype)

# Exercise 4 Example

pet = input("Enter your pet's name: ")
pettype = petnames[pet][0]
pettage = petnames[pet][1]
petcolor = petnames[pet][2]
sentence = "This " + petcolor + " " + pettype + " has lived for " + str(pettage) + " year(s)."
print(sentence) 

# Exerciise 5

pet = input("Enter your pet's name: ")

if pet not in petnames:
    print("Pet not in dictionary.")
else:
    pettype = petnames[pet][0]
    pettage = petnames[pet][1]
    petcolor = petnames[pet][2]
    sentence = "This " + petcolor + " " + pettype + " has lived for " + str(pettage) + " year(s)."
    print(sentence)     

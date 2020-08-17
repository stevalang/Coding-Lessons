# print(id('Howdy'))

# bacon = 'Hello'
# print(id(bacon))
# bacon += 'world!'  # A new string is made from 'Hello' and 'world!'.
# print(id(bacon))  # bacon now refers to a  completely different string.
#
eggs = ['cat', 'dog']  # This creates a new list.
print(id(eggs))
eggs.append('moose')  # append() modifies the list "in place".
print(id(eggs))  # eggs still refers to the same list as before.
eggs = ['bat', 'rat', 'cow']  # This creates a new list, which has a new identity.
print(id(eggs))
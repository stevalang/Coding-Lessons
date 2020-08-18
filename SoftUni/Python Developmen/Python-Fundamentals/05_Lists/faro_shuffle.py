"""
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]
Write a program that receives a single string (cards separated by a space) and on the second line receives a number of faro shuffles that have to be made. Print the state of the deck after the shuffle
Note: The length of the deck of cards will always be an even number
"""

deck = input().split(' ')
print(deck)
new_deck = []
new_deck[0] = deck[0]
print(new_deck[0])
shuffle_times = int(input())

mid = int(len(line)/2)


for card in deck:
    if card % 2 != 0:
        new[i] = line[i]
    if i % 2 == 0:
        new[mid + i] = line[mid + i]


print(new)

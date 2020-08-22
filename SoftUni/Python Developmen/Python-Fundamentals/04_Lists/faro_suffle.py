"""
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]
Write a program that receives a single string (cards separated by a space) and on the second line receives a number of faro shuffles that have to be made. Print the state of the deck after the shuffle
Note: The length of the deck of cards will always be an even number
"""

cards = input().split()
shuffles_count = int(input())
middle_length = len(cards) // 2
for _ in range(shuffles_count):
    result = []
    for index in range(middle_length):
        first_card = cards[index]
        current_index_second_deck = index + middle_length
        second_card = cards[current_index_second_deck]

        result.append(first_card)
        result.append(second_card)
    cards = result
print(result)

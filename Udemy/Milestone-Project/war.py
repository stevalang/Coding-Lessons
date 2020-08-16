"""
CARD
SUIT, RANK, VALUE
"""
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two": 2,'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
          'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    pass


class Player:
    pass


class GameLogic:
    pass


two_hearts = Card("Hearts", "Two")
print(two_hearts)
print(two_hearts.suit)
print(two_hearts.rank)
print(values[two_hearts.rank])

three_clubs = Card("Club", 'Three')
print(three_clubs)
print(three_clubs.suit)
print(three_clubs.rank)
print(three_clubs.value)

print(two_hearts.value == three_clubs.value)



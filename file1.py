import random

cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
deck = []
for card in cards:
    for suit in suits:
        deck.append(f'{card} of {suit}')
random.shuffle(deck)
print(deck.pop())
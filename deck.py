from card import Card
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

def new_deck():
    cards = []
    for suit in suits:
        for value in values:
            cards.append(Card(suit, value))
    return cards

class Deck:
    def __init__(self):
        self.cards = new_deck()

    def __repr__(self):
        return 'Deck of {} cards'.format(self.count())

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
	        raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def _deal(self, num):
        count = self.count()
        actual = min([num, count])
        if count == 0:
            raise ValueError
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_hand(self, num):
        return self._deal(num)

    def deal_card(self):
        return self._deal(1)[0]

deck = Deck()
deck.shuffle()
# for val in deck.cards:
    # print(val)
# print(deck.deal_card())
# print(deck.deal_hand(5))
print(deck.deal_hand(53))
# print(deck.deal_card())

# print(deck)

# card = Card()
# print(card)

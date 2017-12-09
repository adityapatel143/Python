from __future__ import print_function, division

import random


class Card:
    """Represents a standard playing card.

        Attributes:
          suit: integer 0-3     : 0 = Clusb, 1 = Diamonds, 2 = Hearts, 3 = Spades
          rank: integer 1-13
        """
    # suit_names & rank_names are 'class attribute' because it is defined inside class and outside of any method

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    # suit and rank are 'instance attributes' because they  are associated with particular instance.

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # Returns a human-readable string representation.
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    # Checks whether self and other have the same rank and suit.
    #          returns: boolean

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    # Compares this card to other, first by suit, then rank.  ==> this is written in the form of tuple
    #    returns: boolean

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


'''
    # def __lt__(self, other):
    #     # check the suits
    #     if self.suit < other.suit: return True
    #     if self.suit > other.suit: return False
    #     
    #     # suits are the same ... check ranks
    #     return self.rank < other.rank
'''


# ==================================  class Deck  =================================================

class Deck:
    """Represents a deck of cards.

        Attributes:
          cards: list of Card objects.
        """

    # Initializes the Deck with 52 cards.

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)            # card is as object
                self.cards.append(card)

                # Returns a string representation of the deck

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # Adds a card to the deck.
    #       card: Card

    def add_card(self, card):
        self.cards.append(card)

    # Removes a card from the deck or raises exception if it is not there.
    # card: Card

    def remove_card(self, card):
        self.cards.remove(card)

    # Removes and returns a card from the deck.
    # i: index of the card to pop; by default, pops the last card.

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    #  Shuffles the cards in this deck.

    def shuffle(self):
        random.shuffle(self.cards)

    # Sorts the cards in ascending order.

    def sort(self):
        self.cards.sort()

        """Moves the given number of cards from the deck into the Hand.

                hand: destination Hand object
                num: integer number of cards to move
                """

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


# ==================================  class Hand  =================================================

class Hand(Deck):
    """" Represents a hand of playing cards
        Hand : the cards held by one player
        """

    def __init__(self, label=''):
        # super().__init__()
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)

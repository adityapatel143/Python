
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

    def __init__(self, suit = 0, rank=2):
        self.suit = suit
        self.rank = rank

# Returns a human-readable string representation.
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

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
    
card1 = Card(2, 11)

print(card1)

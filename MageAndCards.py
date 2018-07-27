import random
class Player:
    def __init__(self, deck, name, order):
        self.lifepoint = 20
        self.decksize = len(deck)
        self.deck = deck
        self.name = name
        self.order = order
        self.board = []
        self.hand = []
    def draw_card(self):
        n = random.randint(0,len(self.deck)-1)
        card_drawn = self.deck[n]
        self.deck.remove(card_drawn)
        self.hand.append(card_drawn)
        return card_drawn

class Card:
    def __init__(self, name, manacost):
        self.name = name
        self.tap = False
        self.manacost = manacost

class Creature(Card):
    def __init__(self, player1):

class Instant(Card):
    def __init__(self):

class InstantCible(Instant):
    def __init__(self, player1, player2):


class Enchant(Card):
    def __init__(self):

class EnchantCible(Enchant):
    def __init__(self):

class Sorcery(Card):
    def __init__(self):

class SorceryCible(Sorcery):
    def __init__(self, board):

class Land(Card):
    def __init__(self,type):

        self.type = type

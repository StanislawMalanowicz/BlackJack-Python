from random import shuffle
from deck_models import full_name_color, full_name_value, card_value

global str

# str = str(mar)


COLORS = ['S', 'C', 'H', 'T']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


    


class Card:

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.value}{self.color}"

    def talk_name(self):
        val = full_name_value(self.value)
        col = full_name_color(self.color)
        return f"hello {val} of {col}"


class BlackJackCard(Card):
    def check_value(self):
        card_val = card_value(self.value)
        return int(card_val)


class Hand:
    
    def __init__(self):
        self.cards = []

    def __str__(self):
        cards = ''
        if not self.cards:
            return '<pusta>'
        else:
            for card in self.cards:
                cards += f"{card}, "
            return cards
    
    
    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
    

class Player(Hand):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.point = 0
    
    def update_score(self):
        if self.cards:
            self.point = 0
            for card in self.cards:
                self.point += card.check_value()
    def reset_score(self):
        self.point = 0


class Deck(Hand):

    def populate(self, card_type):
        for col in COLORS:
            for val in VALUES:
                self.add(card_type(val, col))
    
    def shuffle(self):
        shuffle(self.cards)

    def deal(self, hands_list, cards_num):
        for i in range(cards_num):
            for hand in hands_list:
                card = self.cards.pop()
                hand.add(card)
                hand.update_score()

    def other_cards(self):
        return len(self.cards)

    

# card2 = BlackJackCard("A", "D")
# card3 = BlackJackCard("K","S")
# print(str(card2.value()))
# card2.check_value()
# card3.check_value()
# print("card2.check_value()")

    



# jan_player = Player("Jan")

# print(jan_player.name)
# print(jan_player.cards)


# new_hand = Hand()
# sec_hand = Hand()
# new_deck = Deck()
# new_deck.populate()
# new_deck.shuffle()
# print(new_hand)
# print(sec_hand)
# new_deck.deal([new_hand, sec_hand], 3)
# print(new_hand)
# print(sec_hand)
# card3 = Card("D", "Q")
# player1 = Hand()
# print(card2)
# print(card2.talk_name())

# print(card)
# # print(player1.he)
# player1.hello("jan")
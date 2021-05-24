from random import shuffle
from deck_models import full_name_color, full_name_value, card_value
from game_models import  play_and_return_winner


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

    

class Game:
    def __init__(self):
        self.active_players = []
        self.turn_counter = 0
        self.passed_players = []
        self.players_scoreboard = {}

    def start_game(self):
        number_of_players = int(input("podaj liczbe graczy <1-6>"))

        for x in range(0, number_of_players):
            player_name = input(f"podaj imie gracza nr {x}")
            player = Player(player_name)
            player.update_score()
            self.active_players.append(player)

        dealer = Player("Dealer")
        dealer.update_score()
        self.active_players.append(dealer)

        for player in self.active_players:
            self.players_scoreboard[player.name] = 0
    
    def play(self):
        want_to_play = input("Czy chcesz ropoczac gre? \n  <y> - tak")
        new_deck = Deck()
        new_deck.populate(BlackJackCard)
        new_deck.shuffle()
        minimum_cards = len(self.active_players) * 3
        
        while want_to_play == "y":
            print("Game in progres...")
            print("less cards in deck: ", new_deck.other_cards())

            for player in self.active_players:
                player.clear()

            new_deck.deal(self.active_players, 2)

            self.turn_counter += 1
            winner, players_list = play_and_return_winner(self.active_players, self.passed_players, new_deck)

            if winner and players_list:
                print("the winner is: ", winner)
                print("Players scorelist from round nr: ", self.turn_counter)
                for player in players_list:
                    print(f" Gracz {player.name} zdobyl {player.point} punktow")
                self.players_scoreboard[winner] +=1

            self.active_players = self.active_players + self.passed_players
            self.passed_players = []

            for player in self.active_players:
                player.reset_score()

            want_to_play = input("Czy chcesz zagrac jeszcze raz? \n  <y> - tak " )
            if new_deck.other_cards() < minimum_cards:
                not_enough_cards = input("Koncza sie karty jak wcisniesz Enter to dobiore, zostalo: niewiele")
                new_deck.cards = []
                new_deck.populate(BlackJackCard)
                new_deck.shuffle()
        print("Koniec, dzieki za gre")

    def show_players(self):
        for player in self.active_players:
            print("Gracz: ", player.name)
    
    def show_scoreboard(self):
        print("Players score:")
        for player_name, points in self.players_scoreboard.items():
            print(player_name," => ", points)
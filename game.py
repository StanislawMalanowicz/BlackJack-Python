from deck import BlackJackCard, Deck, Player
from game_models import turn, finish_game, play_and_return_winner

# start kometarza ======================================

# new_deck = Deck()
# print(new_deck)
# new_deck.populate( BlackJackCard)
# new_deck.shuffle()
# print(new_deck)

# player1 = Player("Player_One")
# player2 = Player("Player_Two")
# dealer = Player("Dealer")

# players_list = [player1, player2, dealer]
# passed_players_list = []


# # ▸ Rozdaj na początek wszystkim graczom i rozdającemu po 2 karty
# new_deck.deal(players_list, 2)

# player1.update_score()
# player2.update_score()

# # ▸ Dla każdego gracza
#     # ▸ Dopóki gracz prosi o dodatkową kartę i nie ma fury
# while players_list:
#     print("players in game: ")
#     for player in players_list:
#         print(player.name)
#     turn(players_list, passed_players_list, new_deck)
        

# koniec kometarza ======================================

# # ▸ Jeśli nie ma już graczy pozostających w grze
# finish_game(players_list, passed_players_list)

    # ▸ Pokaż karty rozdającego, gracze przegrywają





class Game:
    def __init__(self):
        self.active_players = []
        self.turn_counter = 0
        self.passed_players = []
        self.players_scoreboard = {}

        # pass
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
        print("Koniec, dzieki za gre")

    def show_players(self):
        for player in self.active_players:
            print("Gracz: ", player.name)
    
    def show_scoreboard(self):
        print("Players score:")
        for player_name, points in self.players_scoreboard.items():
            print(player_name," => ", points)

new_game = Game()
new_game.start_game()
new_game.play()
# new_game.show_players()
new_game.show_scoreboard()
print("liczba zagranych rund: ", new_game.turn_counter)





# ▸ W przeciwnym razie

    # ▸ Dopóki rozdający musi dobierać karty i nie ma fury

        # ▸ Wydaj rozdającemu dodatkową kartę

    # ▸ Jeśli rozdający ma furę

        # ▸ Dla każdego gracza pozostającego w grze

            # ▸ Gracz wygrywa

    # ▸ W przeciwnym razie

        # ▸ Dla każdego gracza pozostającego w grze

            # ▸ Jeśli suma punktów gracza jest większa niż suma punktów rozdającego

                # ▸ Gracz wygrywa

            # ▸ W przeciwnym razie, jeśli suma gracza jest mniejsza niż suma rozdającego

                # ▸ Gracz przegrywa
            # ▸ W przeciwnym razie
                # ▸ Gracz remisuje
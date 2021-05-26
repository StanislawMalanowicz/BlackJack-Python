from deck import Game


# new_game = Game(test_for_aces=True)
new_game = Game()
new_game.start_game()
new_game.play()
# new_game.show_players()
new_game.show_scoreboard()
print("liczba zagranych rund: ", new_game.turn_counter)



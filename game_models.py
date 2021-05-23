import operator


def turn(players_list, passed_players_list, new_deck):
    
    for player in players_list:

        # partia gracza
        if player.name != "Dealer":
            print(f"\n -------------\n\n Punkty gracza {player.name} : {player.point}")
            pick_card = input(f"Fraczu {player.name}: Chcesz dobrac karte? \n <y> - tak")

            # ▸ Wydaj graczowi dodatkową kartę
            if pick_card == "y":
                new_deck.deal([player], 1)

                # sprawdz czy gracz nie ma fury
                if player.point > 21:
                    print(f"Punkty gracza: {player.name} ({player.point} pkt.) przekryczyly dozwolone 21")
                    print("Przegrywasz")
                    players_list.remove(player)
                    passed_players_list.append(player)
            else:
                players_list.remove(player)
                passed_players_list.append(player)

        # partia krupiera
        else:
            # jesli ma mniej niz 17 punktow, niech dobierze karte
            if player.point < 17:

                new_deck.deal([player], 1)
                player.update_score()
            # jesli krupier ma fure zakoncz gre
                if player.point > 21:
                    players_list.remove(player)
                    passed_players_list.append(player)
                    return

            # niech kurpier passuje
            else:
                print('dupa, dealer wiecej nie pobiera')
                players_list.remove(player)
                passed_players_list.append(player)


def finish_game(begin_list, new_list):
    print("**************************\n")
    print("finish game method")
    print("**************************\n")
    final_list = begin_list + new_list
    looser_list = []
    winner_list = []
    sorted_list = []

    for player in final_list:
        if player.point > 21:
            looser_list.append(player)
        else:
            winner_list.append(player)
   
    sorted_list = sorted(winner_list, key=operator.attrgetter("point"))
    if sorted_list:
            return sorted_list[-1].name, final_list
    
    print("Wszyscy udupili!!!")
    return '', []


def play_and_return_winner(players_list, passed_players_list, new_deck):

    print("player list ")
    for player in players_list:
        print(f"    {player.name} ma {player.point} pkt" )

    #     ▸ Dopóki gracz prosi o dodatkową kartę i nie ma fury
    while players_list:
        turn(players_list, passed_players_list, new_deck)
    return finish_game(players_list, passed_players_list)


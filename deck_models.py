def full_name_value(val):
    if val == "A":
        return "Ace"
    elif val == "K":
        return "King"
    elif val == "Q":
        return "Qeen"
    elif val == "J":
        return "Jack"
    else:
        return val

def full_name_color(col):
    if col == "S":
        return "Spades"
    elif col == "C":
        return "Clubs"
    elif col == "H":
        return "Hearts"
    elif col == "D":
        return "Diamonds"

# dodac dane o aktualnej punktacji gracza:
def card_value(val):
    if val == "A":
        return "11"
    elif val == "K":
        return "10"
    elif val == "Q":
        return "10"
    elif val == "J":
        return "10"
    else:
        return val


















# trash
  # if player_points <= 10:
        #     print("punkty gracza: ", player_points)
        #     print("THIS IS big ACE: ")
        #     return "11"
        # else:
        #     print("punkty gracza: ", player_points)
        #     print("THIS IS small ACE: ")
        #     return "1"
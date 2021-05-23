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

def card_value(val):
    # print("meethot card: ", val)
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
    # return val
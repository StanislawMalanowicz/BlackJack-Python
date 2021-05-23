# class Game:
#     def __init__(self) -> None:
#         pass
# class Test:
#     def __init__(self):
#         self.name = "Test"
#         pass

#     def create_surname(self):
#         self.surname = "Nazwisko"

# xx = Test()
# print(xx.name)
# # print(xx.surname)
# xx.create_surname()
# print(xx.surname)

# class Game:
#     def __init__(self):
#         self.players = []
#         # self.dealer_wins = 0
#         self.players_scoreboard = []

#         # pass
#     def start_game(self):
#         number_of_players = int(input("podaj liczbe graczy <1-6>"))
#         for x in range(0, number_of_players):
#             print("hello, ", x)
#         for player in self.players:
#             self.players_scoreboard.append({player.name : 0})


#         # pass

# newgame = Game()
# newgame.start_game()

# d = {'jan': 0,'alek': 3,'Dealer': 1}

# for k, v in d.items():
#     print(k)
#     print(v)

# import operator

lis = [{ "name" : "Nandini", "point" : 33},
{ "name" : "Manjeet", "point" : 18 },
{ "name" : "Nikhil" , "point" : 25 }]

newlist = sorted(lis, key= lambda i: i['point'])

for user in newlist:
    print(f"has punktow {user['point']}" )

print(lis[1].get("point") )
print(lis[1]['name'] )
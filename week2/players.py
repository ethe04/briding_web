players = ['charles','martina','michael','florence','eli']
print(players[0])
print(players[0:3]) #the output is sublist of players
some_players = players[0:3]
print(f"Some players are {some_players}")
print(players[:4]) #default start index 0
print(players[2:]) #omitting stop index means it will work through the last item
print(players[-3:])

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
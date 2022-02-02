players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # only print the first players

print(players[1:4]) # only print players 2, 3 and 4

print(players[:4]) # only prints players until forth

print(players[2:]) # only prints players after second

print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
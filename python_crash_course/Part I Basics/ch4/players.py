players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:4])
print('-'*50)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print('-'*50)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
print('-'*50)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
print('-'*50)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-2:])

print('-'*50)
#Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first two players on my team:")
for player in players[:2]:
 print(player.title())
print('-'*50)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the last two players on my team:")
for player in players[-2:]:
 print(player.title())
print('-'*50)

#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
print(my_foods)
friend_foods = my_foods[:] #copy
print(friend_foods)
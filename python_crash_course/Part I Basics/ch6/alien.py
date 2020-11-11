alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print('-'*50)
#Working with Dictionaries
#A dictionary is a collection of key-value pairs ,dynamic structures
#Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])
print('-'*20)
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print('-'*50)
#Adding New Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('-'*50)
#Starting with an Empty Dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print('-'*50)
#Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


#Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)
print('^'*50)

#  syntax => for target_list in expression_list:
 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(f'{magician.title()},that was a great trick! I can\'t wait to see your next trick, {magician.title()}.\n')
  print(f'{magician.capitalize()},that was a great trick!I can\'t wait to see your next trick, {magician.capitalize()}.\n')
  print(f'{magician.lower()},that was a great trick!I can\'t wait to see your next trick, {magician.lower()}.\n')
  print(f'{magician.upper()},that was a great trick! I can\'t wait to see your next trick, {magician.upper()}.\n')
  print('^'*50)
print('loop Ended')
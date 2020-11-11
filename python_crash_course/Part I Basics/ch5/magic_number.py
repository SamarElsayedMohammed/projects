answer = 17
if answer != 42:
  print("That is not the correct answer. Please try again!")
print('-'*50)

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

print('-'*50)
age_0 = 22
age_1 = 18
print( age_0 >= 21 and age_1 >= 21)
print('-'*50)
print((age_0 >= 21) and (age_1 >= 18))
print('-'*50)

print(age_0 >= 21 or age_1 >= 21)
print('-'*50)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
print('-'*50)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('onions' in requested_toppings )
print('apple' in requested_toppings )

print('-'*50)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")
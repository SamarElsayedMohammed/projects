print("*"*50)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("*"*50)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
# print(bicycles[4]) #IndexError: list index out of range
print("*"*50)
print(bicycles[0].title()) 
print(bicycles[1].capitalize())
print(bicycles[2].upper())
print(bicycles[3].lower())
print("*"*50)
print(bicycles[-1])#specialized
print(bicycles[-2])#redline
print(bicycles[-3])#cannondale
print(bicycles[-4])#trek
print("*"*50)
print(len(bicycles))
print("*"*50)
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
message = f"My last bicycle was a {bicycles[-1].title()}."
print(message)
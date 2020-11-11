cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print('='*50)

# reverse order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
print('='*50)

#Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print('%'*30)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)
print('@'*30)

#Printing a List in Reverse Order
#revese the item position not order items
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print('+'*30)

#Finding the Length of a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
print('+'*30)

#Avoiding Index Errors When Working with Lists

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) 
# #File "motorcycles.py", line 2, in <module>
# print(motorcycles[3])
# IndexError: list index out of range
print(motorcycles[-1])
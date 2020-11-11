#Modifying Elements in a List
print("-"*50)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'.title() #replace honda with ducati
print(motorcycles) #after modify first element
motorcycles[-1] = 'motorela'.upper() #replace suzuki with motorela
print(motorcycles) #after modify last element
print("-"*50)

#Adding Elements to a List
motorcycles.append('ducati')
print(motorcycles)
motorcycles.append('kia')
print(motorcycles)
print("-"*50)

cars=[]
print(cars)
cars.append("kia")
cars.append('suny')
cars.append("marsedise")
cars.append("IBM")
print(cars)
print('-'*50)

#Inserting Elements into a List
#syntax  insert(index,element)
char=[]
print(char)
char.insert(0,'a')
char.insert(1,'b')
char.insert(-1,'c')
char.insert(-2,'d')
char.insert(2,'e')
char.insert(-1,'f') #postion before the last element
print(char)
print('-'*50)

#Removing Elements from a List
numbers=[1,2,3,4,5]
print(numbers)
del numbers[0]
del numbers[-1]
print(numbers)
print('-'*50)

#Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #remove the last item
print(motorcycles)
print(popped_motorcycle)
print('='*30)

#Popping Items from any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_item = motorcycles.pop(0) #remove the particular item
print(motorcycles)
print(f"the first item removed is : {popped_item.upper()}" ) #syntax pop(index)
print('='*50)

#Removing an Item by Value

names =['samar ,talia','samah']
print(names)
names.remove('samah')
print(names)
print('='*30)

notFreind = 'soma'
names =['samar ,talia','samah','soma']
print(names)
names.remove(notFreind)
print(names)
print(f"A \"{notFreind}\" is not my friend")
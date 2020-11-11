squares = []
for value in range(1, 11):
 square = value ** 2
 squares.append(square)
 print(squares)
print('*'*50)

 #output
# [1]
# [1, 4]
# [1, 4, 9]
# [1, 4, 9, 16]
# [1, 4, 9, 16, 25]
# [1, 4, 9, 16, 25, 36]
# [1, 4, 9, 16, 25, 36, 49]
# [1, 4, 9, 16, 25, 36, 49, 64]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = []
for value in range(1, 11):
 square = value ** 2
 squares.append(square)
print(squares)


print('*'*50)
squares = []
for value in range(1,11):
 squares.append(value**2)
print(squares)
print('*'*50)
#list
digits =list(range(0,10))
print(f'the minimum value is :{min(digits)}')
print(f'the maxmum value is :{max(digits)}')
print(f'the sumetion  value is :{sum(digits)}')
print('-'*50)


squares = [value**2 for value in range(1, 11)]
print(squares)

print('-'*50)
sq = list(value**2 for value in range(1,11))
print(sq)
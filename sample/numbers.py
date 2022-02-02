for value in range(1, 5):
    print(value)            #only prints untill 4

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2)) # numbers between 2 and 11 but: 2, 2+2, 4+2 ... 8+10
print(even_numbers)

squares = []
for value in range(1, 11):  # value is a variable with every number between 1 and 10
    square = value ** 2     # square is the square of value: ** is exponential (like ^)
    squares.append(square)  # this adds square items to squares variable

print(squares)

# simpler way to do the same:
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# list of comprehension to produce the same list
squares = [value**2 for value in range(1, 11)]
print(squares)

#--------------------
# try it yourself

#4.3
twenty = list(range(1, 21))
print(twenty)

#4.4
million = list(range(1, 1000001))
for mil in million:
    print(mil)

#4.5
million = list(range(1, 1000001))
min(million)
max(million)
sum(million)

#4.6
odd_numbers = list(range(1, 20, 2))
for odd in odd_numbers:
    print(odd)

#4.7
threes = list(range(3, 31, 3))
for three in threes:
    print(three)

#4.8 and 4.9
cubes = list(value ** 3 for value in range(1, 11))
for cube in cubes:
    print(cube)
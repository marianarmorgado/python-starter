from pickle import TRUE
from sqlite3 import enable_shared_cache


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sorts list by alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True) # sorts list by reverse alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHereis the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse() # print in reverse order
print(cars)

cars = ['audi', 'bmw', 'subaru', 'toyota']
len(cars) # length of a list

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw' # to set the value of car to 'bmw'
car == 'bmw' # to check whether this is true (checking for equality)
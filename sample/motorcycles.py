motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #change items of list
print(motorcycles)

motorcycles.append('ducati') #add items to list
print(motorcycles)

motorcycles = [] # a more dynamic way to create list and add items to it
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati') # add item to list position 0
print(motorcycles)

del motorcycles[0] # delete item in position 0
print(motorcycles)

popped_motorcycle = motorcycles.pop() # creates new variable with last item, while removing the item from motorcycles
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop(0) # creates new variable with first item, while removing the item from motorcycles
print(motorcycles)
print(last_owned)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati') # removes item by name
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.") # \n is an empty line
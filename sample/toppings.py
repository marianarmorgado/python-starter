requested_topping = 'mushrooms'

if requested_topping != 'onions': #checking for inequality
    print("Hold the onions")

requested_toppings = ['mushrooms', 'onions', 'pinapple']
'mushrooms' in requested_toppings # checking if a value is in a list
'garlic' in requested_toppings

topping = 'garlic'
if topping not in requested_toppings:
    print(topping.title() + ", you are not a topping!")

requested_toppings = ['mushrooms', 'extra vegan cheese']

# testing multiple conditions

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepper' in requested_toppings:
    print("Adding peppers.")
if 'extra vegan cheese' in requested_toppings:
    print("Adding extra vegan cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra vegan cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making yout pizza!")

# if there are no green peppers

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making yout pizza!")

# checking if a list is empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plane pizza?")

# using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'tomatoes', 'pinapple', 'extra vegan cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra vegan cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making yout pizza!")
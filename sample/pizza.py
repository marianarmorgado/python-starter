# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra vegan cheese']
}

# summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza" + 
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
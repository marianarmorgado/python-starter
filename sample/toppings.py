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
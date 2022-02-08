age = 12
if age < 4:
    print("Your admission cost is 0€.")
elif age < 18:                              # another if test that only runs if previous if test failed
    print("Your admission cost is 5€.")
else:
    print("Your admission cost is 10€.")

# cleaner code

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is " + str(price) + "€.")

# you can omit the else in some cases

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is " + str(price) + "€.")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(
    "Sarah's favourite language is " +
    favourite_languages['sarah'].title() +
    "."
)

favourite_languages['sarah']

# looping through all the keys in the dictionary

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
        language.title() + ".")

for name in favourite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favourite language is " +
            favourite_languages[name].title() + "!")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favourite_languages.keys()): # looping in order
     print(name.title() + ", thank you for taking the poll.")
    
print("The following languages have been mentioned:") # looping through all values
for language in favourite_languages.values():
    print(language.title())

print("The following languages have been mentioned:") # looping through all values but doesn't repeat duplicates
for language in set(favourite_languages.values()):
    print(language.title())
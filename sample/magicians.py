magicians = ['alice', 'david', 'carolina']
for magician in magicians: # loop to pull a name from magicians and store it in variable magician
    print(magician)        # it will pull each name at a time in loop until it pulls all three names in order
                           # variable magician end up only containing the last name: carolina

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title())
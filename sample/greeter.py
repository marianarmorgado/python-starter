# defining or creating a function

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# passing information to a function

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('nana')

# try it yourself 8-1

def display_message():
    """Display what I'm learning about in this chapter."""
    print("I'm learning about functions and parameters in Chapter 8.")

display_message()

# try it yourself 8-2

def favourite_book(title):
    """Display one of my favourite books title."""
    print("One of my favourite books is " + title.title() + ".")

favourite_book('Alice in Wonderland')
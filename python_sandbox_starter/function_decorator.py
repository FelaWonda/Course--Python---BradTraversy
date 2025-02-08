 """
    A function decorator in Python is a design pattern that allows you to modify or enhance 
    the behavior of a function or method without permanently changing its source code. 
    Decorators are essentially functions that take another function as an argument and 
    return a new function, usually with additional functionality wrapped around the 
    original function.
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

# Description: This file contains the decorators used in the project.
#Un decorador en Python es una función que toma otra función como argumento, amplía el comportamiento de esta función sin modificarla explícitamente.

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
    
hello()
import cookfood # importing entire module
from cookfood import mix  # importing particular function 
from cookfood import mix as m # importing particular function with alis
from cookfood import *  # importing all function 

def vegfood(items):
    mix(items)
    m(items)
    cookfood.startCooking("veg")

if __name__ == "__main__":
    vegfood("potato")

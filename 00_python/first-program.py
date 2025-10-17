kattle_is_empty = True
clean_cup = True

def make_chai(kattle_is_empty,clean_cup):
    
    kattle_is_empty = kattle_is_empty
    clean_cup = clean_cup
    print("kattle_is_empty = "+str(kattle_is_empty))
    if not ketttle_has_water():
        fill_it_with_water()
    plugin_kattle()
    boil_water()
    if not cup_is_not_clean():
        wash_cup()
    add_to_cup("tea leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stie("cup")
    serve("server chai")


def ketttle_has_water() :
    return kattle_is_empty

def fill_it_with_water() :
    print("filling kattle")
   
def plugin_kattle() :
    print("kattle pluged in")

def boil_water():
    print("water boiling")

def cup_is_not_clean() :
    return clean_cup

def wash_cup():
    print("washing cup")

def add_to_cup(type):
    print (type +" added to cup") 

def pour():
    print ("pored in cup") 

def stie():
    print ("stiering the cup") 

def serve():
    print ("Serving the chai") 

if __name__ == "__main__":
    make_chai(True, True)
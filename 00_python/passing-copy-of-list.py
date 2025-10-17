cities = ['city 1', 'city 2', 'delhi', 'city 4', 'city 5', 'delhi', 'city 7', 'city 8', 'delhi', 'city 10']
citiesNew = []
def filterCity(list1, list2):
    for i in range (1, 11):
        if(i % 3 == 0):
            list2.append(list1[i])
    print(list2)
    print(list1)


cities2= cities[:] # to copy a list just use [:]
print(cities2)

#passing arbitrary number of argument to function

def pizzaTopping(*topppings):
    print(f"topping {topppings}")

if __name__ == "__main__":
    filterCity(cities[:], citiesNew)    
    pizzaTopping("pepperoni")
    pizzaTopping('mushrooms', 'green peppers', 'extra cheese')

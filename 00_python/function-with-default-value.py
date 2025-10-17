def searchDataByLocation(location = "Delhi"):
    if(location == "Delhi"):
        print(f"your are searching for default location {location}")
    else:
        print(f"your are searching {location}")   


cities = []
def askUserToFillTheList(city = "delhi"):
      cities.append(city)  




if __name__ == "__main__":
    searchDataByLocation("Mumbai")
    for i in range(1, 11):
        if(i % 3 == 0):
            askUserToFillTheList()
        else:    
            askUserToFillTheList(f"city {i}")

    print(cities)


    
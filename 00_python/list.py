bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(len(bicycles))

for i in bicycles:
    print(i)

print("###############################")

for i in reversed(bicycles):
    print(i.upper())    

print("###############################")
for i in range(len(bicycles) - 1, -1, -1):
    print(bicycles[i])

# Unlike Java python also provide negative index. For example -1 is the last, -2 is the second last 


days_in_month = []

for i in range(1,31,1):
    days_in_month.append(i)

print(days_in_month)    

days_in_month.insert(len(days_in_month)+1, 31)

print(days_in_month)    


# use del to delete element from the list if you know the index

del days_in_month[30]

print(days_in_month)    

# Use pop to delete and get the item from the list, The pop() method removes the last item in a list, but it lets you work
#  with that item after removing it

x = days_in_month.pop()
print(x)
print(days_in_month)    

company = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(company)
company.remove('honda')
print(company)


#sort list
company.sort()
print(company)

#Sort in reverse 
company.sort(reverse=True)
print(company)

#sorting the list with sorted to keep orginial list intect

print(sorted(company))
print(company)

print(sum (days_in_month))
print(min (days_in_month))
print(max (days_in_month))

#without List comprehension
squares = []
for i in range(1, 10):
    squares.append(i*i)
    print(squares)   
print("with List comprehension")
#with List comprehension
squares1 = [value**2 for value in range(1, 10)]
print(squares1)   

#Slicing a list
bikes = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(bikes[0:2])

copyBikes = bikes[:]
print(copyBikes)


#Check list contains an element
if 'honda' in bikes:
    print('Yeah, I am there!')
else:
    print("Sorry not me")



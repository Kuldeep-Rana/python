for i in range(1,11):
    if(i % 2 ==0):
        print("even")
    else:
        print("odd")    


#if with multiple conditions

days = ['Sunday','Monday','Tuesday','Wednesday','ThrusDay','Friday','Saturday']

for day in days:
    if day.startswith('S') or day.startswith('T'):
        print("==> "+day)
    else:
        print("----> "+day)        


print(f"{days[0]}, is the day")

print (len(days) ==7)

print (len(days) > 7)

print ('Monday' == days[1])

print ("Kuldeeep" == days[0])

print ('Monday'.lower() == days[1])

num = 10;

if num > 9 and num < 11:
    print("its 10")

print (num == 10)    

print ( 'Monday' in days)

print ( 'Monday' not in days)

# if elif & else 

numbers = [10,13, 15, 17, 19]

for n in numbers:
    if(n % 2 == 0):
        print("its an even number")
    elif( n % 3 == 0):
        print("its an odd number")
    else:
        print("its prime number")    


while True:
    num = int(input("enter any num:"))

    if( num == 0):
      print("its a zero")
    elif (num == 1):
        print("its a one")
    elif (num == 2):
        print("its two")
    elif (num == 3):
        print("its three") 
    elif (num < 0):
        print("its a negative number, throwing you out !!!")
        break; 
    else:
        print(f"{num} its greater than three") 

    

      
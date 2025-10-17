intSum = 2+3
print(intSum)

floatSum = 2.5+3.6
print(floatSum)

floatSum1 = 0.2 + 0.1
print(round(floatSum1,1))

#define number with underscore

a_long_number = 15_000_333_4444_555

print(a_long_number)

a = 1000
b = 1_000
c = 10_00
d = 100_0

print (a==b)
print (a==c)
print (a==d)

x,y,z = 10,20,30

print ("x "+str(x))
print ("y "+str(y))
print ("z "+str(z))

DAYS_IN_A_YEAR = 365 # Python consider this as a constant


nums = [value for value in range (1,101)]

#get the odd numbers without list comprehension 
odds = []
for n in nums :
    if n % 2 != 0:
        odds.append(n)

print(odds)

#get the odd numbers with list comprehension 
oddsNew =  [value for value in range (1,101) if value %2 != 0]
print(oddsNew)
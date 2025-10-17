num1 = 121;
# check if its prime

for i in range(2, num1):
    
    if(num1 % i ==0):
        print(f"{num1} is not a prime number")
        break;
    else:
        print(f"{num1} is a prime number")    
        break;

# Check if the number is an Armstrong number - number's each digit sum is equal to it self, when each digit power is
#  raised to the number of digits in the number

orgnalNum = 153
num2 = orgnalNum 
digitSum = 0
for i in range(len(str(num2))):
    digit = num2 % 10
    digitSum += digit*digit*digit
    num2 = int(num2 / 10)

if num2 == digitSum:    
    print(f"{orgnalNum} is a Armstrong number")
else:
    print(f"{orgnalNum} is not a Armstrong number")    


# Check if the number is a Palindrome number - number's read same from both the direction

num3 = 121
temp = num3
revNum = 0
while num3 > 0:
    revNum =  revNum * 10 + int(num3 % 10) 
    num3 //= 10  

if(num3 == revNum):
    print( f"{temp} is a prime Palindrme number")
else:
    print( f"{temp} is not a prime Palindrme number")





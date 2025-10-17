name = "kuldeep rana"


print(name.title())

print(name.upper())

print(name.capitalize())

print(name.casefold())

print(name.count("e"))

print(name.encode())

arr = name.split(" ")
print(len(arr))

for i in arr:
    print(i)

# iteration with range 

for i in range(len(arr)):
    print(arr[i])    

#Using variables in String

first = "Hello"

last = "world"

message = "Good morning, " + first +" "+ last
print(message)

messageNew = f"Good afternoon, {first} {last}"
print(messageNew)

messageWithWhiteSpace = " Hi, How are you doing "
print(messageWithWhiteSpace + "1")
print(messageWithWhiteSpace.rstrip()+"1")
print(messageWithWhiteSpace.lstrip())

#Reverse string
str = "122"
reversed_text = str[::-1]
print(reversed_text)

reversed_text = ''.join(reversed(str))
print(reversed_text)  

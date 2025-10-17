#play with list and dictionary

# create a list 
# create a dictionary 
# create a tuple

# manipulate them

my_list = ["apple", "banana", "cherry", "date", "elderberry"]

my_dict = {
    "name": "Alice",
    "age": 28,
    "city": "New York",
    "country": "USA",
    "occupation": "Engineer"
}

my_tuple = ("red", "green", "blue", "yellow", "purple")


print("List:", my_list)
print("Dictionary:", my_dict)
print("Tuple:", my_tuple)

print(my_list[2:4]) # the right value is exclusive - effective output will be - index 2 and 3

my_list.append("orrage")
my_list[0] = "Apple"
print("List:", my_list)
print(my_list[0] == 'Apple') # string with "" is == to ''

print(my_dict.get('name'))
x= my_dict.pop("name")
print(my_dict)
print(x)

my_dict['name'] = "Kuldeep"
print(my_dict)

my_dict.popitem()
print(my_dict)

for key in my_dict.keys():
    print(f"key - {key}")
    print(f"value - {my_dict.get(key)}")


if "age" in my_dict:
    print("exist") 
else:
    print("not exist")     

#my_tuple = ("red", "green", "blue", "yellow", "purple")

print(my_tuple[0])

print(my_tuple[1:4])

# usually we can't modify the tuple but we can concat.
my_tuple = my_tuple + ("megnta","black")

print(my_tuple)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

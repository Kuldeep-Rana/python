import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)



with open(filename) as file:
    nums = json.load(file)
    print(nums)


userJsonFile = "user.json"
with open(userJsonFile) as userJson:
    users = json.load(userJson)

for user in users:
    items = user.items() 
    for key, value in items:
        print(f"key : {key} and value : {value}")
    print("")

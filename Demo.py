d1={"Name":"ABC","Class":9,"Age":12,"School":"Pates","Country":"England"}
print(d1)
d1["Hobbies"]="Coding"
print(d1)
d1["Age"]="13"
print(d1)
del d1["Country"]
print(d1)
for key in d1.keys():
    print(key)
for key in d1.keys():
    print(d1[key])
for value in d1.values():
    print(value)
user_input = input("Enter an item in the dictionary:")
if str(user_input) in d1:
    print(d1[user_input])
else:
    print("OK.")
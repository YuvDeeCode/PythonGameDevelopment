numbers={}
user_input = input("Enter your number: ")
for n in user_input:
    if n.isdigit():
        if n in numbers:
            numbers[n]=numbers[n]+1
        else:
            numbers[n]=1
print(numbers)
status=True
for i in numbers.values():
    if i==0:
        status=False
    else:
        status=True
if status==True and len(numbers)==10:
    print("It is a panagram!")
else:
    print("It isn't a panagram.")


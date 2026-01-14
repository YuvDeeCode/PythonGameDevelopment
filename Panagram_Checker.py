alphabet = {}
user_input = str(input("Enter a string: "))
for c in user_input:
    if c.isalpha():
        if c in alphabet:
            alphabet[c]=alphabet[c]+1
        else:
            alphabet[c]=1
print(alphabet)
status=True
for i in alphabet.values():
    if i==0:
        status=False
    else:
        status=True
if status==True and len(alphabet)==26:
    print("It is a panagram!")
else:
    print("It's not a panagram")
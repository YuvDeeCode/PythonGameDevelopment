alphabet = {}
user_input = str(input("Enter a string: "))
for c in user_input:
    if c.isalpha():
        if c in alphabet:
            alphabet[c]=alphabet[c]+1
        else:
            alphabet[c]=1
print(alphabet)
#HW:.isdigit()
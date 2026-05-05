user_input = str(input("Enter a string that you think is a panagram: "))
user_input = list(user_input)
set(user_input)
#alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
alphabet=[]
for letter in user_input:
    if letter.isalpha():
        alphabet.append(letter)
alphabet = set(alphabet)
if len(alphabet)<26:
    print("This string is not a panagram")
elif len(alphabet) == 26:
    print("This string is a panagram")
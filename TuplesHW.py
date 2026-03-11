groups=[]
for i in range(5):
    a = input("Enter your group name: ")
    b = input("Enter the size of your group: ")
    c = input("Enter the date of your competition: ")
    d = input("Enter your venue: ")
    e = input("Enter the type of medal: ")

    tuple1 = (a,b,c,d,e)
    groups.append(tuple1)
print(groups)
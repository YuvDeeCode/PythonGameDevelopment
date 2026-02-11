#Creating a matrix
m1=[[1,2,3],[4,5,6],[7,8,9]]
print(m1)
    #Checking no. rows
print(len(m1))
    #Checking no. columns
print(len(m1[0]))
    #Printing element in the inner list in 2D list.
print(m1[1][1])
for i in range(len(m1)):
    for j in range(len(m1[0])):
        print(m1[i][j],end=" ")
    print("\n")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

m2=[]

for i in range(rows):
    temp=[]
    for j in range(columns):
        element = int(input("Enter an element: "))
        temp.append(element)
    m2.append(temp)
for i in range(rows):
    for j in range(columns):
        print(m2[i][j],end=" ")
    print("\n")

mat1=[[1,2],[3,4]]
mat2=[[5,6],[7,8]]
result1=[[0,0],[0,0]]
result2=[[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        result1[i][j]=mat1[i][j]+mat2[i][j]
        result2[i][j]=mat2[i][j]-mat1[i][j]

for i in range(2):
    for j in range(2):
        print(result1[i][j],end=" ")
    print("\n")

for i in range(2):
    for j in range(2):
        print(result2[i][j],end=" ")
    print("\n")

m3=[]
for i in range(3):
    temp2=[]
    for j in range(3):
        element= int(input("Enter an element: "))
        temp2.append(element)
    m3.append(temp2)

for i in range(3):
    print(m3[i][i])
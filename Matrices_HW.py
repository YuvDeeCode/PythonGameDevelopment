import random
m1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        print(m1[i][j],end=" ")
    print("\n")

x = max((max(x) for x in m1))
print(x)

for i in range(len(m1)):
    for j in range (len(m1[0])):
        if m1[i][j] == x:
            print(str(j)+","+str(i))
        else:
            continue

m2=[]
for i in range(3):
    li=[]
    for j in range(3):
        li.append(random.randint(0,9))
    m2.append(li)

for i in range(len(m2)):
    for j in range(len(m2[0])):
        print(m2[i][j],end=" ")
    print("\n")

column0 = m2[0][0] + m2[1][0] + m2[2][0]
column1 = m2[0][1] + m2[1][1] + m2[2][1]
column2 = m2[0][2] + m2[1][2] + m2[2][2]
diagonal1 = m2[0][0] + m2[1][1] + m2[2][2]
diagonal2 = m2[0][2] + m2[1][1] + m2[2][0]
row0 = m2[0][0] + m2[0][1] +m2[0][2]
row1 = m2[1][0] + m2[1][1] +m2[1][2]
row2 = m2[2][0] + m2[2][1] +m2[2][2]
if column0 == column1 == column2 == diagonal1 == diagonal2 == row0 == row1 == row2:
    print("This is a magic square!")
else:
    print("This is not a magic square.")
print("Column0: "+str(column0))
print("Column1: "+str(column1))
print("Column2: "+str(column2))
print("Diagonal1: "+str(diagonal1))
print("Diagonal2: "+str(diagonal2))
print("Row0: "+str(row0))
print("Row1: "+str(row1))
print("Row2: "+str(row2))
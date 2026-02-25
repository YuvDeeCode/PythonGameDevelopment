#A tuple is like other data sets but it cannot be modified.
#It can only be packed and unpacked as shown below.
#A tuple doesn't require brackets, but if you want to give brackets, use round brackets.
tuple1 = (1,2,3)
print(tuple1)
#Packing
a=1
b=2
c=3
tuple2=(a,b,c)
print(tuple2)
#-------------
#Unpacking:
t3=("hello world",True,496,2,1,"Ok")
a1,a2,a3,a4,a5,a6=t3
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
#-----------------------------------
#Nested Tuple
t4 =("Hello World",[1,2,3],(4,5,6),{"Hello":1,"Bye":2})
print(t4[2][2])
t5 = ("a","b","c","d","e","f")
print(t5[1:4])
print(t5[-1:-7:-1])
t4[1][1]=5
print(t4)
t4[1][1]=2
print(t4)
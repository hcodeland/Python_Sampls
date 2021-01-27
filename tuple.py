mytuple=("car","mobile","book","laptop")
print(type(mytuple))
print(mytuple)
print(len(mytuple))

# mytuple[1]="apple"
# print(mytuple)

mylist=list(mytuple)
mylist[1]="apple"
mytuple=tuple(mylist)
print(mytuple)

tuple1=(1,2,3)
tuple2=(4,5,6)
tuple1=tuple1+tuple2
print(tuple1)

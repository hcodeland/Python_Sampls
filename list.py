mylist=['car','book','mobile','computer','car','car']
print(mylist)
# print(type(mylist))
mylist[1]="python" #update
print(mylist)

#insert to list
mylist.insert(2,"apple")
print(mylist)

#remove as list
mylist.remove('car')
print(mylist)

#del
del mylist[1]
print(mylist)

#pop
mylist.pop()
print(mylist)

# Copt List
number1=[1,2,3,4]
number2=[5,6,7,8]
number1=number2
number1=number2.copy()

number2[1]=1000
print(number1)
print(number2)
new_list=number1+number2
number1.extend(number2)
print(new_list)
print(number1)

#Clear List
number1.clear()
print(number1)
#Sorted
number=[0,-1,1000,2,3]
print(number)
number.sort()
print(number)

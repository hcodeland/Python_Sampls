def first_list():
   yield 'laptop'
   yield 'computer'
   yield 'book'
for i in first_list():
   print(i)


def printNumber(n):
    num=0
    while num<10:
       yield num
       num+=1

for i in printNumber(10):
   print(i)


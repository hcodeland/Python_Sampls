def sey_hello(name):
   print("hello " + name)

n=input("Please Enter Name:")
sey_hello(n)
sey_hello("hamid")
sey_hello("milad")
sey_hello("mina")


def show_Info(name,lastname,age,email,country="iran"):
   print("name: " +name)
   print("last Name:" + lastname)
   print("age: " + str(age))
   print("email: " + email)
   print("country: " + country)

show_Info("hamid","hg",37,"h.haghshehas@emial.com")
show_Info("ali","imani",30,"ali@gmail.com","germany")


def calc_avg(set_number,set_unit):
   result=set_number/set_unit
   return result

number=calc_avg(370,30)
print("Avg: " + str(number))

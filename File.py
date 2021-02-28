path="C:/Users/Hamid._.Haghshenas/Desktop/Mysample/content.txt"
path2="C:/Users/Hamid._.Haghshenas/Desktop/Mysample/test.txt"
file=open(path,"r")
print(file.read())
list_file=file.readlines()
print(list_file)
print(file.readline())
print(file.readline())
file2=open(path2,"w+")
file2.write("c#.net")

file3=open(path2,"a")
file3.write("python")




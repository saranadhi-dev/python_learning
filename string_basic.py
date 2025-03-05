#indexing
message ="Hello! I am new to python"
index = 0
for i in message:
    print('message[ '+str(index)+' ] : '+i)
    index+=1

print('Character at index 10 : ' + message[10])

#Concat, Append and Multiple String
data = '7'
print((str(data)+' ')*3)
data+='3'
print(data)

#String are immutable
data = '15'
print(id(data))
data = '25'
print(id(data))

#String Formatting
name = 'user'
age = 5
percentage = 60.44
print("Name = %s and age = %d and grade = %f" %(name,age,percentage))

#Built in functions
str = 'hello'
print(str.center(16,'*'))


name = 'saran'
str = "saranaadithyan1"
print(str.count(name,0,(len(str))))
print(str.isalnum())
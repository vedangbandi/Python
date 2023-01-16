'''Perform the following operations on a list of names
Create a list of 5 names Anil Amol Aditya Avi Alka'''
#Print element and add anuj before aditya
list1=['Anil','Amol','Aditya','Avi','Alka']
list1.insert(2,'Anuj')
print(list1)
#Add zudu at last 
list1.append('zuhu')
print(list1)
#Remove avi
list1.remove('Avi')
print(list1)
#Replace Anil with anilkumar
list1[0]='anilkumar'
print(list1)
#Sort list
list1.sort()
print(list1)
#Print in reverse order
print(list1[::-1])

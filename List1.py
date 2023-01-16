''' Perform the following operations on list of numbers
'''
list1=[1,5,7,9,11]
print(list1)
list2=[2,4,6,8,10]
print(list2)
#Combine List
combine_list=list1+list2
print("Combine list:",combine_list)
#Display Prime numbers
prime_number=[11,17,29] + combine_list
print("prime number:",prime_number)
#Display elements
elements=len(prime_number)
print("Number of elements present in the list:",elements)
print(elements)
#Replace number in the list
R_List=prime_number
R_List[10]=100
R_List[11]=200
R_List[12]=300
print(R_List)
#Delete all the elements
R_List.clear()
print("Delete all the elements:",R_List)



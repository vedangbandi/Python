
#Dictionary in Python

Branches= {'FE':'Mechanical Engg,Chemical Engg,Computer Engg,Civil Engg,Electrical Engg,Artificial Intelligence And Data Science Engg',
               'Subjects':'Mathematics,Physics,Chemistry,Engg Mechanics,BEE,Engg Drawing'
               }
print("All Elements:",Branches)
#clear
Branches.pop("Subjects")
print("Pop Subjects:",Branches)
#copy
x = Branches.copy()
print("Copied Elements",x)
#Values
print("Key Values Stored in FE",Branches.values())
#Update
Branches.update(Branches)
print("Dictionary after updation:")
print(Branches)
#fromkeys
print("From keys opr:",dict.fromkeys(Branches, None))
#get
print(Branches.get(4, "Not found"))
#items
print(Branches.items())
#Keys
print(Branches.keys())
#pop
Branches.popitem()
print("After Pop opr:",Branches)
#setdefault
y = Branches.setdefault("Subject", "Physics")

print("Setdefault:",y)


#Dictionary in Python

Branches= {'FE':'Mechanical Engg,Chemical Engg,Computer Engg,Civil Engg,Electrical Engg,Artificial Intelligence And Data Science Engg',
               'Subjects':'Mathematics,Physics,Chemistry,Engg Mechanics,BEE,Engg Drawing'
               }
print("All Elements:\n\n",Branches)
#clear
Branches.pop("Subjects")
print("Pop Subjects:\n\n",Branches)
#copy
x = Branches.copy()
print("Copied Elements:\n\n",x)
#Values
print("Key Values Stored in FE:\n\n",Branches.values())
#Update
Branches.update(Branches)
print("Dictionary after updation:\n\n")
print(Branches)
#fromkeys
print("From keys opr:\n\n",dict.fromkeys(Branches, None))
#get
print("get:\n\n",Branches.get(4, "Not found"))
#items
print("items:\n\n",Branches.items())
#Keys
print("Keys:\n\n",Branches.keys())
#pop
Branches.popitem()
print("After Pop opr:\n\n",Branches)
#setdefault
y = Branches.setdefault("Subject", "Physics")

print("Setdefault:\n\n",y)


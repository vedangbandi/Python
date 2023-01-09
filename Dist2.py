"""
Assume Suitable value for distance between two cities(in km)
WAP to convert and print this 
distance in meteres,feet,inches and cm
"""

Distance= int(input("Distance between two cities in KM: "))

meter=Distance*1000
print("Distance in meter:",meter)
feet=Distance*3280.84
print("Distance in feet:",feet)
inches=Distance*39370.1
print("Distance in inches:",inches)
centimeter=Distance*100000
print("Distance in centimeter:",centimeter)




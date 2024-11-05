""" A person is booking ticket in railway , normal price is 50 and senior citizen if age
    is above 60 price is 30 , if child's age is below 12 years the price is 20 , calculate
    the total quantity of price of the tickets"""


total=0
n= int(input("Enter the Quantity of tickets:"))    #Quantity
for i in range(1,n+1):
    age = int(input("Enter the age of each person:"))
    
    if age>0 and age<12:
        total = total + 20   #child
        
    elif age>=12 and age<=60 :
        total = total + 50   #normal
        
    elif age > 60 :
        total = total + 30   #senoir citizen
    else:
        pass

    
    if age>0:

     pass

    else:

     print("Enter a valid age :")

print(total)

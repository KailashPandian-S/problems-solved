""" A person is ordering food from menu , apply discount 10% and print the amount if the price is above 500 otherwise print the amount """

print("Menu: \n1.Pizza - 200 \n2.Burger - 180\n3.Briyani - 250\n4.Dosa - 80\n5.Idly - 50")

k = int(input("How many food item you are going to order:"))
total = 0
for i in range(1,k+1):
 food = int(input("Enter the food number:"))
 n = int(input("Enter the Quantity:"))
 if food == 1 :
     total += 200 * n
 elif food == 2 :
     total += 180 * n
 elif food == 3 :
     total += 250 * n
 elif food == 4 :
     total += 80 * n
 elif food == 5 :
     total += 50 * n
 else:
     print("Please enter the food number in the menu card")

if total > 500 :
    print("You have 10% discount in your order" )
    price = total - (total * (10 /100))
    print("The discounted price is",price)
else:
    print("The total order price is",total)
  

 

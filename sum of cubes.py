#print the sum of cubes of the numbers from m to n

m= int(input())
n= int(input())
sum = 0
if n > m : 
 for i in range(m,n+1): 
    sum = sum + (i**3)
 print(sum) 
else: 
    print(False)
    

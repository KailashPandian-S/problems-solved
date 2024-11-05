"""You are a teacher creating a engaging math activity for your students by writing n numbers on the classroom white board .Use green pen to write the odd numbers and use red pens for even numbers , calculate the number of times you need to switch from a green pen to red pen """

a = input()
prev_green = False
prev_red = False

switches = 0

if int(a[0]) % 2 == 0 :
    prev_red = True #even
else:
    prev_green = True #odd

for i in range(2,len(a)):
    digit = int(a[i])
    even = False
    odd = False
    if digit % 2 == 0 :
        even = True
    else:
        odd = True
    if even==True and prev_green==True :
        switches += 1
print(switches)

def binarylogics(str_1):  #function defenition 
 r = len(str_1)
 if r == 0 or r<3:     #invalid string
     return -1



 result = int(str_1[0])
 char = None 


 for i in range(1,r):           #iterating string
    if str_1[i].isdigit(): 
        num = int(str_1[i])
        if char == "A": 
            result = result and num   #selecting the operator and and performing operation and storing it in result 
        elif char == "B": 
            result = result or num 
        elif char == "C": 
            result = result ^ num 
        else: 
            print("Invalid character")
    else: 
        char = str_1[i] 
        
 print(result)                       #printing result
 
ans = binarylogics("1C1A0A0C0B1A0")

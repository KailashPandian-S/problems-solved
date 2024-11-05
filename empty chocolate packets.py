""" A chocolate factory produces chocolates and packed them in the packets , the empty packets sgould be moved to the end of the conveyor belt"""

n = int(input())
arr = []

for i in range(1,n+1):
   ele = int(input())
   arr.append(ele)
for i in range(n):
  for i in range(0,n-1):
    current = arr[i]
    nxt = arr[i+1]
    if nxt < current :
        temp = nxt 
        nxt = current 
        current = temp
    arr[i] = current 
    arr[i+1] = nxt
cond = True
while cond:
    if arr[0] == 0 :
        arr.remove(arr[0])
        arr.append(0)
    else:
        cond = False
        break

print(arr)

        

"""stock max profit"""



#get stock price list from user 

n = int(input("Enter the size of the array: "))
stock_price_daily = []
for i in range(n): 
    price_element = int(input())
    stock_price_daily = stock_price_daily + [price_element] 
    
    
buy_sell_price = [] 
profits_final = []


#taking all combinations of stock buying and selling
for i in range(len(stock_price_daily)):   
    buy = stock_price_daily[i]                     #stock buying price
    for j in range(i,len(stock_price_daily)): 
        sell = stock_price_daily[j]
        element = [buy,sell] 
        buy_sell_price = buy_sell_price + [element]  #adding the elements combination to the buy_sell list 
        
        profit = buy - sell 
        profits_final = profits_final + [profit] 


max = -3576855667
max_index = 0
for i in range(len(profits_final)): #finding maximum profit
    if profits_final[i] >= max : 
        max = profits_final[i] 
        max_index = i 
        

result = buy_sell_price[i]


print(result)


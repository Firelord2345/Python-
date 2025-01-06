INTEGER_MAX_VALUE = 2**31 - 1 
def max_profit(prices):
    li=[]
    min_price=INTEGER_MAX_VALUE
    max_profit1=0
    for price in prices:
        if min_price>price:
            min_price=price
        elif max_profit1<price-min_price:
            max_profit1=price-min_price
            li.append(max_profit1)
            max_profit1=0
            min_price=price
            
            
    return sum(i for i in li)
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices)) 
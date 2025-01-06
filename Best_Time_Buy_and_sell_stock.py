INTEGER_MAX_VALUE = 2**31 - 1 
def max_profit(prices):
    min_price=INTEGER_MAX_VALUE
    max_profit1=0
    for price in prices:
        if min_price>price:
            min_price=price
        elif max_profit1<price-min_price:
            max_profit1=price-min_price
            
    return max_profit1
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices)) 
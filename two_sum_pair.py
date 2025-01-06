target_sum = 7
lit = [2, 3, 4, 1,5]
dict = {}
lit1=[]

def two_sum(target_sum):
    for num in lit:
        complement = target_sum - num
        if complement in dict:
             i=[complement, num]
             lit1.append(i)
             
        dict[num] = True
    print(lit1)

two_sum(target_sum)
def fact(y):
    if y<=1:
        return 1
    return y*fact(y-1)


def prime_no(n):
    list=[True]*(n+1)
    list[1]=list[0]=False
    for x in range(2,int(n**0.5+1)):
        for y in range(x*x,n+1,x):
            if list[y]:
                list[y]=False
    return[i for i,is_prime in enumerate(list) if is_prime]

y=int(input("Enter the number for factorial"))

n=fact(y)
print(prime_no(n))
    
    
    
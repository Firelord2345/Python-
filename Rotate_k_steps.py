k=[1,2,3,4,5,6,7]
def rotate_k(k,step):
    start=0
    end=len(k)-1
    reverse(start,end)
    reverse(start,step-1)
    reverse(step,end)
def reverse(i,j):
    temp=0
    while(i<j):
        temp=k[i]
        k[i]=k[j]
        k[j]=temp
        i+=1
        j-=1
    
rotate_k(k,3)
print(k)
n=int(input())
sum1=0
while n>0 or sum1>9:
    if n==0:
        n=sum1
        sum1=0
    else:
        sum1+=n%10
        n//=10
print(sum1)

"""Write a function that accepts three parameters: two positive integers r and unit, and a positive integer array arr of size n.

1.r represents the number of rats present in an area.

2.unit is the amount of food each rat consumes.

3.Each element of the array arr represents the amount of food present in each house,

where the index of the array corresponds to the house number.

The function should determine the minimum number of houses required to provide enough food for all the rats.

Constraints:

Return -1 if the array is null.

Return O if the total amount of food from all houses is not sufficient for all the rats.

Computed values lie within the integer range.

Example:

• Input:

r:7

unit: 2

n: 8

• arr: [2, 8, 3, 5, 7, 4, 1, 2]

• Output: 4"""

def food(r,fc,arr,n):
    if n==0:
        return -1
    fn=r*fc
    hn=0
    for i in range(n):
        hn+=arr[i]
        if hn>fn:
            return i+1
    return 0
r=int(input())
fc=int(input())
n=int(input())
arr=list(map(int,input().split()))
print(food(r,fc,arr,n))
        

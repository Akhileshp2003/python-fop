"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Input format:

The input consists of a single integer n.



Output format:

Print true if n is a power of 2, else false.



Example 1:

Input:

1

Output:

true

Explanation:

20 = 1"""

n=int(input())
if (n & n-1)==0:
  print("true")
else:
  print("false")

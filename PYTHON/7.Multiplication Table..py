## DESCRIPTION 
Multiplication Table
Given a number n, print the multiplication table from 1 to 10 for n in a single line, separated by spaces.

Examples:
Input: n = 9
Output: 9 18 27 36 45 54 63 72 81 90
## SOLUTION 
n = int(input())

# code here
for i in range (1,11):
    print(i*n,end=" ")
    

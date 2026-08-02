## DESCRIPTION 
If conditional statement- Python

You are familiar with basics of input/output and many other useful things in Python. This module is all about conditional statements like if, elif, else; for, while, etc.

In Python, any conditional statement ends with ':' (proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false

Example 1:

Input:
j_angry = True, s_angry = True
Output:
True
Explanation:
Since both of them are angry, you are in trouble.

## SOLUTION 
def friends_in_trouble(j_angry, s_angry):
    if j_angry and s_angry and True:
        return True
    if j_angry != True and s_angry != True:
        return True
    else:
        return False
        

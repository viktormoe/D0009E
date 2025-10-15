"""Someone has written a function, f, that takes a list, lst, and a value e as arguments.
Function should count and return the number of occurrences of e in lst and return the
result.
The programmer arrived at the following:"""
def f(lst, e):
    num=0
    for c in lst:
        if c==e:
            num +=1
            
    print(num)
"""The programmer made mistakes. The task is to write a corrected version. It is not allowed
to write an entirely new program; only the errors in this existing code should be corrected.
Changing the loop type is also not allowed (from while to for or vice versa)."""
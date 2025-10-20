Someone has written a function, frequency, that takes a list of numbers, lst, and a 
value x as arguments. Function should count and return the number of occurrences of x in 
lst.
Programmeraren kom fram till följande:
def frequency(lst, x):
    count=0
    i=0
    while i< len(lst):
        if lst[i]==x:
            count += 1
            i += 1
        else:
            i+=1
    print(count)
The programmer made mistakes. The task is to write a corrected version. It is not allowed 
to write an entirely new program; only the errors in this existing code should be corrected. 
Changing the loop type is also not allowed (from while to for or vice versa).

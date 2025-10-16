def replaceAll1(lst, element, replace):
    i=0
    while i<len(lst):
        if lst[i]==element:
            lst[i]=replace
        i=i+1
    return lst
lst1=[4,1,0,1]
lstA1=replaceAll1(lst1,1,9)

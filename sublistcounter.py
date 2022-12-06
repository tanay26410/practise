def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
print(sublist_counter([1,2,[1,2,3],[4,5],[6,7]]))
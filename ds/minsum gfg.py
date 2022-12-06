#minsum
def minsum(arr,n):
        if n==1:
            return arr[0]
        arr.sort()
        str1=str2=''
        for i in range(0,n,2):
            str1+=str(arr[i])
        for i in range(1,n,2):
            str2+=str(arr[i])
        return int(str1)+int(str2)

n=6
arr=[6, 8, 4, 5 ,2, 3]
print(minsum(arr,n))
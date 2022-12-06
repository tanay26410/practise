#valid palindrome1
def palindrome(s):
    a=''
    for i in s:
        if i.isalpha():
            a+=i
    b=a.lower()
    return b==b[::-1]

s = "A man, a plan, a canal: Panama"
print(palindrome(s))
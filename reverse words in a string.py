#reverse words in a string
def string(s):
    w=s.strip().split()
    w=w[::-1]
    return " ".join(w)
s=input()
print(string(s))
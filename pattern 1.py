def solve(s):
    if s.isalnum()==False:
            for i in s:
                if i.isnumeric():
                    return i
                else:
                    return i.title()
    
s = "1 w 2 r 3g"

result = solve(s)
print(result)
def solve(s):
    if s.isnumeric():
            for i in s:
                if i.isnumeric():
                    return i
                else:
                    return i.title()
    else:
        return s.title()

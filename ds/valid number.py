#valid number
def val(n):
    try:
        if 'inf'==n or 'Inf'== n:
            return False
        else:
            float(n)
    except:
        return False
    else:
        return True
n=input()
print(val(n))
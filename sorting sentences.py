#sorting sentences
def sorte(s):
    w=s.split(' ')
    w.sort(key=lambda x:x[-1])
    return ' '.join([i[:-1] for i in w])
s="is2 sentence4 This1 a3"
print(sorte(s))
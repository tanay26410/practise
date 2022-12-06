def outer(text):
    def inner():
        print(text)
    return inner
a=inner("hello")
print(a)
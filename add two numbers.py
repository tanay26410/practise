#add two numbers
def add(a,b):
    return (a+b)
t=int(input())
for i in range(t):
    a,b=input().split(',')
    print(add(int(a),int(b)))
T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = a + b
	print(ans)
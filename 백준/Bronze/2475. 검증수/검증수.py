a,b,c,d,e = input().split()
a,b,c,d,e = int(a), int(b), int(c), int(d), int(e)

print(((a*a)+(b*b)+(c*c)+(d*d)+(e*e))%10)

a = int(input())

for i in range(1, a+1):
    print(" "*(a-i), "*"*i)

a = int(input())

for i in range(1, a+1):
    print(("*"*i).rjust(a))

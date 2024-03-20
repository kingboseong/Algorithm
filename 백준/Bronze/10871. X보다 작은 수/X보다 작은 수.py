a, b = map(int,input().split())
numList = list(map(int,input().split()))
while True:
    for i in range(a):
        if numList[i] < b:
            print(numList[i])
    
    break
        

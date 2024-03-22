#여러개 출력가능하게 하는 방법 for문 안에 input을 넣기
lst = []
for i in range(9):
  lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1) #리스트의 인덱스 구하는 함수
n = int(input()) # ��� �� 
arr = list(map(int,input().split())) # ���� �ð�
arr.sort() # ����

result = 0

for i in range(1,n):
    arr[i] += arr[i-1] # ���� �ð� ����

print(sum(arr))

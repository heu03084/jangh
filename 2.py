data = input()
# ù ��° ���ڸ� ���ڷ� �����Ͽ� ����
result = int(data[0])
for i in range(1, len(data)):
# �� �� �߿��� �ϳ��� '0' Ȥ�� '1'�� ���, ���ϱ⺸�ٴ� ���ϱ� ����
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

# ���� ����Ʈ�� ��ġ �Է¹ޱ�
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ����Ʈ�� �̵��� �� �ִ� 8���� ���� ����
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 8���� ���⿡ ���Ͽ� �� ��ġ�� �̵��� �������� Ȯ��
result = 0
for step in steps:
# �̵��ϰ��� �ϴ� ��ġ Ȯ��
    next_row = row + step[0]
    next_column = column + step[1]
# �ش� ��ġ�� �̵��� �����ϴٸ� ī��Ʈ ����
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)

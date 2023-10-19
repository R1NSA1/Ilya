# 5.1
max_val = int(input("Введите первое целое число: "))
repeat = int(input("Введите второе целое число: "))
s1 = []
for s in range(1, int(max_val) + 1):
    s1.append(int(s))
if len(s1 * int(repeat)) == repeat ** 2:
    s2 = s1 * int(repeat)
    print(s2)
# 5.2
    s3 = s2.copy()

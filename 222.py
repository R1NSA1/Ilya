from random import randint
print('  ' + 'a', ' ' + 'b', ' ' + 'c', ' ' + 'd', ' ' + 'e', ' ' + 'f', ' ' + 'g', ' ' + 'h')
p = [[], [], [], [], [], [], [], []]
for el in p:
    for i in range(8):
        el.append(randint(0, 1))


for idx, i in enumerate(p):
    print((chr(ord('1') + idx)) + str(i))
x = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
y = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}


arr = []
def play():
    a = ""
    while a != "Игрок 1 победил" and a != "Игрок 2 победил":
        if 1 in p[0] or 1 in p[1] or 1 in p[2] or 1 in p[3] or 1 in p[4] or 1 in p[5] or 1 in p[6] or 1 in p[7]:
            print("\nИгрок 1 вводит координаты")
            letter = input()
            f(letter)
            arr.append(1)
        if 1 in p[0] or 1 in p[1] or 1 in p[2] or 1 in p[3] or 1 in p[4] or 1 in p[5] or 1 in p[6] or 1 in p[7]:
            print("\nИгрок 2 вводит координаты")
            letter = input()
            f(letter)
            arr.append(2)
        else:
            if arr[-1] == 1:
                a = "Игрок 1 победил"
            else:
                a = "Игрок 2 победил"
        print(a)


def f(letter):
    string_1 = "abcdefgh"
    string_2 = "12345678"
    if letter in string_1:
        for n in p:
            n[x[letter]] = 0
    if letter in string_2:
        p[y[letter]] = [0] * 8

    print('  ' + 'a', ' ' + 'b', ' ' + 'c', ' ' + 'd', ' ' + 'e', ' ' + 'f', ' ' + 'g', ' ' + 'h')
    for index, n in enumerate(p):
        print((chr(ord('1') + index)) + str(n))
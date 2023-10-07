from random import choice                                                   #Импортируем функцию, которая рандомно выбирет одну цифру.
z = '0123456789'                                                            #Создаем строку со всеми цифрами.
x = choice(z[1:10])                                                         #Создаем строку из одной рандомной цифры (не включая 0).
for i in range(3):                                                          #Для цикла из 3 повторений:
    z = ''.join(z.split(x[i]))                                              #Удаляем из строки z цифру, добавленную в строку x.
    x += choice(z)                                                          #Снова добавляем в строку x рандомную цифру из z.
n = 0                                                                       #Создаем счётчик ходов.
while True:                                                                 #Цикл выполняется до тех пор, пока истинно:
    y = input("Введите четырёхзначное число: ")                             #Функция ввода своего 4-значного числа.
    n += 1                                                                  #Увеличиваем счётчик ходов на 1.
    b = 0                                                                   #Задаем переменную для Bulls и Cows
    c = 0
    for i in range(4):                                                      #Для цикла из 4 повторений:
        if x[i] == y[i]:                                                    #Проверка, стоит ли цифра на своём месте.
            b += 1                                                          #Если да, то +1 к быкам.
        elif y[i] in x:                                                     #Если нет, проверка, есть ли цифра в загаданном числе.
            c += 1                                                          #Если да, то +1 к коровам.
    print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')
    if b == 4:                                                              #Если число угадано (найдено 4 быка)
        print('Вы победили за', n, 'ходов')                                 #Вывод победы
        break
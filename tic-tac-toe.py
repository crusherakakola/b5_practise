import re
turn_cnt = 0
playing_field = [[' ',0,1,2],
          [0,'-','-','-'],
          [1,'-','-','-'],
          [2,'-','-','-']]
def diag_check(x=3,y=1):
    if playing_field[x][y] == xo:
        diag_cntr[1] += 1
    if x <= 1:
        return
    return diag_check(x-1,y+1)
def field_rendering():
    for i in range(len(playing_field)):
        print(playing_field[i][0],playing_field[i][1],playing_field[i][2],playing_field[i][3])
def turn(xo):
    print(f'\nХодит {xo.upper()}\n')
    x, y = input('Введите номер строки:\n'), input('Введите номер колонки:\n')
    while not re.fullmatch('\d', x):
        field_rendering()
        print('\nВы ввели некорректное значение!\n')
        x, y = input('Введите номер строки:\n'), input('Введите номер колонки:\n')
    x, y = int(x), int(y)
    while x > 2 or y > 2 or x < 0 or y < 0:
        field_rendering()
        print('\nВы ввели несуществующее значение!\n')
        x, y = input('Введите номер строки:\n'), input('Введите номер колонки:\n')
        while not re.fullmatch('\d', x):
            field_rendering()
            print('\nВы ввели некорректное значение!\n')
            x, y = input('Введите номер строки:\n'), input('Введите номер колонки:\n')
        x, y = int(x), int(y)
    print()
    if playing_field[x + 1][y + 1] == '-':
        playing_field[x + 1][y + 1] = xo
    else:
        print('Выбранное вами поле уже занято!\n')
        global turn_cnt
        turn_cnt -= 1
while True:
    field_rendering()
    if turn_cnt % 2 == 0:
        xo = 'x'
        turn(xo)
        turn_cnt += 1
    else:
        xo = 'o'
        turn(xo)
        turn_cnt += 1
    vert_cntr = [0, 0, 0]
    hor_cntr = [0, 0, 0]
    diag_cntr = [0, 0]
    diag_check()
    for i in range(1, 4):
        if playing_field[i][i] == xo:
            diag_cntr[0] += 1
        for j in range(1, 4):
            if playing_field[i][j] == xo:
                vert_cntr[j - 1] += 1
                hor_cntr[i - 1] += 1
    if 3 in vert_cntr or 3 in hor_cntr or 3 in diag_cntr:
        print()
        field_rendering()
        print(f'\nПобедил {xo.upper()}!')
        break
    if '-' not in playing_field[1] and '-' not in playing_field[2] and '-' not in playing_field[3]:
        print()
        field_rendering()
        print('\nНичья!')
        break








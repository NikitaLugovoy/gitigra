import random
class Werio:
    def __init__(self, name, xp = 100):
        self.name = name
        self.xp = xp
        print('Вы создали бойца {} с количеством хп 100'.format(self.name))

    def udar(self , wrag):
        if True:
            print('Боец {} нанёс удар своему сопернику {}'.format(self.name, wrag.name))
            wrag.ostxp(
                wrag.polxp() - random.randint(0, 30)
            )
        else:
            print('Некорректроне хп {}'.format(wrag.name))
            print(type(wrag.polxp()))

    def ostxp(self, xp):
        self.xp = xp
        if xp > 0 :
            print('У бойца {} осталось {}'.format(self.name, self.xp))
        else:
            print('У бойца {} нет хп'.format(self.name))

    def polxp(self):
        try:
            return self.xp
            print('XP {} - {}'.format(self.name,self.xp))
        except:
            return 'ХП net'


print('Введите имя своего бойца: ')
name1 = input()
unit1 = Werio(name1, 100)

print('Если вы хотите сразиться против обычного игрока, то введите 1 , если хотите сразиться с боссом, то введите любое друге число')
viborIgri = int(input())
if viborIgri == 1:

    print('Введите имя второга бойца: ')
    name2 =input()
    unit2 = Werio(name2, 100)

    print("НАЧАЛО ИГРЫ!!!")
    while (unit1.xp > 0) and (unit2.xp > 0):
        raund = random.randint(1,2)
        if raund == 1 :
            unit1.udar(unit2)
        else:
            unit2.udar(unit1)

    if raund == 1:
        name = unit1.name
        wrageskname = unit2.name
    else:
        name = unit2.name
        wrageskname = unit1.name

    print('{} ПОБЕДИЛ ИГРОКА {}'.format(name, wrageskname))

else:
    print('Выходит БОСС:...\n...\n...\n Выходит староста ИВТ-201 (Рябцев Николай, ему предоставляется первый ход:')
    print(' ТЫ В ЧЁРНОМ СПИСКЕ!!!\n это -1000 хп из 100\n GAME OVER')


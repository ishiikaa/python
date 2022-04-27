def switch_veer(ishika):
    love = {
        1: 'vivu',
        2: 'vinki',
        3: 'vivu',
        4: 'veeru',
        5: 'jiya',
        6: 'jiyu',
        7: 'jiyoske',
        8: 'king',
        9: 'jiye west',
        10: 'food eating penguin'
    }
    return love.get(ishika, "invalid name")
a = int(input("enter no.: "))
print(switch_veer(a))
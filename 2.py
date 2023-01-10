n = int(input('Введите число -> '))
list = [n]

def prostye_mnozhitely(list):
    m = 0
    for i in range(list[-1] // 2, 1, -1):
        if list[len(list)-1] % i == 0:
            list.append(i)
            list[-2] = list[-2] // i              
            m += 1

    if m != 0:
        prostye_mnozhitely(list)

prostye_mnozhitely(list)
    
print(list)
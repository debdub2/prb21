def possibility(y):       #Данная функция ввсчитывает возможность попасть в ячейку y при заданных условиях
    x = a[0]
    while x < t:
        x += a[x-1]
    if x == t:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    n=int(input()) #А ещё я не смог разобраться, как организовать в Python ввод в одну строку
    t=int(input())
    a=[0]*(n-1) #Создаём массив с числами ai
    for i in range(n-1):
        a[i]=int(input()) #Заполняем его данными необходимыми числами
    if possibility(t) == True:  #Вызываем функцию и высчитываем возможность оказаться в ячейке t
        print('Yes')
    else:
        print('No')

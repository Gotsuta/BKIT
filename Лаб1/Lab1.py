import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = float(coef_str)

        return coef
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
        try:
            coef = float(coef_str)
            return coef
        except:
            return math.inf
        


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        timeroot = -b / (2.0*a)
        if timeroot==0.0:
            result.append(timeroot)
        elif timeroot>0.0:
            root1=math.sqrt(timeroot)
            root2=-math.sqrt(timeroot)
            result.append(root1)
            result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        timeroot1 = (-b + sqD) / (2.0*a)
        timeroot2 = (-b - sqD) / (2.0*a)
        if timeroot1==0.0:
            result.append(timeroot1)
        elif timeroot1>0.0:
            root1=math.sqrt(timeroot1)
            root2=-math.sqrt(timeroot1)
            result.append(root1)
            result.append(root2)
        if timeroot2==0.0:
            result.append(timeroot2)
        elif timeroot2>0.0:
            root1=math.sqrt(timeroot2)
            root2=-math.sqrt(timeroot2)
            result.append(root1)
            result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a=math.inf
    b=math.inf
    c=math.inf
    while a==math.inf or a==0:
        a = get_coef(1, 'Введите коэффициент А:')
    while b==math.inf:
        b = get_coef(2, 'Введите коэффициент B:')
    while c==math.inf:
        c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: x1={}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: x1={}; x2={}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: x1={}; x2={}; x3={}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: x1={}; x2={}; x3={}; x4={}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4

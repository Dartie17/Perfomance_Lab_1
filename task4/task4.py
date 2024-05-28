# Нахождение минимального количества шагов для приведение всех чисел массива к одному числу
# В качестве аргументов принимает файл с числами массива

from statistics import median

def bring_same_num(num_file):
    n = open(num_file)
    num_list = [int(line.strip()) for line in n]
    n.close()

    med = median(num_list)

    steps = int(sum(abs(num - med) for num in num_list))

    print(steps)


bring_same_num(input())
# Путь интервала по круговому массиву
# В качестве аргумента принимает ввод двух чисел через пробел

def find_path(arg):

    n, m = arg.split()
    n, m = int(n), int(m)

    numbers = [i for i in range(1, n + 1)]
    full_path = [[0]]
    step = 0
    path = []

    while full_path[-1][-1] != 1:
        interval = []
        for _ in range(m):
            interval.append(numbers[step])
            step += 1
            if step == n:
                step = 0
        step -= 1
        path.append(str(interval[0]))
        full_path.append(interval)

    print(''.join(path))


find_path(input())
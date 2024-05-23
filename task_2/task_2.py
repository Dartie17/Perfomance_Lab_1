# Расчет положения точек относительно окружности
# В качестве аргументов принимает файл с координатами и радиусом окружности и файл с координатами точек

def dots_laying_circle(circle_file, dots_file):
    c = open(circle_file)
    circle_list = [line.strip() for line in c]
    c.close()

    circle_x, circle_y = int(circle_list[0][0]), int(circle_list[0][2])
    circle_r = int(circle_list[1][0])

    d = open(dots_file)
    dots_list = [line.strip() for line in d]
    d.close()

    for i in range(len(dots_list) - 1):
        dot_x, dot_y = int(dots_list[i][0]), int(dots_list[i][2])
        if (circle_x - dot_x) ** 2 + (circle_y - dot_y) ** 2 <= circle_r:
            print(1)
        if (circle_x - dot_x) ** 2 + (circle_y - dot_y) ** 2 >= circle_r:
            print(2)
        else:
            print(0)


dots_laying_circle('circle.txt', 'dots.txt')
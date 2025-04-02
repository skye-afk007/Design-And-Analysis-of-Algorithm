def dda_algorithm(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = dx if abs(dx) > abs(dy) else abs(dy)

    
    x_increment = dx / steps
    y_increment = dy / steps

    
    x, y = x1, y1
    points = []
    for i in range(steps + 1):
        points.append((int(x + 0.5), int(y + 0.5))) 
        x += x_increment
        y += y_increment

    return points


x1, y1 = 5, 7
x2, y2 = 10, 15

points = dda_algorithm(x1, y1, x2, y2)
for point in points:
    print(point)
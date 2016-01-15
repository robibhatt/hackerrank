def get_distance((a,b), (c,d)):
    return ((a-c)**2 + (b-d)**2)**(0.5)

x_plus = None
y_plus = None
x_minus = None
y_minus = None

N = int(raw_input())
for i in range(N):
    [x, y] = [int(i) for i in raw_input().split(' ')]
    if y_plus == None:
        y_plus = y
    if y > y_plus:
        y_plus = y
    if y_minus == None:
        y_minus = y
    if y < y_minus:
        y_minus = y
    if x_plus == None:
        x_plus = x
    if x > x_plus:
        x_plus = x
    if x_minus == None:
        x_minus = x
    if x < x_minus:
        x_minus = x

points = [(x_minus, 0), (x_plus, 0), (0, y_minus), (0, y_plus)]
max_distance = 0
for i in range(3):
    for j in range(4)[(i+1):]:
        if get_distance(points[i], points[j]) > max_distance:
            max_distance = get_distance(points[i], points[j])
print "%.15f" % max_distance
        
    


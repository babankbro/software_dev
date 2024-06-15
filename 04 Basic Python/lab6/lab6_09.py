f = open("lab6/DM.csv", 'r')
lines = f.readlines()
DM = []
for i in range(len(lines)):
    line = lines[i]
    line = line.replace("\n", '')
    line = line.replace("\t", '')
    data = line.split(',')
    numbers = []
    for d in data:
        numbers.append(float(d))
    DM.append(numbers)
    
def distane_route(route, DM):
    total = 0
    N = len(route)
    for i in range(N-1):
        current = route[i]
        next_city = route[i+1]
        total += DM[current][next_city]
    current = route[N-1]
    next_city = route[0]
    total += DM[current][next_city]
    return total
        
route = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
total_distance = distane_route(route, DM)
print("Distance: T1->T2->T3->T4->T5->T6->T7->T8->T9->T10->T1:")
print(total_distance)
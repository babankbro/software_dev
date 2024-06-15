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
    
for row in DM:
    print(row)

#"T8" -> 7
print("T8->T9: ", DM[7][8] )
print("T9->T10 :", DM[8][9] )
print("T8->T9->T10 :", DM[7][8] + DM[8][9] )
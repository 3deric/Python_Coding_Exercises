values = [30,24,12,50,11,49,11,5,2,5,7,55,100,0,7,2,1,1000,200,500,1242]

def insertionsort(values):
    for i in range(len(values)):
        j = i
        while (j > 0) and values[j] < values[j -1]:
            temp = values[j]
            values[j] = values[j - 1]
            values[j - 1] = temp
            j = j - 1
    return values

print(insertionsort(values))
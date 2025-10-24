values = [30,24,12,50,11,49,11,5,2,5,7,55,100,0,7,2,1,1000,200,500,1242]

def selectionsort(values):
    for i in range(len(values) - 1):
        smallsub = i
        for j in range(i + 1, len(values)):
            if values[j] < values[smallsub]:
                smallsub = j
        temp = values[i]
        values[i], values[smallsub] = values[smallsub], temp
    return values

print(selectionsort(values))
values = [30,24,12,50,11,49,11,5,2,5,7,55,100,0,7,2,1]

def bubblesort(values):
    for i in range(len(values) - 2):
        for j in range(len(values) -1):
            if values[j] > values[j+1]:
                temp = values[j]
                values[j], values[j+1] = values[j+1], values[j]
    return values

print(bubblesort(values))
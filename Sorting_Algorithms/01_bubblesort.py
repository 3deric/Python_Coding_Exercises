values = [30,24,12,50,11,49,11,5,2,5,7,55,100,0,7,2,1]


def bubblesort(values):
    for i in range(len(values) - 1):
        for j in range(len(values) -1 - i):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                print(values)
    return values

print(bubblesort(values))
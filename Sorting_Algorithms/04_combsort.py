import math

values = [30,24,12,50,11,49,11,5,2,5,7,55,100,0,7,2,1,1000,200,500,1242]

def combsort(values):
    gap = len(values)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = math.floor(gap/ shrink)
        if gap < 1:
            gap = 1
            sorted = True
        elif gap == 9 or gap == 10:
            gap = 11
        i = 0
        while i + gap < len(values):
            if values[i] > values[i + gap]:
                values[i], values[i + gap] = values[i + gap], values[i]
                sorted = False
            i += 1
    return values

print(combsort(values))

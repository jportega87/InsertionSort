import random

def insertionSort(arr):

    value = 0

    for i in range(1, len(arr)):
        value = arr[i]
        for j in xrange(i-1, -1, -1):
            if value < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = value
    return arr

count = 0
x = []

while count < 10:
    x.append(random.randint(0, 10000))
    count += 1

x = insertionSort(x)
print x

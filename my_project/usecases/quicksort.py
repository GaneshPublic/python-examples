# call this to execute sorting
def sort(input):
    return quicksort(input, 0, len(input)-1)

def quicksort(input, l, h):
    if len(input) == 1:
        return input

    if l < h:
        pivot = partition(input, l, h)
        quicksort(input, l, pivot -1)
        quicksort(input, pivot + 1, h)

def partition(input, l, h):
    i = l-1
    pivot = input[h]

    for j in range(l, h):
        if input[j] <= pivot:
            i += 1
            input[i], input[j] = input[j], input[i]

    input[i+1], input[h] = input[h], input[i+1]
    return (i+1)
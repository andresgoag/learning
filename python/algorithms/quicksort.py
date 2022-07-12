def  quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)



print(quick_sort([1,2,5,5,5,5,5,5,5,5,5,5,5,5,5,90984,1992093,6,3,2,3,8,5]))
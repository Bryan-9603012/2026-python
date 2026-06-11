# sorts.py

def _validate_list(data):
    if not isinstance(data, list):
        raise TypeError("data must be a list")


def bubble_sort(data: list) -> list:
    _validate_list(data)

    result = data.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def quick_sort(data: list) -> list:
    _validate_list(data)

    if len(data) <= 1:
        return data.copy()

    pivot = data[0]
    left = []
    middle = []
    right = []

    for item in data:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            middle.append(item)

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(data: list) -> list:
    _validate_list(data)

    if len(data) <= 1:
        return data.copy()

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
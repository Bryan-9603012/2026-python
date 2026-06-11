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

def builtin_sorted(data: list) -> list:
    _validate_list(data)

    return sorted(data)


def optimized_quick_sort(data: list) -> list:
    _validate_list(data)

    result = data.copy()
    _optimized_quick_sort_in_place(result, 0, len(result) - 1)
    return result


def _optimized_quick_sort_in_place(data: list, low: int, high: int) -> None:
    while low < high:
        if high - low <= 16:
            _insertion_sort_range(data, low, high)
            return

        pivot_index = _median_of_three(data, low, high)
        data[pivot_index], data[high] = data[high], data[pivot_index]

        partition_index = _partition(data, low, high)

        left_size = partition_index - low
        right_size = high - partition_index

        if left_size < right_size:
            _optimized_quick_sort_in_place(data, low, partition_index - 1)
            low = partition_index + 1
        else:
            _optimized_quick_sort_in_place(data, partition_index + 1, high)
            high = partition_index - 1


def _median_of_three(data: list, low: int, high: int) -> int:
    mid = (low + high) // 2

    a = data[low]
    b = data[mid]
    c = data[high]

    if a <= b <= c or c <= b <= a:
        return mid
    if b <= a <= c or c <= a <= b:
        return low
    return high


def _partition(data: list, low: int, high: int) -> int:
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def _insertion_sort_range(data: list, low: int, high: int) -> None:
    for i in range(low + 1, high + 1):
        key = data[i]
        j = i - 1

        while j >= low and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

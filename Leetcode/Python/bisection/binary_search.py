from typing import Union, Literal

def binary_search(array: list[int], target: int) -> Union[int, Literal[-1]]:
    """
    Search for a target index in log n time complexity.
    In case the target value occurs more than once, this binary search algorithm will find it
    but it's not guaranteed to be either left-most or right-most element.
    """
    left, right = 0, len(array) - 1
    while left <= right:  # Both inclusive, thus need `<=` here.
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1  # New search space [lo, mid - 1].
        else:
            left = mid + 1  # New search space [mid + 1, hi].
    return -1
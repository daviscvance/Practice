from typing import Union, Literal

def bisect_right(array: list[int], target: int) -> Union[int, Literal[-1]]:
    """
    Returns the idx such that arr[:idx] <= t (and arr[idx:] > t)
        i.e. the smallest idx such that the criterion is False
        e.g.    arr :     [2, 3, 5, 4, 6, 7, 7, 7, 7, 8, 9]
        arr[idx] <= 7 :   [T, T, T, T, T, T, T, T, T, F, F]
                                               return 9
    we have to find the largest index where the element is less than OR equal to (<=) the target:
        1) to find the index JUST AFTER the right most index when a target is present in the array,
           hence if required, the right most index of target can finally be obtained by modifying
           the below return statement to `left - 1`
        2) OR where it can be inserted (in case target is absent from array - generates same result
           as bisect_left).
    """
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1  # New search space [mid + 1, hi).
        else:
            right = mid  # New search space [lo, mid).
    return left

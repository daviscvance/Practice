from typing import Union, Literal

def bisect_left(array: list[int], target: int) -> Union[int, Literal[-1]]:
    """
    Returns the idx such that arr[:idx] < t (and arr[idx:] >= t)
        i.e. the largest idx such that the criterion is False
        e.g.    arr :     [2, 3, 5, 4, 6, 7, 7, 7, 7, 8, 9]
        arr[idx] < 7 :    [T, T, T, T, T, F, F, F, F, F, F]
                                   return 5
    We have to find the largest index where the element is STRICTLY less than (<) the target:
        1) to find the left most index when a target is present in the array
        2) OR where it can be inserted (in case target is absent from array - generates same result
           as bisect_right).
    """
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < target:
            # Since we're looking for the first index at which the IF condition fails; Therefore
            # if is still being satisfied we need to shift the lower bound of the search space to
            # disregard the mid point AS WELL AS all indices to the left of it (since those indices
            # would also satisfy the IF condition).
            left = mid + 1  # New search space [mid + 1, hi).
        else:
            # However, if we encounter an index at which the IF condition fails, then the FIRST
            # index at which the condition fails certainly couldn't be AFTER the mid point since
            # the midpoint already fails the IF condition; there is of course the possibility that
            # the first index that fails the IF condition lies BEFORE the mid point: therefore to
            # cover that scenario we'll set the upper bound of our search space to the mid point and
            # check whether indices prior to it FAIL the IF condition.
            right = mid  # New search space [lo, mid).
    return left  # At point of exiting while loop left or right are the same so can return either.

print(bisect_left([2, 3, 5, 4, 6, 7, 7, 7, 7, 8, 9], 7))

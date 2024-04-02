# 4. Median of Two Sorted Arrays
# Hard
# Array, Binary Search, Divide and Conquer
# https://leetcode.com/problems/median-of-two-sorted-arrays
#
# Return the median of two sorted arrays with run time of O(log m + n).
# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50

from typing import List


class Solution:
    # Bisection | Time: O(log m + log n) / O(log(m*n)) | Space: O(log m*n)
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        nA, nB = len(A), len(B)

        def getKth(
                k: int,  # Median to find.
                # These variables represent the beginning and end of the search space in binary search
                # in accordance to the A and B arrays.
            start_A: int = 0,
                end_A: int = nA - 1,
                start_B: int = 0,
                end_B: int = nB - 1):
            '''
            Performs binary search recursively on 2 sorted arrays. The idea is to imagine they are
            being operated on as if they were already joined together. But without actually joining,
            we cant fully know where the median is, so by process of elimination, we come to a
            conclusion of where it has to be by recursively constraining the search space.
            '''
            # If either passed array is empty, directly take the median of an existing array.
            if start_A > end_A and start_B <= end_B:
                return B[k - start_A]
            if start_A <= end_A and start_B > end_B:
                return A[k - start_B]

            # Estimate where the actual median could be based on the medians of the two arrays.
            index_A, index_B = (start_A + end_A) // 2, (start_B + end_B) // 2
            value_A, value_B = A[index_A], B[index_B]
            if index_A + index_B < k:  # Kth element is higher than current indices, revise up.
                if value_A > value_B:  # B is smaller, push B search space up.
                    return getKth(k, start_A, end_A, index_B + 1, end_B)
                else:  # A is smaller, push A search space up.
                    return getKth(k, index_A + 1, end_A, start_B, end_B)
            else:  # Kth element in full array is smaller than current indices, revise down.
                if value_A > value_B:  # A is larger, push A search space down.
                    return getKth(k, start_A, index_A - 1, start_B, end_B)
                else:  # B is larger, psuh B search space down to find K.
                    return getKth(k, start_A, end_A, start_B, index_B - 1)

        combined_len = nA + nB
        median = combined_len // 2
        # Manage the difference between an even and odd joined array.
        if combined_len % 2 == 0:  # Even total.
            # Average between elements left and right of the median.
            return (getKth(median) + getKth(median - 1)) / 2
        else:  # Odd total, can take the median directly.
            return getKth(median)

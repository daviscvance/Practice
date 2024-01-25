# 4. Median of Two Sorted Arrays
# Hard
# Array, Binary Search, Divide and Conquer
# https://leetcode.com/problems/median-of-two-sorted-arrays
#
#
# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        def getKth(
            k: int,  # Median to find.
            # These variables represent the beginning and end of the search space in binary search
            # in accordance to the nums1 and nums2 arrays.
            start1: int = 0,
            end1: int = len1 - 1,
            start2: int = 0,
            end2: int = len2 - 1):
            '''
            Performs binary search recursively on 2 sorted arrays. The idea is to imagine they are
            being operated on as if they were already joined together. But without actually joining,
            we cant fully know where the median is, so by process of elimination, we come to a
            conclusion of where it has to be.
            '''
            # If either passed array is empty (i.e. []), directly take the median of an existing array.
            if start1 > end1 and start2 <= end2:
                return nums2[k]
            elif start1 <= end1 and start2 > end2:
                return nums1[k]
            
            # Estimate where the actual median could be based on the medians of the two arrays.
            median1, median2 = (end1 - start1) // 2, (end2 - start2) // 2
            

        combined_len = len1 + len2
        median = combined_len // 2

        # Manage the difference between an even and odd joined array.
        if combined_len % 2 == 0:  # Even total.
            # Average between elements left and right of the median.
            return (getKth(median) + getKth(median + 1)) / 2
        else:  # Odd total, can take the median directly.
            return getKth(median)


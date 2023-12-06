def two_sum_optimized(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum_optimized(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(two_sum_optimized(nums2, target2))  

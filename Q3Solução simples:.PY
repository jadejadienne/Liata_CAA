def two_sum_simple(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

# Exemplo de uso
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum_simple(nums1, target1))  # Saída: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(two_sum_simple(nums2, target2))  # Saída: [1, 2]

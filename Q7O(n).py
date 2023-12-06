def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1
    
    while left <= right:
        left_square, right_square = nums[left] ** 2, nums[right] ** 2
        
        if left_square >= right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1
        
        index -= 1
    
    return result

nums = [-4, -1, 0, 3, 10]
resultado = sortedSquares(nums)
print(resultado)

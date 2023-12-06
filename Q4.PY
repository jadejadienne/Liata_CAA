def majority_element(nums):
   
    candidate, count = None, 0
    
    # Iterar sobre o array
    for num in nums:
    
        if count == 0:
            candidate = num
        
        
        count += (1 if num == candidate else -1)
    
    return candidate

nums1 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums1))  

nums2 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(nums2))  

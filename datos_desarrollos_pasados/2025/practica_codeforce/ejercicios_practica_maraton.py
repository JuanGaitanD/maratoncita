def maxSubArray(nums) -> int:
    max_sum = max(nums)

    j = len(nums)    
    
    for i in range(len(nums)):
        temp = 0
        temp_i = i
        array_temp = []

        while i < j:
            temp += nums[i]
            array_temp.append(temp)

            i+=1
        
        i = temp_i
        
        if max_sum < max(array_temp):
            max_sum = max(array_temp)
    
    return max_sum

# def maxSubArray(nums):
#     maxSum = nums[0]
#     curSum = 0

#     for n in nums:
#         curSum = max(curSum, 0)
#         curSum += n
#         maxSum = max(maxSum, curSum)
#     return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))


# https://neetcode.io/courses/advanced-algorithms/0
# https://leetcode.com/problems/maximum-subarray
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:

    num_to_index = {} 
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return []	
	
nums = [int(num) for num in input("nums: ").split(',')]
target = int(input("target: "))

result = twoSum(nums, target)
if result:
    print(result)
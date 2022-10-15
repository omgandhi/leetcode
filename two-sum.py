# 1
# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    nums_index = [(v, index) for index, v in enumerate(nums)]
    print(nums_index)
    nums_index.sort()
    begin, end = 0, len(nums) - 1
    while begin < end:
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target:
            return [nums_index[begin][1], nums_index[end][1]]
        elif curr < target:
            begin += 1
        else:
            end -= 1


input_list = [2, 8, 12, 15]
print(twoSum(input_list, 20))

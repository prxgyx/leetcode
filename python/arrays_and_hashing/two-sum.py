class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val -> index
        # lookup_dict = dict((v,k) for k, v in enumerate(nums))
        # return next(((i, lookup_dict.get(target-v)) for i,v in enumerate(nums) if lookup_dict.get(target-v, i)!=i), None)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[num] = i

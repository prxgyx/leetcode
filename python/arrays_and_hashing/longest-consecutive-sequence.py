class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashSet = set(nums)
        
        for num in nums:
            # check if its the start of a seq
            if num-1 not in hashSet:
                length = 0
                while num+length in hashSet:
                    length += 1
                longest = max(length, longest)
                
        return longest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        
        first_idx, last_idx = 0, len_nums-1
        
        while first_idx <= last_idx:
            middle_idx = (first_idx + last_idx) // 2
            print(middle_idx)
            if target == nums[middle_idx]:
                return middle_idx
            elif target < nums[middle_idx]:
                last_idx = middle_idx - 1
            else:
                first_idx = middle_idx + 1
        return -1

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l,r=0,0
        max_length=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            max_length = max(max_length, r-l+1)
        return max_length 
            
            
    # O(n^2)
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     max_len_substring = len(set(s))
    #     length_string = len(s)
    #     len_substring = 0
    #     for start_idx in range(0, length_string):
    #         for end_idx in range(start_idx+1, start_idx+1+max_len_substring):
    #             temp_substring = s[start_idx:end_idx]
    #             len_temp_substring = len(temp_substring)
    #             if len_temp_substring == len(set(temp_substring)) and len_temp_substring > len_substring:
    #                 len_substring = len_temp_substring
    #                 if len_substring == max_len_substring:
    #                     return len_substring
    #     return len_substring
                

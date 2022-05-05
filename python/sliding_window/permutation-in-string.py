from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        l,r=0,0
        s1_count_map = defaultdict(int)
        
        for x in s1:
            s1_count_map[x] +=1
        
        temp_counter = defaultdict(int)

        while r < len(s2):
            temp_counter[s2[r]]+=1
            # print(l,r,temp_counter)
            if r-l+1 == len(s1):
                
                if temp_counter == s1_count_map:
                    return True
                else:
                    if temp_counter[s2[l]] == 1:
                        del temp_counter[s2[l]]
                    else:
                        temp_counter[s2[l]]-=1
                    l+=1
                    r+=1
            elif r-l+1 < len(s1):
                r+=1
            
        return False
                
        

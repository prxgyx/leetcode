from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finaldict = defaultdict(list)
        
        if len(strs) == 1:
            return [[strs[0]]]
        
        for s in strs:
            hashlist = [0] * 26
            for char in s:
                hashlist[ord(char) - ord("a")] += 1
            finaldict[tuple(hashlist)].append(s)
            # print(finaldict)
        
        return finaldict.values()


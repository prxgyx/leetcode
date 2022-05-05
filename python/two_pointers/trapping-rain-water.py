class Solution:
    def trap(self, height: List[int]) -> int:
        
        length = len(height)
        maxleft = [0]*length
        maxright = [0]*(length+1)
        minheight = [0]*length
        res=0

        for i in range(length-1, -1, -1):
            maxright[i] = max(maxright[i+1], height[i])
        for i in range(length):
            maxleft[i] = max(maxleft[i-1], height[i])
            minheight[i] = min(maxleft[i], maxright[i])
            units=minheight[i] - height[i]
            if units<0:
                units=0
            res+=units
        
        return res

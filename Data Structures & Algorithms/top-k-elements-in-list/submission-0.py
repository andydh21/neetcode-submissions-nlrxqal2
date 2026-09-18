class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped = {}
        for i in nums:
            if i in grouped: 
                grouped[i] += 1
            
            else:
                grouped[i] =  1
        
        res = [] 
        for key, value in sorted(grouped.items(), key=lambda item: item[1], reverse=True)[:k]:
            res.append(key)

        return res
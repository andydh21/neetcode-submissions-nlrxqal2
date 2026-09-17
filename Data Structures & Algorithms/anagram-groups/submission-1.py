class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        # sorted each string then used them as keys 
        # stored values as an array
        for i in strs:
            tmp = list(i)
            tmp.sort()
            tmp = "".join(tmp)

            if tmp not in grouped.keys():
                grouped[tmp] = [i]
            
            else:
                grouped[tmp].append(i)
            

        res = [] 
        for value in grouped.values(): 
            res.append(value)


        return res
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = {}

        for i in range(len(strs)):
            string = strs[i]
            sorted_str = ''.join(sorted(string))

            if sorted_str not in sortedStrs:
                sortedStrs[sorted_str] = []
            
            sortedStrs[sorted_str].append(string)

        res = []
        for sorted_str in sortedStrs:
            res.append(sortedStrs[sorted_str])

        return res
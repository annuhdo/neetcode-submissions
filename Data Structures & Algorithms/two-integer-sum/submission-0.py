class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locations = {} # val -> index with later val replacing hashmap
        for i in range(len(nums)):
            locations[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in locations:
                if locations[target - nums[i]] == i:
                    continue
                
                return [i, locations[target - nums[i]]]

        return []
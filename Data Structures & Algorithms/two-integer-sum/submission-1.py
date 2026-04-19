class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevLocations = {} # val -> index only populated with past values
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevLocations:
                return [prevLocations[diff], i]

            prevLocations[nums[i]] = i
        

        return []
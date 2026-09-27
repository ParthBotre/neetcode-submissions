class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #[3,4,5,6]
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[n]=i

        



        
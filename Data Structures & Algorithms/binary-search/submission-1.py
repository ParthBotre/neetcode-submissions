class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums [1,2,3,4,5] target is 4
        #left and right = 0, len(nums)-1
        # mid = left + right // 2; mid = 3 but at index 2
        #[1] left <= right ; 0 = 0
        # left = mid + 1


        left , right = 0, len(nums)-1
        

        while left <= right:
            mid = (left + right)//2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: 
                return mid
        else:
            return -1
            










        
        
        
        
        
        
        
        
        
        
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1

        
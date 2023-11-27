class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        for i in range(len(self.nums)):
            for n in range(i+1,len(self.nums)):
                if self.nums[i]+self.nums[n]==self.target:
                    return [i,n]
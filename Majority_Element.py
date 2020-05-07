class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for x in nums:
            if (nums.count(x)>=(len(nums)//2)+1) and len(nums)%2==1:
                return(x)
            elif (nums.count(x)>=len(nums)//2) and len(nums)%2==0:
                return x
            else:
                for y in range(nums.count(x)):
                    nums.remove(x)

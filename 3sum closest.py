class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        mindiff=100000
        res=0
        for i in range(len(nums)):
            left=i+1; right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                diff=abs(sum-target)
                if diff<mindiff: mindiff=diff; res=sum
                if sum==target: return sum
                elif sum<target: left+=1
                else: right-=1
        return res
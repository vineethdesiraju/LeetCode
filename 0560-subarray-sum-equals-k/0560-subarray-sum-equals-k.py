class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k=p[j]-p[i-1] -> p[j]-k=p[i-1]
        d={0:1}
        count=0
        prefix_sum=0
        for num in nums:
            prefix_sum+=num
            if (prefix_sum -k) in d:
                count+=d[prefix_sum -k]
            if prefix_sum in d:
                d[prefix_sum]+=1
            else:
                d[prefix_sum]=1
        return(count)

        
        
        
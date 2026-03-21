class Solution {
    public int jump(int[] nums) {
        int finaljumps=0;
        int coverage=0;
        int lastindexdx=0;
        int destination=nums.length-1;
        if(nums.length==1)
        {
            return 0;
        }
        for(int i=0;i<nums.length;i++)
        {
            coverage=Math.max(coverage,nums[i]+i);

            if(i==lastindexdx)
            {
                lastindexdx=coverage;
                finaljumps++;
                if(coverage>=destination)
                {
                    return finaljumps;
                }
            }
        }
        return finaljumps;
    }


}
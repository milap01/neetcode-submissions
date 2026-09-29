class Solution {
    public int maxSubArray(int[] nums) {
        
        int curr = 0;

        int mx = nums[0];

        for(int num : nums){

            if(curr < 0){
                curr = 0;
            }

            curr += num;

            mx = Math.max(mx,curr);
        }

        return mx;
    }
}

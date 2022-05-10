class MaxConsecutiveOnes {
    

    static int simpleApproach(int[] nums) {
        int result = 0, count = 0;
        return result;
    }

    static int findStartEndIndex(int[] nums) {
        
        int maxCount = 0;

        /* If we were to create an array to store the indices 
        what would be the length of the indices array
        Even if the input array contains alternating 1's and 
        0's the index array size will not exceed the size of the input array 
        */
        int[] start_index = new int[nums.length]; // Use ArrayList here
        int[] end_index = new int[nums.length]; // Use ArrayList here
        int j = 0;
        int k = 0;

        for( int i = 0; i < nums.length; i++ ) {
            
            if(i != 0) { // To prevent array index out of bounds exception
                if( nums[i] == 1 && nums[i - 1] == 0 ) {
                    start_index[j] = i;
                    j++;
                }
            }
            else {
                if( nums[0] == 1 ) {
                    start_index[j] = 0;
                    j++;
                }
            }
            
            if(i != nums.length) {
                if( nums[i] == 1 && nums[i + 1] == 0) {
                    end_index[k] = i+1;
                    k++;
                }
            }
            else {
                if ( nums[i] == 1 ) {
                    end_index[k] = i;
                    k++;
                }
            }
        }
        
        return maxCount;
    }

    public static void main(String args[]) {

        //int[] nums = {1,1, 0, 0, 1, 1, 1, 0};
        int[] nums = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0};
        findStartEndIndex(nums);




    }
}
/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

public class Solution {

    public String getSum(int a, int b) {
        int sum = a + b;
        return sum;
    }      

    public static void main(String args[]) {

        Solution obj = new Solution();
        System.out.println(obj.getSum(10, 20));
    }
}

/******************************************************************************
Output:- Compilation error
*******************************************************************************/
/******************************************************************************
2. A bag contains 50 P, 25 P, and 10 P coins in the ratio 5: 9: 4, amounting to Rs. 206. Find the number of coins of each type respectively.
Answer:- 200, 360, 160 
*******************************************************************************/

/******************************************************************************
3. Can we access the variables outside the method body which are defined inside the method body?
Answer:- No
*******************************************************************************/

/******************************************************************************
4. What is the output of the following code?
*******************************************************************************/

public class Solution {
    public int getSum(int a, int b) {
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

/******************************************************************************
5. Which keyword is used to skip to the next iteration of the loop? 
Answer:- continue
*******************************************************************************/
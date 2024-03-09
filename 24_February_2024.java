/******************************************************************************
5. What will be the output of the following code? 
*******************************************************************************/

public class Solution {
    public static void main(String args[]) {
        int x = 5;
        int y = 10;
        first: {
            second: {
                third: {
                    if (x == y >> 1) {
                        break second;
                    }
                }
                System.out.println(x);
            }
            System.out.println(y);
        }
    }
}

/******************************************************************************
Output:- 10
*******************************************************************************/
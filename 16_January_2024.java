/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

public class Solution {
    static int x = 10;

    public static void main(String args[]) {
        System.out.println(x);
    }
}

/******************************************************************************
Output:- 10
*******************************************************************************/

/******************************************************************************
2. What is the output of the following code?
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
3. Salaries of Ravi and Sumit are in the ratio 2 : 3. If the salary of each is increased by Rs. 4000, the new ratio becomes 40 : 57. What is Sumit’s salary
Answer:- Rs. 38,000
*******************************************************************************/

/******************************************************************************
 4. What will be the output of the following code?
*******************************************************************************/

public class Solution {
    public static void main(String args[]) {
        int i = 2;

        switch (i) {
            case 1:
                System.out.print("Case 1" + "");
                break;
            case 2:
                System.out.print("Case 2" + "");
                break;
            case 3:
                System.out.print("Case 3" + "");
                break;
            default:
                System.out.print("Default" + "");
        }
    }
}

/******************************************************************************
Output:- Case 2
*******************************************************************************/








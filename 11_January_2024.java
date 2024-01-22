/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

public class Solution {
    public static void main(String args[]) {
        int x = 5;
        int y = 6;

        if (x++ == - -y) {
            System.out.println("Coding Ninjas");
        } else {
            System.out.println("Ninjas");
        }
    }
}

/******************************************************************************
Output:- Coding Ninjas 
*******************************************************************************/

/******************************************************************************
2. What is the output of the following code?
*******************************************************************************/

public class Solution {
    public Static getSum(int a, int b) {
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
3. What is the output of the following code?
*******************************************************************************/

public class Test {
    public static void main(String args[]) {
        int x = 10;
        System.out.print(x + "");
    }

    static {
        int x = 20;
        System.out.print(x + "");
    }
}

/******************************************************************************
Output:- 20 10 
*******************************************************************************/

/******************************************************************************
4. Which of the following operators returns 1 if the corresponding bits are different?
Answer:- Bitwise Exclusive Or operator
*******************************************************************************/

/******************************************************************************
5. 3 monkeys have bananas in a ratio of 1/3:1/5:1/7. The total number of bananas with 3 monkeys is 284. How many bananas does each monkey have? 
Answer:- 140, 84, 60
*******************************************************************************/
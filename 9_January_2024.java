/******************************************************************************
2. What is the output of the following code?
*******************************************************************************/

public class Solution {
    public static void main(String args[]) {
        int a = 8;
        System.out.println("a >> 2 = " + (a >> 2));
    }
}

/******************************************************************************
Output:- a >> 2 = 2
*******************************************************************************/

/******************************************************************************
3. What is the output of the following code?
*******************************************************************************/

public class Solution {
    public Solution() {
        System.out.println("Default constructor called");
    }

    public static void main(String args[]) {
        Solution obj = new Solution(10);
    }
}

/******************************************************************************
Output:- Compile – time error
*******************************************************************************/

/******************************************************************************
4. What is the output of the following code?
*******************************************************************************/

class Test {
    private int a = 10;
}

public class Solution {
    public static void main(String args[]) {
        Test obj = new Test();
        System.out.println(obj.a);
    }
}

/******************************************************************************
Output:- Compile – time error
*******************************************************************************/






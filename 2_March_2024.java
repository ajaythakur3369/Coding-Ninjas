/******************************************************************************
5. What is the output of the following code?
*******************************************************************************/

public class Test {
    int x = 10;
    public static void main(String args[]) {
        System.out.print(x);
    }
    static {
        System.out.println(x + 10);
    }
}

/******************************************************************************
Output:- error
*******************************************************************************/
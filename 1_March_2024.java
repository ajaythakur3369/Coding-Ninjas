/******************************************************************************
4. What will be the output of the following code?
*******************************************************************************/

public class Test {
    public static void main(String args[]) {
        try {
            throw 10;
        }       
        catch(int e) {
            System.out.println("Catch the exception" + e);
        }        
    }        
}

/******************************************************************************
Output:- Compilation error
*******************************************************************************/
/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

public class multidimention_array {
    public static void main(String args[]) {
        int arr[][] = new int[3][];
        arr[0] = new int[1];
        arr[1] = new int[2];
        arr[2] = new int[3];
        int sum = 0;
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < i + 1; ++j)
                arr[i][j] = j + 1;
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < i + 1; ++j)
                sum + = arr[i][j];
        System.out.print(sum);
    }
}

/******************************************************************************
Output:- 10
*******************************************************************************/

/******************************************************************************
2. How many types of assignment operators in java?
Answer:- 5
*******************************************************************************/

/******************************************************************************
3. What is the output of the following code?
*******************************************************************************/

class Parent {

    public final void show() {
        System.out.println("Inside parent class");
    }
}

class Child extends Parent {

    public void show() {
        System.out.println("Inside child class");
    }
}

public class Main {
    public static void main(String args[]) {
        Parent p = new Child();
        p.show();
    }
}

/******************************************************************************
Output:- Error 
*******************************************************************************/

/******************************************************************************
4. C++ supports overloading of all except one of the following. Identify it.
Answer:- Destructor
*******************************************************************************/
/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

class Base {
    
    public void show() {
        System.out.println("Base class show() method called");
    }
}

class Derived extends Base {
    
    public void show() {
        System.out.println("Derived class show() method called");
    }

}

public class Main {

    public static void main(String[] args) {
        Base b = new Derived();;
        b.show();
    }

}

/******************************************************************************
Output:- Derived class show() method called
*******************************************************************************/

/******************************************************************************
2. Let A be a square matrix of size n x n. Consider the below pseudocode. What is the expected output?
*******************************************************************************/

C = 100;
for i = 1 to n do
    for j = 1 to n do 
        Temp = A[i][j] + C;
        A[i][j] = A[j][i];
        A[j][i] = Temp - C;
for i = 1 to n do
    for j = 1 to n do
        Output(A[i][j]);

/******************************************************************************
Output:- The matrix A itself
*******************************************************************************/

/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

final class Parent {

    public void show() {
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
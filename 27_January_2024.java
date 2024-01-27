/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

class Base {

    final public void show() {
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
Output:- Compile time error
*******************************************************************************/


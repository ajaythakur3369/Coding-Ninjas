/******************************************************************************
2. What is the output of the following code?
*******************************************************************************/

public class CodingNinjas {

    public static void main(String[] args) {
        String str1 = "Coding";
        int len = str1.length();

        String str2 = "";
        while (len > len / 2) {
            len--;
            str2 += str1.charAt(len);
        }

        str1 = str1.toUpperCase();
        str2 = str2.toLowerCase();

        String str = str1 + str2;

        if(str.contains("NGgn")) {
            str += "Ninjas";
        }

        str = str.toLowerCase();
        System.out.println(str);
    }
}

/******************************************************************************
Output:- Codinggnidocninjas
*******************************************************************************/

/******************************************************************************
3. What is the output of the following code?
*******************************************************************************/

public class Solution {
    public static void main(String arg[]) {
        int a = 8;
        System.out.println("a >> 2 = " + (a >> 2));
    }
}

/******************************************************************************
Output:- a >> 2 = 2 
*******************************************************************************/

/******************************************************************************
4. What is the output of the following code?
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
Output:- Error
*******************************************************************************/

/******************************************************************************
5. How many types of decrement operators in java?
Answer:- 2
*******************************************************************************/
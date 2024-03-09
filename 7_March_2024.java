/******************************************************************************
1. What is the output of the following code? 
*******************************************************************************/

public class CodingNinjas{
    public static void main(String[]args) {
        String str1 = "Coding";
        int len = str1.length();
        String str2 = "";
        while (len > len/2) {
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
Output:- codinggnidocninjas
*******************************************************************************/

/******************************************************************************
2. What is the output of the following code?
*******************************************************************************/

public class Solution{
    public String getSum(int a, int b) {
        int sum = a + b;
        return sum;
    }
    public static void main(String args[]) {
        Solution obj = new Solution();
        System.out.println(obj.getSum(10, 20));
    }
} 

/******************************************************************************
Output:- compilation Error 
*******************************************************************************/

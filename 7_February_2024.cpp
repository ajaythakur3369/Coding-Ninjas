/******************************************************************************
1. What is the output of the following code?
*******************************************************************************/

#include <iostream>
using namespace std;

int main() {
    char * a = "Hello\0World";
    cout << strlen(a) << endl;
    return 0;
}

/******************************************************************************
Output:- 5
*******************************************************************************/

/******************************************************************************
2. The concept of Encapsulation is best shown by 
Answer:- class student{int a; public: void disp(){ cout<<a;} };
*******************************************************************************/
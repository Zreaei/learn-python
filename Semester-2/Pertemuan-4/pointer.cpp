#include <iostream>
using namespace std;

int main(){
    int x = 10;
    int *px;

    px = &x;

    cout << "Nilai x: " << x << endl;
    cout << "Alamat x: " << px << endl;

    int test;
    int *ptest;

    cout << "---------- INPUT 1 ----------" << endl;
    cout << "Masukan nilai: "; cin >> test;
    ptest = &test;
    cout << "---------- OUTPUT ----------" << endl;
    cout << "Nilai: " << test << endl;
    cout << "Alamat: " << ptest << endl;

    cout << "---------- INPUT 2 ----------" << endl;
    cout << "Masukan nilai: "; cin >> test;
    ptest = &test;
    cout << "---------- OUTPUT ----------" << endl;
    cout << "Nilai Ke-2: " << test << endl;
    cout << "Alamat Ke-2: " << ptest << endl;
}
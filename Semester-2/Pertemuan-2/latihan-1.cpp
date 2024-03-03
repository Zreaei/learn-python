#include <iostream>
using namespace std;

// Latihan 1
int main() {
    string huruf[12] = {"c","h","a","m","p","i","o","n","s","h","i","p"};
    cout << "Huruf Pertama: " << huruf[0] << endl;
    cout << "Huruf Kelima: " << huruf[4] << endl;

    for (int i = 0; i < 12; i++) {
        cout << huruf[i] << endl;
    }
    
    return 0;
}

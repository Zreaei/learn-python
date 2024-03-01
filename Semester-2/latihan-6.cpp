#include <iostream>
using namespace std;

// Latihan 4
int main() {
    int arr[2][3];

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Masukkan nilai array" << "[" << i << "]" << "[" << j << "]: ";
            cin >> arr[i][j];
        }
    } cout << endl;
    
    int m = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] > m) {
                m = arr[i][j];
            }
        }
    }

    cout << "Nilai Maksimum dari array tersebut adalah: " << m << endl;
    
    return 0;
}
#include <iostream>
using namespace std;

// Latihan 4
int main() {
    int a[2][3];
    int b[2][3];
    int hasil[2][3];

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Masukkan Array A: " << "[" << i << "]" << "[" << j << "]: ";
            cin >> a[i][j];
        }
    } cout << endl;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Masukkan Array B: " << "[" << i << "]" << "[" << j << "]: ";
            cin >> b[i][j];
        }
    } cout << endl;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            hasil[i][j] = a[i][j] + b[i][j];
        }
    } cout << endl;

    cout << "Hasil Penjumlahan Array A dan B adalah:  " << endl;
    cout << hasil[0][0] << " " << hasil[0][1] << " " << hasil[0][2] << endl;
    cout << hasil[1][0] << " " << hasil[1][1] << " " << hasil[1][2] << endl;

    return 0;
}
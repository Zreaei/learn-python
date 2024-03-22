#include <iostream>
using namespace std;

int main() {
    int a[2][2];
    int b[2][3];
    int hasil[2][2];

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << "Masukkan Matrix A: " << "[" << i << "]" << "[" << j << "]: ";
            cin >> a[i][j];
        }
    } cout << endl;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << "Masukkan Matrix B: " << "[" << i << "]" << "[" << j << "]: ";
            cin >> b[i][j];
        }
    } cout << endl;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            hasil[i][j] = a[i][j] * b[i][j];
        }
    } cout << endl;

    cout << "Hasil Perkalian Matrix A dan B adalah:  " << endl;
    cout << hasil[0][0] << " " << hasil[0][1] << endl;
    cout << hasil[1][0] << " " << hasil[1][1] << endl;

    return 0;
}
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

    cout << "Nilai array 2 x 3 adalah: " << endl;
    cout << arr[0][0] << " " << arr[0][1] << " " << arr[0][2] << endl;
    cout << arr[1][0] << " " << arr[1][1] << " " << arr[1][2] << endl;

    return 0;
}
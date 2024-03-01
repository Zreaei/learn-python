#include <iostream>
using namespace std;

// Latihan 3
int main(){
    int A[2][2] = {{1,2},{3,4}};
    int B[2][2] = {{1,2},{3,4}};
    int C[2][2];

    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }

    cout << "Nilai dari array C adalah: " << endl;
    cout << C[0][0] << " " << C[0][1] << endl;
    cout << C[1][0] << " " << C[1][1] << endl;

    return 0;
}
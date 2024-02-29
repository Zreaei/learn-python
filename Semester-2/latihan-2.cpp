#include <iostream>
using namespace std;

// Latihan 2
int main(){
    int nilai[10] = {97,90,68,75,80,89,62,45,99,71};
    int jmlNilai = sizeof(nilai) / sizeof(int);
    int totalNilai = 0;

    for (int i = 0; i < jmlNilai; i++) {
        totalNilai += nilai[i];
    }

    float avgNilai = (float)totalNilai / jmlNilai;

    cout << "Nilai rata-ratanya adalah: " << avgNilai << endl;
}
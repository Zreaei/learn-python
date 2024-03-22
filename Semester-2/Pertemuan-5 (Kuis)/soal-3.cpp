#include <iostream>
using namespace std;

int main(){
    int awal = 10; // Inisialisasi Nilai Awal pada Integer awal sebesar 10
    int *pawal; // Inisialisasi Integer *pawal untuk menyimpan alamat pointer awal

    pawal = &awal;

    cout << "Nilai Awal:  " << awal << endl; // Output Nilai Awal
    cout << "Alamat Nilai Awal: " << pawal << endl; // Alamat Nilai Awal

    cout << "---------------------------" << endl;

    int input; // Inisialisasi Integer input
    int *pinput; // Inisialisasi Integer *pinput untuk menyimpan alamat pointer input

    cout << "Input Ke-1: "; cin >> input; // Input Ke-1
    pinput = &input;

    cout << endl;

    // Output dan Alamat Pointer dari Input Ke-1
    cout << "Output Ke-1: " << input << endl;
    cout << "Alamat Ke-1: " << pinput << endl;

    cout << "---------------------------" << endl;

    // Input Pointer Ke-2 (Mengganti nilai yang ada pada Input Ke-1)
    cout << "Input Ke-2: "; cin >> input; // Input Ke-2
    pinput = &input;

    cout << endl;

    // Output dan Alamat Pointer dari Input Ke-2
    cout << "Output Ke-2: " << input << endl;
    cout << "Alamat Ke-2: " << pinput << endl;

    cout << endl;

    cout << "Dari program diatas, dapat dilihat bahwa pointer tetap memiliki alamat memori yang sama meskipun data atau nilainya sudah diganti." << endl;
}
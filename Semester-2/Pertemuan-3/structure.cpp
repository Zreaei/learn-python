#include <iostream>
using namespace std;

int main() {
    // Mendefinisikan struct
    struct Mahasiswa {
        string namaLengkap;
        string NIM;
        string Angkatan;
        string programStudi;
        int IPK;
    };

    // Menginisialisasi objek struct
    Mahasiswa rafi;
    rafi.namaLengkap = "Muhammad Rafi Zamzami";
    rafi.NIM = "123456789";
    rafi.Angkatan = "2022";
    rafi.programStudi = "Informatika";
    rafi.IPK = 3.75;

    // Mengakses dan mencetak informasi dari objek struct
    cout << "Nama Lengkap: " << rafi.namaLengkap << endl;
    cout << "NIM: " << rafi.NIM << endl;
    cout << "Angkatan: " << rafi.Angkatan << endl;
    cout << "Program Studi: " << rafi.programStudi << endl;
    cout << "IPK: " << rafi.IPK << endl;

    return 0;
}

#include <iostream>
using namespace std;

struct nilaiMahasiswa {
    string namaMahasiswa;
    string NIM;
    int tugas_1;
    int tugas_2;
    int tugas_3;
    int nilaiAkhir;
};

int main(){
    nilaiMahasiswa mahasiswa;
    mahasiswa.namaMahasiswa = "";
    mahasiswa.NIM = "";
    mahasiswa.tugas_1 = 0;
    mahasiswa.tugas_2 = 0;
    mahasiswa.tugas_3 = 0;

    cout << "Masukan nama mahasiswa: ";
    cin >> mahasiswa.namaMahasiswa;
    cout << "Masukan NIM mahasiswa: ";
    cin >> mahasiswa.NIM;
    cout << "Masukan nilai tugas 1: ";
    cin >> mahasiswa.tugas_1;
    cout << "Masukan nilai tugas 2: ";
    cin >> mahasiswa.tugas_2;
    cout << "Masukan nilai tugas 3: ";
    cin >> mahasiswa.tugas_3;

    cout << endl;

    mahasiswa.nilaiAkhir = (mahasiswa.tugas_1 + mahasiswa.tugas_2 + mahasiswa.tugas_3) / 3;

    if (mahasiswa.nilaiAkhir >= 75) {
        cout << mahasiswa.namaMahasiswa << " Lulus" << endl ;
    } else {
        cout << mahasiswa.namaMahasiswa << " Tidak Lulus" << endl;
    };

    return 0;
}
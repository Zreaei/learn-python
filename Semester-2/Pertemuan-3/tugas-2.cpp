#include <iostream>
using namespace std;

struct mahasiswa {
    string namaMahasiswa;
    string NIM;
    string angkatan;
    string prodi;
};

struct mataKuliah {
    struct mahasiswa mahasiswa;
    string namaMataKuliah;
    string kodeMataKuliah;
};

int main(){
    mataKuliah mataKuliah;
    mataKuliah.mahasiswa.namaMahasiswa = "Muhammad Rafi Zamzami";
    mataKuliah.mahasiswa.NIM = "2300000";
    mataKuliah.mahasiswa.angkatan = "2023";
    mataKuliah.mahasiswa.prodi = "S1 Rekayasa Perangkat Lunak";
    mataKuliah.namaMataKuliah = "Struktur Data dan Algortima";
    mataKuliah.kodeMataKuliah = "RL-0101";   

    cout << "Nama Mahasiswa: " << mataKuliah.mahasiswa.namaMahasiswa << endl;
    cout << "NIM Mahasiswa: " << mataKuliah.mahasiswa.NIM << endl;
    cout << "Angkatan Mahasiswa: " << mataKuliah.mahasiswa.angkatan << endl;
    cout << "Prodi Mahasiswa: " << mataKuliah.mahasiswa.prodi << endl;
    cout << "Nama Mata Kuliah: " << mataKuliah.namaMataKuliah << endl;
    cout << "Kode Mata Kuliah: " << mataKuliah.kodeMataKuliah << endl; 
}


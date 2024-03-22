#include <iostream>
using namespace std;

struct nilaiMahasiswa{
    string nama;
    string mataKuliah;
    int nilaiKehadiran;
    int nilaiTugas;
    int nilaiUTS;
    int nilaiUAS;
    int nilaiTotal;
    int nilaiRata;
    string nilaiAkhir;
};

int main(){
    nilaiMahasiswa mahasiswa;
    mahasiswa.nama = "";
    mahasiswa.mataKuliah = "";
    mahasiswa.nilaiKehadiran = 0;
    mahasiswa.nilaiTugas = 0;
    mahasiswa.nilaiUTS = 0;
    mahasiswa.nilaiUAS = 0;
    mahasiswa.nilaiTotal = 0;
    mahasiswa.nilaiRata = 0;
    mahasiswa.nilaiAkhir = "";

    cout << "Masukan nama mahasiswa: ";
    cin >> mahasiswa.nama;
    cout << "Masukan mata kuliah: ";
    cin >> mahasiswa.mataKuliah;
    cout << "Masukan nilai kehadiran: ";
    cin >> mahasiswa.nilaiKehadiran;
    cout << "Masukan nilai tugas: ";
    cin >> mahasiswa.nilaiTugas;
    cout << "Masukan nilai UTS: ";
    cin >> mahasiswa.nilaiUTS;
    cout << "Masukan nilai UAS: ";
    cin >> mahasiswa.nilaiUAS;

    cout << endl;

    mahasiswa.nilaiKehadiran = (mahasiswa.nilaiKehadiran * 10/100);
    mahasiswa.nilaiTugas = (mahasiswa.nilaiTugas * 20/100);
    mahasiswa.nilaiUTS = (mahasiswa.nilaiUTS * 30/100);
    mahasiswa.nilaiUAS = (mahasiswa.nilaiUAS * 40/100);
    mahasiswa.nilaiTotal = (mahasiswa.nilaiKehadiran + mahasiswa.nilaiTugas + mahasiswa.nilaiUTS + mahasiswa.nilaiUAS);
    mahasiswa.nilaiRata = (mahasiswa.nilaiKehadiran + mahasiswa.nilaiTugas + mahasiswa.nilaiUTS + mahasiswa.nilaiUAS) / 4;

    if (mahasiswa.nilaiTotal >= 90){
        mahasiswa.nilaiAkhir = "A";
    } else if (mahasiswa.nilaiTotal >= 80){
        mahasiswa.nilaiAkhir = "B";
    } else if (mahasiswa.nilaiTotal >= 70){
        mahasiswa.nilaiAkhir = "C";
    }

    cout << "Nama Mahasiswa: " << mahasiswa.nama << endl;
    cout << "Mata Kuliah: " << mahasiswa.mataKuliah << endl;
    cout << "Nilai Kehadiran: " << mahasiswa.nilaiKehadiran << endl;
    cout << "Nilai Tugas: " << mahasiswa.nilaiTugas << endl;
    cout << "Nilai UTS: " << mahasiswa.nilaiUTS << endl;
    cout << "Nilai UAS: " << mahasiswa.nilaiUAS << endl;
    cout << "Nilai Total: " << mahasiswa.nilaiTotal << endl;
    cout << "Nilai Rata-Rata: " << mahasiswa.nilaiRata << endl;
    cout << "Nilai Akhir (Grade): " << mahasiswa.nilaiAkhir << endl;
}
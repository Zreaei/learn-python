#include <iostream>
#include <string>
using namespace std;

struct mahasiswa{
    string nama;
    int angkatan;
    string prodi;
};

typedef mahasiswa mahasiswa_array[2];
void LoadArray(mahasiswa_array peop);

int main(void){
    mahasiswa_array people;
    LoadArray(people);

    cout << "\n";
    cout << "No\t Nama\t Angkatan\t Prodi\n";
    for (int i = 0; i < 2; i++){
        cout << i+1 << "\t " << people[i].nama << "\t   " << people[i].angkatan << "\t  " << people[i].prodi << endl;
    }
}
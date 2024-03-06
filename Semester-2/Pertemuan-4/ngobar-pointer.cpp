#include <iostream>
using namespace std;

int main(){
    int asyep;
    int banyu;
    int *Pasyep;
    int *Pbanyu;
    
    cout << "Masukan nilai asyep : " ; cin >> asyep;
    Pasyep = &asyep;
    cout << "Masukan nilai banyu : " ; cin >> banyu;
    Pbanyu = &banyu;

    cout <<"-------------------------------"<<endl;

    //Output nilai dan alamat
    cout << "OUTPUTNYA" << endl;
    cout << "Nilai asyep  : " << asyep << endl;
    cout << "Alamat asyep : " << Pasyep << endl;
    
    cout << "Nilai banyu  : " << banyu << endl;
    cout << "Alamat banyu : " << Pbanyu << endl;
    cout<<endl;

    cout <<"------------- NILAI SETELAH SWAP ---------------"<<endl;
    // SWAP(asyep, banyu)
    swap(asyep, banyu);
    swap(Pasyep, Pbanyu);
    
    cout << "Nilai asyep  : " << asyep << endl;
    cout << "Alamat asyep : " << Pasyep << endl;
    cout << "Nilai banyu  : " << banyu << endl;
    cout << "Alamat banyu : " << Pbanyu << endl;

    cout<<endl;
    cout<<endl;
    cout<<endl;

    cout <<"----------- PENGGUNAAN ARRAY dan MEMORY --------------------"<<endl;
    char lokasi[] = "Cibiru"; //Pendefinisian variable array = Cibiru
    char *Plokasi = lokasi; //Pointer Lokasi untuk menunjuk nilai array lokasi

    cout << "Value         : " << lokasi << endl; //Mencetak nilai lokasi
    cout << "Array[0]      : " << lokasi[0] << endl; 
    cout << "Nilai Plokasi : " << *Plokasi << endl;
    cout << "Pointer[2]    : " << Plokasi[2] << endl;

    Plokasi += 2;
    cout << "Pointer[2+3]  : " << Plokasi[2] << endl;
    cout << "Pointer[2+3]  : " << Plokasi << endl;
}
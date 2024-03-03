#include <iostream>
using namespace std;

struct customer {
    string nama;
};

struct tiket {
    struct customer customer;
    int tiketPesan;
    int jmlDiskon;
    int jmlTiket;
    int totalPembayaran;
    int hargaTiket = 50000;
};

int main(){
    tiket ticket;

    cout << "Masukan nama Anda: ";
    cin >> ticket.customer.nama;
    cout << "Masukan jumlah tiket yang dipesan: ";
    cin >> ticket.tiketPesan;

    cout << endl;

    if (ticket.tiketPesan > 5) {
        ticket.jmlDiskon = ticket.tiketPesan * ticket.hargaTiket * 0.1;
        ticket.totalPembayaran = (ticket.tiketPesan * ticket.hargaTiket) - ticket.jmlDiskon;
    } else if (ticket.tiketPesan > 10) {
        ticket.totalPembayaran = ticket.tiketPesan * ticket.hargaTiket;
    } else if (ticket.tiketPesan > 0){
        ticket.totalPembayaran = ticket.tiketPesan * ticket.hargaTiket;
    } else {
        cout << "Tidak ada invoice yang dikeluarkan." << endl;
        return 0;
    }

    ticket.jmlTiket = ticket.tiketPesan;
    if (ticket.tiketPesan > 10) {
        ticket.jmlTiket += 1;
    }

    cout << "Nama Customer : " << ticket.customer.nama << endl;
    cout << "Jumlah Tiket yang dipesan : " << ticket.tiketPesan << endl;
    cout << "Jumlah Diskon : " << ticket.jmlDiskon << endl;
    cout << "Total Tiket : " << ticket.jmlTiket << endl;
    cout << "Total Pembayaran : " << ticket.totalPembayaran << endl;

    return 0;
}
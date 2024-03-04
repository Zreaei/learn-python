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
    int totalBonus;
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
    } else if (ticket.tiketPesan > 0) {
        ticket.totalPembayaran = ticket.tiketPesan * ticket.hargaTiket;
    } else {
        cout << "Tidak ada invoice yang dikeluarkan." << endl;
        return 0;
    }

    ticket.jmlTiket = ticket.tiketPesan;
    if (ticket.tiketPesan > 10) {
        ticket.jmlTiket += 1;
        ticket.jmlDiskon = 0;
        ticket.totalBonus = 1;
    } else {
        ticket.totalBonus = 0;
    }

    ticket.totalPembayaran = (ticket.tiketPesan * ticket.hargaTiket) - ticket.jmlDiskon;

    cout << "-------- PEMESANAN TIKET FILM THE GUARDIAN OF GALAXY VOL. 2 --------" << endl;
    cout << "Nama Customer : " << ticket.customer.nama << endl;
    cout << "Jumlah Tiket  : " << ticket.tiketPesan << endl;

    cout << endl;

    cout << "------------ INVOICE ------------" << endl;
    cout << "  The Guardian of Galaxy Vol. 2  " << endl;
    cout << "---------------------------------" << endl;

    cout << endl;

    cout << "Nama Customer     : " << ticket.customer.nama << endl;
    cout << "Total Pesanan     : " << ticket.tiketPesan << endl;
    cout << "Total Bonus       : " << ticket.totalBonus << endl;
    cout << "Total Tiket       : " << ticket.jmlTiket << endl;
    cout << "Total Diskon      : " << ticket.jmlDiskon << endl;
    cout << "Jumlah Pembayaran : " << ticket.totalPembayaran << endl;

    cout << endl;

    cout << "--------- TERIMA KASIH ---------" << endl;

    return 0;
}
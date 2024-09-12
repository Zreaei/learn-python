#include <iostream>
// #include <stdlib.h> 
using namespace std;

const int kapasitas = 10;
struct stack {
    int top;
    int isi[kapasitas];
} stack;

void buatStack(){
    stack.top = -1;
}

int isFull(){
    if (stack.top == kapasitas - 1){
        return 1;
    } else {
        return 0;
    }
}

int isEmpty(){
    if (stack.top == -1){
        return 1;
    } else {
        return 0;
    }
}

void tambahStack(int data){
    if (isFull() == 1){
        // system("cls");
        cout << "Maaf, stack sudah penuh" << endl;
    } else {
        stack.top++;
        stack.isi[stack.top] = data;
        // system("cls");
        cout << "Data " << stack.isi[stack.top] << " berhasil masuk kedalam stack" << endl;
    }
}

void lihatStack(){
    if (isEmpty() == 0){
        // system("cls");
        cout << "Menampilkan isi stack: " << endl;
        for (int i = stack.top; i >= 0; i--){
            cout << "Data index stack ke-" << i << " adalah " << stack.isi[i] << endl;
        }
    } else {
        // system("cls");
        cout << "Maaf, tidak ada data pada stack" << endl;
    }
}

void cariStack(int data){
    int tmp, itmp;

    if (isEmpty() == 1){
        // system("cls");
        cout << "Maaf, tidak ada data pada stack" << endl;
    } else {
        for (int i = stack.top; i >= 0; i--)
            if (data == stack.isi[i]){
                tmp = data;
                itmp = i;
            }
        if (data == tmp){
            // system("cls");
            cout << "Data " << data << " ditemukan pada index stack ke-" << itmp << endl;
        } else {
            // system("cls");
            cout << "Data " << data << " tidak ditemukan pada stack" << endl;
        }
    }
}

void hapusStack(){
    if (isEmpty() == 0){
        stack.top--;
        // system("cls");
        cout << "Data " << stack.isi[stack.top] << " berhasil dihapus dari stack" << endl;
    } else {
        // system("cls");
        cout << "Maaf, tidak ada data pada stack" << endl;
    }
}

void kosongkanStack(){
    stack.top = -1;
    // system("cls");
    cout << "Stack berhasil dikosongkan" << endl;
}

int main(){
    while(true){
        // system("cls");
        int pilihan, data;
        string input;
        cout << "Menu Program Stack" << endl;
        cout << "===================" << endl;
        cout << "1. Tambah Data ke Stack" << endl;
        cout << "2. Lihat Isi Stack" << endl;
        cout << "3. Cari Data pada Stack" << endl;
        cout << "4. Hapus Data dari Stack" << endl;
        cout << "5. Kosongkan Stack" << endl;
        cout << "6. Keluar" << endl;
        cout << endl; 

        cout << "Masukan Menu: ";
        cin >> pilihan;

        if (pilihan == 1) {
            // system("cls");
            cout << "Masukkan data yang ingin ditambahkan: ";
            cin >> data;
            tambahStack(data);
        } else if (pilihan == 2) {
            // system("cls");
            lihatStack();
        } else if (pilihan == 3) {
            // system("cls");
            cout << "Masukkan data yang ingin dicari: ";
            cin >> data;
            cariStack(data);
        } else if (pilihan == 4) {
            // system("cls");
            hapusStack();
        } else if (pilihan == 5) {
            // system("cls");
            kosongkanStack();
        } else if (pilihan == 6) {
            // system("cls");
            cout << "Terima kasih telah menggunakan program Stack" << endl;
        } else {
            // system("cls");
            cout << "Pilihan tidak valid" << endl;
        }

        cout << endl;
        cout << "1. Kembali ke Menu Utama" << endl;
        cout << "2. Keluar" << endl;
        cout << endl;
        cout << "Masukan Menu : "; 
        cin >> pilihan;

        if (pilihan == 2)
            return 0;
    }
}

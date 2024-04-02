#include <iostream>
using namespace std;

struct node {
    int dataGenap; // Deklarasi Variabel
    node *next; // Pointer untuk menunjuk Node selanjutnya
};

int main(){
    // cout << "Linked List Lesgo" << endl;

    // Kondisi awal, head = NULL
    // struct node *head = NULL;
    // head = (struct node*) malloc (sizeof(struct node));
    // cout << head << endl;

    // Posisi Awal / Inisialisasi Pointer
    node *head = NULL;
    node *kedua = NULL;
    node *ketiga = NULL;
    node *tail = NULL;

    // Mengalokasikan Keempat Node
    head = new node();
    kedua = new node();
    ketiga = new node();
    tail = new node();

    // Masukan Data kedalam masing-masing Node
    head->dataGenap = 2;
    head->next = kedua;
    kedua->dataGenap = 12;
    kedua->next = ketiga;
    ketiga->dataGenap = 20;
    ketiga->next = tail;
    tail->dataGenap = 26;
    tail->next = NULL;

    cout << "Data Awal: " << head->dataGenap << endl;
    cout << "Data Kedua: " << kedua->dataGenap << endl;
    cout << "Data Ketiga: " << ketiga->dataGenap << endl;
    cout << "Data Terakhir: " << tail->dataGenap << endl;

    // Transfersal Node
    
}
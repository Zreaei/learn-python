#include <iostream>
using namespace std;

struct node{
    int data;
    node *next;
};

// Inisialisasi Pointer
node *head;
node *tail;

// Melakukan Pengecekan apakah Nodenya kosong
bool isEmpty(){
    if (head==NULL){
        return true;
    }
    return false;
}

// Menambahkan data diawal
void insertFirst(int nilai){
    node *new_node;
    new_node = new node;
    new_node -> data = nilai;

    if (isEmpty()){
        head = new_node;
        head -> next = NULL;
    } else {
        new_node -> next = head;
        head = new_node;
    }
}

void insertLast(int nilai){
    node *new_node, *current;
    new_node = new node;
    new_node -> data = nilai;
    new_node -> next = NULL;

    if (isEmpty()){
        head = new_node;
        head -> next = NULL;
    } else {
        current = head;
        
        while (current -> next != NULL){
            current = current -> next;
        }
        current -> next = new_node;
    }
}

// Transfersal (Menelusuri node yang ada)
void cetakList(){
    if (!isEmpty()){
        node *current;
        current = head;
        
        while (current != NULL){
            cout << current -> data << endl;
            current = current -> next;
        }
    }
}

int main(){
    head = NULL;
    insertFirst(1);
    insertFirst(3);
    insertFirst(5);
    cetakList();
}
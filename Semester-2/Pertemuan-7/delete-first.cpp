#include <iostream>
#include <malloc.h>
using namespace std;

struct node {
    int data;
    struct node *next;
    struct node *prev;
};

node *head;
node *current = NULL;

bool isEmpty() {
    if (head == NULL) {
        return true;
    }
    return false;
};

void insertLast(int nilai){
    node *new_node;
    new_node = new node;
    new_node->data = nilai;
    new_node->next = NULL;

    if (isEmpty()){
        new_node->prev = NULL;
        head = new_node;
    } else {
        current = head;
        
        while (current->next != NULL){
            current = current->next;
        }
        current->next = new_node;
        new_node->prev = current;
    }
};

void deleteFirst(struct node *hapus){
    if (isEmpty()){
        cout << "List kosong, tidak ada yang dihapus" << endl;
        return;
    }

    if (head == hapus){
        head = hapus->next;
    }

    if (hapus->next != NULL){
        hapus->next->prev = hapus->prev;
    }

    if (hapus->prev != NULL){
        hapus->prev->next = hapus->next;
    }

    delete hapus;
};

void cetakList(){
    if (isEmpty()){
        cout << "List kosong" << endl;
        return;
    }

    node *current = head;
    while (current != NULL){
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
};

int main(){
    head = NULL;
    insertLast(1);
    insertLast(3);
    insertLast(5);
    
    cout << "Sebelum remove first" << endl; 
    cetakList();

    cout << "Setelah remove first" << endl;
    deleteFirst(head);
    cetakList();

    return 0;
}

#include <iostream>
#include <malloc.h>
using namespace std;

struct node {
    int data;
    struct node *next;
    struct node *prev;
};

node *head;
node *tail;
node *current = NULL;

bool isEmpty() {
    if (head == NULL) {
        return true;
    }
    return false;
};

void insertFirst(int nilai){
    node *new_node;
    new_node = new node;
    new_node->data = nilai;

    if (isEmpty()){
        head = new_node;
        head->next = NULL;
    } else {
        new_node->next = head;
        new_node->prev = NULL;
        head = new_node;
    }
};

void inserAfter(struct node *next_node, int nilai){
    if (next_node == NULL){
        cout << "Nilai sebelumnya tidak boleh NULL";
        return;
    }

    node *new_node = new node;
    new_node->data = nilai;

    if (isEmpty()){
        new_node->prev->next = new_node;
    } else {
        new_node->prev = next_node->prev;
        next_node->prev = new_node->prev;
        new_node->next = next_node;
        head->next = new_node;
    }
};

void cetakList(){
    if (!isEmpty()){
        node *current;
        current = head;
        
        while (current != NULL){
            cout << current->data << " ";
            current = current->next;
        }
    }
};

int main() {
    head = NULL;
    insertFirst(7);
    insertFirst(5);
    insertFirst(1);
    cout << "Sebelum Insert" << endl;
    cetakList();
    cout << "\n";
    inserAfter(head->next, 3);
    cout << "Setelah Insert" << endl;
    cetakList();
    cout << "\n";
}
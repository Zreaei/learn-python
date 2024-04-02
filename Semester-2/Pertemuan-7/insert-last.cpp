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
    insertLast(1);
    insertLast(3);
    insertLast(5);
    insertLast(7);
    cetakList();
}
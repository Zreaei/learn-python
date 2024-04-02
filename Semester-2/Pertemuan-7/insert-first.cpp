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

bool isEmpty() {
    if (head == NULL) {
        return true;
    }
    return false;
};

void insertFirst(int nilai){
    node *new_node;
    new_node = (struct node *)malloc(sizeof(struct node));
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
    insertFirst(1);
    insertFirst(3);
    insertFirst(5);
    insertFirst(7);
    cetakList();
}
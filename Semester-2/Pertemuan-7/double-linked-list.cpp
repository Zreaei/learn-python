#include <iostream>
#include <malloc.h>
using namespace std;

struct node {
    int data;
    struct node *prev;
    struct node *next;
};

int main() {
    // Inisalisasi Node
    node *head;
    node *one = NULL;
    node *two = NULL;
    node *three = NULL;
    node *current = NULL;
    
    // Alokasi Node
    one = (struct node *)malloc(sizeof(struct node));
    two = (struct node *)malloc(sizeof(struct node));
    three = (struct node *)malloc(sizeof(struct node));

    // Assign Data Value
    one->data = 1;
    two->data = 2;
    three->data = 3;

    // Connect Node
    one->next = two;
    one->prev = NULL;
    two->next = three;
    two->prev = one;
    three->next = NULL;
    three->prev = two;

    // Menyimpan Node pertama menjadi Head
    head = one;

    // Tampilkan data Head
    current = head;
    cout << current->data << endl;
    while (current->next != NULL) {
        current = current->next;
        cout << current->data << endl;
    }
    return 0;
};


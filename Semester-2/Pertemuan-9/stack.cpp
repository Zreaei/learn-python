#include <iostream>
#include <stack>
using std::cout;
using std::endl;

const int kapasitas = 5;
struct stack {
    int top;
    int temp[kapasitas];
} stack;

void createStack(){
    stack.top = -1;
};

void push(int data){
    // Mengecek Apakah stack Sudah Penuh
    if (isFull() == 1){
        cout << "Maaf, stack sudah penuh" << endl;
    } else {
        stack.top++; // Menaikkan Posisi Top ke atas
        stack.temp[stack.top] = data; // Menyisipkan elemen baru ke posisi Top
        cout << "Data " << stack.temp[stack.top] << "Berhasil masuk kedalam stack" << endl;
    }
}

void displayStack(){
    if (isEmpty() == 0){
        cout << "Menampilkan isi stack: " << endl;
        for (int i = stack.top; i >= 0; i--){
            cout << "Data index stack ke-" << i << " adalah " << stack.temp[i] << endl;
        } cout << endl;
    } else {
        cout << "Maaf, tidak ada data pada stack" << endl;
    }
}

int isEmpty(){
    if (stack.top == -1) {
        return 1;
    } else {
        return 0;
    }
};

int isFull(){
    if (stack.top == kapasitas - 1){
        return 1;
    } else {
        return 0;
    }
};

int main(){
    int data;
    createStack();
    cout << "Push Data" << endl;
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    cout << endl;
    displayStack();
} 
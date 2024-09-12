#include <iostream>
#include <string>
using namespace std;

const int kapasitas = 20;
struct Stack {
    int top;
    char isi[kapasitas];
} charStack;

void buatStack(){
    charStack.top = -1;
}

void push(char data) {
    if (charStack.top == kapasitas - 1) {
        cout << "Stack penuh" << endl;
        return;
    } charStack.isi[++charStack.top] = data;
}

char pop() {
    if (charStack.top == -1) {
        cout << "Stack kosong" << endl;
        return '\0';
    } return charStack.isi[charStack.top--];
}

void membalikanKata(string input) {
    for (int i = 0; i < input.length(); ++i) {
        push(input[i]);
    }

    cout << "Menampilkan kalimat yang telah dibalik: ";
    while (charStack.top != -1) {
        cout << pop();
    } cout << endl;
}

int main() {
    string input;
    cout << "Masukkan kalimat: ";
    cin >> input;

    buatStack();
    membalikanKata(input);
    return 0;
}

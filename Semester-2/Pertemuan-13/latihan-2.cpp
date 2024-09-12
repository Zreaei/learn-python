#include <iostream>
#include <stdlib.h> 
using namespace std;

struct tree {
    int data;
    tree *left, *right;
};

tree *pohon, *root;

void deklarasi() {
    pohon = NULL;
}

void insertTree(tree **root, int nilai) {
    tree *new_node;

    if ((*root) == NULL) {
        new_node = new tree;
        new_node->data = nilai;
        new_node->left = new_node->right = NULL;

        (*root) = new_node;
        (*root)->data = nilai;
        (*root)->left = (*root)->right = NULL;
        cout << "Data " << new_node->data << " berhasil dimasukkan" << endl;
    } else if ((nilai < (*root)->data)) {
        insertTree(&(*root)->left, nilai);
        cout << "Data " << nilai << " berhasil dimasukkan di sebelah kiri" << endl;
    } else {
        insertTree(&(*root)->right, nilai);
        cout << "Data " << nilai << " berhasil dimasukkan di sebelah kanan" << endl;
    }
}

void preOrder(tree *root) {
    if (root != NULL) {
        cout << root->data << " ";
        preOrder(root->left);
        preOrder(root->right);
    }
}

void inOrder(tree *root) {
    if (root != NULL) {
        inOrder(root->left);
        cout << root->data << " ";
        inOrder(root->right);
    }
}

void postOrder(tree *root) {
    if (root != NULL) {
        postOrder(root->left);
        postOrder(root->right);
        cout << root->data << " ";
    }
}

void findTree(tree **root, int cari) {
    int level = 0;
    tree *temp;
    temp = new tree;
    temp = (*root);

    while (temp != NULL) {
        level++;
        if (temp->data == cari) {
            cout << "Data " << cari << " ditemukan" << endl;
            return;
        } else if (temp->data > cari) {
            temp = temp->left;
        } else {
            temp = temp->right;
            level--;
        }
    }
    cout << "Data " << cari << " tidak ditemukan" << endl;
    return;
}

int countNodes(tree *root) {
    if (root == NULL) {
        return 0;
    } else {
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
}

void totalNode() {
    int total = countNodes(pohon);
    cout << "Total node dalam tree: " << total << endl;
}

void deleteTree() {
    pohon = NULL;
    cout << "Data berhasil dihapus" << endl;
}

int main(){
    while(true){
        system("cls");
        int pilihan, data;
        string input;
        cout << "=================" << endl;
        cout << "Menu Program Tree" << endl;
        cout << "=================" << endl;
        cout << "1. Tambah Data ke Tree" << endl;
        cout << "2. Penelusuran PreOrder, InOrder, dan PostOrder" << endl;
        cout << "3. Cari Data pada Tree" << endl;
        cout << "4. Hitung Jumlah Node dalam Tree" << endl;
        cout << "5. Kosongkan Tree" << endl;
        cout << "6. Keluar" << endl;
        cout << endl; 

        cout << "Masukan Menu: ";
        cin >> pilihan;

        if (pilihan == 1) {
            system("cls");
            cout << "Masukkan Data ke dalam Tree: ";
            cin >> data;
            insertTree(&pohon, data);
        } else if (pilihan == 2) {
            system("cls");
            cout << "Data PreOrder" << endl;
            preOrder(pohon);
            cout << endl;
            cout << endl;

            cout << "Data InOrder" << endl;
            inOrder(pohon);
            cout << endl;
            cout << endl;

            cout << "Data PostOrder" << endl;
            postOrder(pohon);
            cout << endl;
        } else if (pilihan == 3) {
            system("cls");
            cout << "Masukkan data yang ingin dicari: ";
            cin >> data;
            findTree(&pohon, data);
        } else if (pilihan == 4) {
            system("cls");
            totalNode();
        } else if (pilihan == 5) {
            system("cls");
            deleteTree();
        } else if (pilihan == 6) {
            system("cls");
            cout << "Terima kasih telah menggunakan program ini" << endl;
            return 0;
        } else {
            system("cls");
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

// int main() {
//     deklarasi();
//     insertTree(&pohon, 50);
//     insertTree(&pohon, 17);
//     insertTree(&pohon, 12);
//     insertTree(&pohon, 23);
//     insertTree(&pohon, 9);
//     insertTree(&pohon, 14);
//     insertTree(&pohon, 19);
//     insertTree(&pohon, 72);
//     insertTree(&pohon, 54);
//     insertTree(&pohon, 70);
//     insertTree(&pohon, 67);
//     cout << endl;

//     if (pohon == NULL) {
//         cout << "Pohon kosong" << endl;
//     } else {
//         cout << "Data PreOrder" << endl;
//         preOrder(pohon);
//         cout << endl;
//         cout << endl;

//         cout << "Data InOrder" << endl;
//         inOrder(pohon);
//         cout << endl;
//         cout << endl;

//         cout << "Data PostOrder" << endl;
//         postOrder(pohon);
//         cout << endl;
//         cout << endl;
//     }

//     findTree(&pohon, 10);
//     findTree(&pohon, 4);
//     deleteTree();

//     if (pohon != NULL) {
//         postOrder(pohon);
//     } else {
//         cout << "Pohon dalam keadaaan kosong" << endl;
//     }
// }
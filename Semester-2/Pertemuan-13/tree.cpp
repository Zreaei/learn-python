#include <iostream>
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

void deleteTree() {
    pohon = NULL;
    cout << "Data berhasil dihapus" << endl;
}

int main() {
    deklarasi();
    insertTree(&pohon, 50);
    insertTree(&pohon, 17);
    insertTree(&pohon, 12);
    insertTree(&pohon, 23);
    insertTree(&pohon, 9);
    insertTree(&pohon, 14);
    insertTree(&pohon, 19);
    insertTree(&pohon, 72);
    insertTree(&pohon, 54);
    insertTree(&pohon, 70);
    insertTree(&pohon, 67);
    cout << endl;

    if (pohon == NULL) {
        cout << "Pohon kosong" << endl;
    } else {
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
        cout << endl;
    }

    findTree(&pohon, 10);
    findTree(&pohon, 4);
    deleteTree();

    if (pohon != NULL) {
        postOrder(pohon);
    } else {
        cout << "Pohon dalam keadaaan kosong" << endl;
    }
}
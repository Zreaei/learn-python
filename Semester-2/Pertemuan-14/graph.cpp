#include <iostream>
using namespace std;

int vertex;
int edge;
int visited[20];
int **adj;

void buatGraph(int v, int e) {
    vertex = v;
    edge = e;

    adj = new int *[v];

    // Membuat matrix [m x n]
    for (int baris = 0; baris < v; baris++) {
        adj[baris] = new int[v];
        for (int kolom = 0; kolom < v; kolom++) {
            adj[baris][kolom] = 0; // Matrix mempunyai elemen 0 atau belum memiliki edge
        }
    }
}

void tambahEdge(int vAwal, int vTujuan) {
    adj[vAwal][vTujuan] = 1;
    adj[vTujuan][vAwal] = 1;
}

void dfs(int start) {
    // Cek vertex saat ini
    cout << vertex << " ";

    // Jika sudah dikunjungi:
    visited[start] = 1;

    // Mengunjungi vertex yang berdekatan dan belum pernah dikunjungi
    for (int i = 0; i < vertex; i++) {
        if (adj[start][i] == 1 && visited[i] == 0) {
            dfs(i);
        }
    }
}

int main() {
    int v = 8;
    int e = 8;

    buatGraph(v, e);
    
    tambahEdge(0, 1);
    tambahEdge(0, 5);
    tambahEdge(1, 2);
    tambahEdge(2, 3);
    tambahEdge(1, 4);
    tambahEdge(5, 6);
    tambahEdge(5, 7);

    dfs(0);

    return 0;
}
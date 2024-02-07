#include <iostream>
using namespace std;

// Deklarasi Function diatas karena C++ membaca code dari atas
int angka();
int input();
int dtype();

// Main
int main()
{
    // Printing
    std::cout << "Selamat pagi semuanya!\n";
    std::cout << "Ini adalah baris baru. ";
    std::cout << "Ini bukan baris baru. ";
    std::cout << "Ini akhir kalimat." << std::endl;
    
    // Memanggil function angka()
    angka();

    // Memanggil function input()
    input();

    // Memanggil function dtype()
    dtype();

    std::cin.get();
    return 0;
}

// Membuat variabel
int angka()
{
    int angka = 10;
    std::cout << angka << std::endl;
    std::cin.get();
    return 0;
}

// Deklarasi (hardcoded), Input (cin), dan namespace std 
int input()
{
    // Hard Coded
    int angka;
    angka = 10;
    cout << "Angka yang di hard coded adalah: ";
    cout << angka << endl;

    // Input (cin)
    int input;
    cout << "Masukan angka: ";
    cin >> input;
    cout << "Angka yang anda masukan adalah: ";
    cout << input << endl;

    cin.get();
    return 0;
}

// Tipe data fundamental
int dtype()
{
    // Bilangan bulat
    short a = 2; // 16-bit/2 byte
    int b = 4; // 32-bit/4 byte
    long c = 6; // 64-bit/8 byte

    // Bilangan desimal
    float d = 1.0;
    double e = 2.5;

    // Character
    char f = 'a'; //1-bit

    // Boolean
    bool g = true; // true/false

    cout << a << endl;

    cin.get();
    return 0;
}
#include <iostream>
using namespace std;

// Deklarasi Function diatas karena C++ membaca code dari atas
int angka();
int input();

// Main
int main()
{
    // Printing
    std::cout << "Selamat pagi semuanya!\n";
    std::cout << "Ini adalah baris baru. ";
    std::cout << "Ini bukan baris baru. ";
    std::cout << "Ini akhir kalimat." << std::endl;
    
    // Memanggil Function angka()
    angka();

    // Memanggil function input()
    input();

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
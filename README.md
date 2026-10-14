# Pertemuan 07 Fungsi Python
Nama: Vanisya Nur Khalimah  
NIM: 2225520201  
Kelas: S1 Pendidikan Matematika FKIP Untirta  

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan
```bash
python3 praktik/utilitas_matematika.py

## Struktur Fungsi - Pertemuan 07
def luas_persegi_panjang(p, l):
    """
    Menghitung luas persegi panjang.
    Parameter:
        p : panjang
        l : lebar
    Return:
        hasil perkalian p * l
    """
    return p * l


def luas_segitiga(a, t):
    """
    Menghitung luas segitiga.
    Parameter:
        a : alas
        t : tinggi
    Return:
        hasil perhitungan 0.5 * a * t
    """
    return 0.5 * a * t


def jumlah_n(n):
    """
    Menghitung jumlah bilangan dari 1 sampai n.
    Parameter:
        n : batas bilangan
    Return:
        total penjumlahan dari 1 sampai n
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    """
    Menghitung faktorial dari n.
    Parameter:
        n : bilangan bulat positif
    Return:
        hasil perkalian berurutan dari 1 sampai n
    """
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    """
    Menampilkan menu pilihan ke layar.
    Parameter:
        tidak ada
    Return:
        tidak ada (hanya menampilkan teks)
    """
    print("\n=== MENU ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")

## Hasil Pengujian
print("=== Hasil Pengujian ===")

# Uji fungsi luas_persegi_panjang
print("luas_persegi_panjang(8, 5) ->", luas_persegi_panjang(8, 5))   # Ekspektasi: 40

# Uji fungsi luas_segitiga
print("luas_segitiga(10, 6) ->", luas_segitiga(10, 6))               # Ekspektasi: 30

# Uji fungsi jumlah_n
print("jumlah_n(5) ->", jumlah_n(5))                                 # Ekspektasi: 15

# Uji fungsi faktorial
print("faktorial(5) ->", faktorial(5)) 

## Refleksi
def refleksi():
    """
    Refleksi:
    Dengan memisahkan perhitungan ke dalam fungsi,
    kode menjadi lebih sederhana dan modular.
    Misalnya, perhitungan faktorial yang sebelumnya
    harus ditulis berulang kini cukup dipanggil dengan faktorial(n).
    """
    return "Program lebih ringkas dan mudah diuji karena setiap perhitungan dipisah ke dalam fungsi."

print("\n=== Refleksi ===")
print(refleksi())

"""Cara menetukan segitiga menggunakan bahasa pemrograman."""


def jenis_segitiga(x, y, z):
    """
    Mengembalikan jenis segitiga berdasarkan panjang sisi-sisinya.

    Parameter:
    x (int): Panjang sisi atas yang ditandai huruf x
    y (int): Panjang sisi kiri yang ditandai huruf y
    z (int): Panjang sisi kanan yang ditandai huruf z

    Returns:
    str: Jenis segitiga (sama sisi, sama kaki, atau sembarang)
    """
    if x == y == z:
        return "Segitiga sama sisi"
    elif x == y or x == z or y == z:
        return "Segitiga sama kaki"
    else:
        return "Segitiga sembarang"

# Menerima input dari pengguna


x = int(input("Masukkan panjang sisi x: "))
y = int(input("Masukkan panjang sisi y: "))
z = int(input("Masukkan panjang sisi z: "))

# Memanggil fungsi dan mencetak hasilnya
hasil = jenis_segitiga(x, y, z)

print("Jenis segitiga: " + hasil)

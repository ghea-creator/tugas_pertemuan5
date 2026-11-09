
def analisis_kalimat(kalimat):
    # Memisahkan kalimat menjadi beberapa kata
    daftar_kata = kalimat.split()

    # Menghitung jumlah kata
    jumlah_kata = len(daftar_kata)

    # Menghitung jumlah karakter termasuk spasi
    jumlah_karakter = len(kalimat)

    # Menentukan kata terpanjang
    if daftar_kata:
        kata_terpanjang = max(daftar_kata, key=len)
    else:
        kata_terpanjang = "-"

    # Mengubah setiap awal kata menjadi huruf kapital
    kalimat_title = kalimat.title()

    return jumlah_kata, jumlah_karakter, kata_terpanjang, kalimat_title


if __name__ == "__main__":
    kalimat = input("Masukkan sebuah kalimat: ")

    hasil = analisis_kalimat(kalimat)

    print("\n=== HASIL ANALISIS KALIMAT ===")
    print("Jumlah kata       :", hasil[0])
    print("Jumlah karakter   :", hasil[1])
    print("Kata terpanjang   :", hasil[2])
    print("Title case        :", hasil[3])

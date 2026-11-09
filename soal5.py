
import re


def analisis_teks(nama_file):
    # Membaca isi file teks
    with open(nama_file, "r", encoding="utf-8") as file:
        teks = file.read()

    # Mengubah teks menjadi huruf kecil
    teks = teks.lower()

    # Mengambil kata dan menghilangkan tanda baca
    daftar_kata = re.findall(r"\b\w+\b", teks)

    # Menghitung frekuensi setiap kata menggunakan dictionary
    frekuensi = {}

    for kata in daftar_kata:
        frekuensi[kata] = frekuensi.get(kata, 0) + 1

    # Menggunakan list untuk mengurutkan 10 kata paling sering
    sepuluh_teratas = sorted(
        frekuensi.items(),
        key=lambda item: item[1],
        reverse=True
    )[:10]

    # Menggunakan set untuk mencari kata unik
    kata_unik = set(daftar_kata)

    # Mencari kata yang hanya muncul satu kali
    hapax = [
        kata for kata, jumlah in frekuensi.items()
        if jumlah == 1
    ]

    # Menghitung type-token ratio
    total_kata = len(daftar_kata)

    if total_kata > 0:
        ttr = len(kata_unik) / total_kata
    else:
        ttr = 0

    return frekuensi, sepuluh_teratas, hapax, ttr, total_kata


if __name__ == "__main__":
    try:
        hasil = analisis_teks("teks.txt")

        print("=== HASIL ANALISIS TEKS ===")

        print("\nTotal kata:", hasil[4])

        print("\nFrekuensi setiap kata:")
        for kata, jumlah in sorted(hasil[0].items()):
            print(f"{kata}: {jumlah}")

        print("\n10 kata paling sering muncul:")
        for kata, jumlah in hasil[1]:
            print(f"{kata}: {jumlah} kali")

        print("\nKata yang hanya muncul satu kali (Hapax Legomena):")
        print(", ".join(hasil[2]) if hasil[2] else "Tidak ada")

        print("\nType-Token Ratio:")
        print(f"{hasil[3]:.4f} atau {hasil[3] * 100:.2f}%")

    except FileNotFoundError:
        print("File teks.txt tidak ditemukan.")

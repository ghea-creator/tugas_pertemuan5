
def analisis_nilai(daftar_nilai):
    # Menghitung rata-rata
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)

    # Menentukan nilai tertinggi dan terendah
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    # Membuat dictionary untuk frekuensi kategori
    frekuensi = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0
    }

    # Mengelompokkan nilai berdasarkan kategori
    for nilai in daftar_nilai:
        if nilai >= 85:
            kategori = "A"
        elif nilai >= 75:
            kategori = "B"
        elif nilai >= 65:
            kategori = "C"
        elif nilai >= 50:
            kategori = "D"
        else:
            kategori = "E"

        frekuensi[kategori] += 1

    return rata_rata, nilai_tertinggi, nilai_terendah, frekuensi


if __name__ == "__main__":
    input_nilai = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")

    daftar_nilai = [float(nilai) for nilai in input_nilai.split(",")]

    if not daftar_nilai:
        print("Daftar nilai tidak boleh kosong.")
    else:
        hasil = analisis_nilai(daftar_nilai)

        print("\n=== HASIL ANALISIS NILAI ===")
        print("Daftar nilai     :", daftar_nilai)
        print("Rata-rata        :", round(hasil[0], 2))
        print("Nilai tertinggi  :", hasil[1])
        print("Nilai terendah   :", hasil[2])

        print("\nFrekuensi kategori:")
        for kategori, jumlah in hasil[3].items():
            print(f"Kategori {kategori}: {jumlah} mahasiswa")

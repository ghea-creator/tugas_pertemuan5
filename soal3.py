
def analisis_beasiswa(beasiswa_a, beasiswa_b):
    # Mengubah list menjadi set
    set_a = set(beasiswa_a)
    set_b = set(beasiswa_b)

    # Mahasiswa yang menerima kedua beasiswa
    kedua_beasiswa = set_a & set_b

    # Mahasiswa yang hanya menerima beasiswa A
    hanya_a = set_a - set_b

    # Mahasiswa yang menerima B tetapi tidak A
    hanya_b = set_b - set_a

    # Semua mahasiswa unik penerima beasiswa
    semua_penerima = set_a | set_b

    return kedua_beasiswa, hanya_a, hanya_b, semua_penerima


if __name__ == "__main__":
    beasiswa_a = ["001", "002", "003", "004", "005"]
    beasiswa_b = ["003", "004", "005", "006", "007"]

    hasil = analisis_beasiswa(beasiswa_a, beasiswa_b)

    print("=== ANALISIS PENERIMA BEASISWA ===")
    print("Penerima beasiswa A:", beasiswa_a)
    print("Penerima beasiswa B:", beasiswa_b)

    print("\nMahasiswa penerima kedua beasiswa:", sorted(hasil[0]))
    print("Mahasiswa yang hanya menerima A:", sorted(hasil[1]))
    print("Mahasiswa yang menerima B tetapi tidak A:", sorted(hasil[2]))
    print("Semua mahasiswa unik penerima beasiswa:", sorted(hasil[3]))

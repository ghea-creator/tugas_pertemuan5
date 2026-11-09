
# Dictionary untuk menyimpan data inventaris
# Nama barang sebagai kunci, (harga, stok) sebagai nilai
inventaris = {
    "Buku": (10000, 20),
    "Pulpen": (3000, 50),
    "Pensil": (2000, 30),
    "Penghapus": (1500, 25)
}


# Fungsi menambahkan barang baru
def tambah_barang(nama, harga, stok):
    if nama in inventaris:
        return "Barang sudah tersedia."

    inventaris[nama] = (harga, stok)
    return "Barang berhasil ditambahkan."


# Fungsi memperbarui stok barang
def update_stok(nama, stok_baru):
    if nama not in inventaris:
        return "Barang tidak ditemukan."

    harga = inventaris[nama][0]
    inventaris[nama] = (harga, stok_baru)

    return "Stok berhasil diperbarui."


# Fungsi mencari barang berdasarkan rentang harga
def cari_barang(min_harga, max_harga):
    hasil = {}

    for nama, (harga, stok) in inventaris.items():
        if min_harga <= harga <= max_harga:
            hasil[nama] = (harga, stok)

    return hasil


# Fungsi menghitung total nilai inventaris
def total_inventaris():
    total = 0

    for harga, stok in inventaris.values():
        total += harga * stok

    return total


if __name__ == "__main__":
    print("=== SISTEM INVENTARIS TOKO ===")

    # Menampilkan data awal
    print("\nData inventaris awal:")
    for nama, (harga, stok) in inventaris.items():
        print(f"{nama}: Harga Rp{harga}, Stok {stok}")

    # Menambahkan barang baru
    print("\n", tambah_barang("Tas", 50000, 10))

    # Mengupdate stok
    print(update_stok("Buku", 30))

    # Mencari barang berdasarkan rentang harga
    print("\nBarang dengan harga Rp2.000 - Rp15.000:")
    hasil_cari = cari_barang(2000, 15000)

    for nama, (harga, stok) in hasil_cari.items():
        print(f"{nama}: Harga Rp{harga}, Stok {stok}")

    # Menghitung total nilai inventaris
    print("\nTotal nilai inventaris: Rp", total_inventaris())

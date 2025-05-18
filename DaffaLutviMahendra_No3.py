import sys

inventaris = {}

def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Barang Baru")
    print("2. Tampilkan Semua Barang")
    print("3. Cari Barang")
    print("4. Perbarui stok Barang")
    print("5. hapus Barang")
    print("6. Analisis Data")
    print("7. keluar")
    
def tambah_barang():
    nama_barang = input("Masukkan nama barang: ").strip()
    if nama_barang in inventaris:
        print(f"Barang '{nama_barang}' sudah ada dalam inventaris.")
        return
    try:
        harga_barang = float(input("Masukkan harga barang: "))
        stok_barang = int(input("Masukkan jumlah stok barang: "))
        inventaris[nama_barang] = {
            "harga": harga_barang,
            "stok": stok_barang
        }
        print(f"Barang '{nama_barang}' berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Pastikan harga adalah angka dan stok adalah bilangan bulat.")
        
def tampilkan_semua_barang():
    if not inventaris:
        print("Inventaris kosong.")
        return
    print("=== Daftar Inventaris ===")
    print(f"{'Nama Barang':<20} {'Harga':<10} {'Stok':<10}")
    print("=" * 40)
    for nama_barang, data in inventaris.items():
        print(f"{nama_barang:<20} {data['harga']:<10} {data['stok']:<10}")
        
def cari_barang():
    nama_barang = input("Masukkan nama barang yang dicari: ").strip()
    if nama_barang in inventaris:
        data = inventaris[nama_barang]
        print(f"Barang '{nama_barang}' ditemukan. Harga: {data['harga']}, Stok: {data['stok']}")
    else:
        print(f"Barang '{nama_barang}' tidak ditemukan dalam inventaris.")
        
def perbarui_stok():
    nama_barang = input("Masukkan nama barang yang ingin diperbarui: ").strip()
    if nama_barang in inventaris:
        try:
            stok_baru = int(input("Masukkan jumlah stok baru: "))
            inventaris[nama_barang]['stok'] = stok_baru
            print(f"Stok barang '{nama_barang}' berhasil diperbarui.")
        except ValueError:
            print("Input tidak valid. Pastikan stok adalah bilangan bulat.")
    else:
        print(f"Barang '{nama_barang}' tidak ditemukan dalam inventaris.")
        
def hapus_barang():
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ").strip()
    if nama_barang in inventaris:
        del inventaris[nama_barang]
        print(f"Barang '{nama_barang}' berhasil dihapus dari inventaris.")
    else:
        print(f"Barang '{nama_barang}' tidak ditemukan dalam inventaris.")
        
def analisis_data():
    if not inventaris:
        print("Inventaris kosong.")
        return
    total_barang = len(inventaris)
    total_stok = sum(data['stok'] for data in inventaris.values())
    total_harga = sum(data['harga'] * data['stok'] for data in inventaris.values())
    
    print(f"Total barang dalam inventaris: {total_barang}")
    print(f"Total stok barang: {total_stok}")
    print(f"Total nilai inventaris: {total_harga}")
    
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-7): ").strip()
    
    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        tampilkan_semua_barang()
    elif pilihan == '3':
        cari_barang()
    elif pilihan == '4':
        perbarui_stok()
    elif pilihan == '5':
        hapus_barang()
    elif pilihan == '6':
        analisis_data()
    elif pilihan == '7':
        print("Terima kasih! Program selesai.")
        sys.exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
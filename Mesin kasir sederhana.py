#import library random
import random

# Mendefinisikan fungsi-fungsi yang dipakai
def konversi_idr_ke_usd(jumlah_idr):
    """
    Fungsi mengonversikan jumlah uang dalam IDR ke USD
    """
    jumlah_usd = jumlah_idr/15000
    return round(jumlah_usd, 2)

def konversi_usd_ke_idr(jumlah_usd):
    """
    Fungsi mengonversikan jumlah uang dalam USD ke IDR
    """
    jumlah_idr = jumlah_usd * 15000
    return jumlah_idr

def konversi_idr_ke_krw(jumlah_idr):
    """
    Fungsi mengonversikan jumlah uang dalam IDR ke KRW
    """
    jumlah_krw = jumlah_idr/10
    return round(jumlah_krw, 2)

def konversi_krw_ke_idr(jumlah_krw):
    """
    Fungsi mengonversikan jumlah uang dalam KRW ke IDR
    """
    jumlah_idr = jumlah_krw * 10
    return jumlah_idr


print("Selamat datang di SisateNG, Dek Depe!")

banyak_menu = int(input("Banyak menu yang diinginkan: "))

nama_menu_list = []
harga_menu_list = []

for i in range (1, banyak_menu + 1):
   menu = input(f"menu {i} ((nama menu) (harga)): ")
   nama_menu_split = menu.split()
   nama_menu  = nama_menu_split[0]
   nama_menu_list.append(nama_menu)
   harga_menu_split = menu.split()
   harga_menu = harga_menu_split[1]
   harga_menu_list.append(harga_menu)

print("Selamat datang di stan sate Pachill, pelanggan!")

print("Menu SisateNG:")
for i in range (1, banyak_menu+1):
    nama_menu = nama_menu_list[i-1]
    harga_menu = harga_menu_list[i-1]
    print(f"{i}. {nama_menu} - Rp {harga_menu}")
print("-------------------------------------------------------")

jumlah_pesanan = int(input("Masukkan jumlah pesanan yang akan dibeli: "))

# # nilai awal
nama_pesanan_list = []
banyak_pesanan_list = []
total_harga_idr = 0

# Meminta input banyak tusuk sate di tiap pesanan
for i in range(1,jumlah_pesanan+1):
    print(f"-PESANAN {i}-")
    nama_pesanan = input("Masukkan menu yang akan dipesan: ")
    banyak_pesanan = input(f"Berapa banyak {nama_pesanan} yang ingin Anda beli untuk pesanan {i}: ")
    if banyak_pesanan == "RANDOM":
        banyak_pesanan = random.randint(1, 21)
    else:
        banyak_pesanan = int(banyak_pesanan)
    print(f"Banyak {nama_pesanan} yang dipesan pada pesanan {i} adalah {banyak_pesanan}.")
    

    # TODO: Memasukkan nama pesanan dan jumlah pesanan ke dalam list yang sesuai
    nama_pesanan_list.append(nama_pesanan)
    banyak_pesanan_list.append(banyak_pesanan)
    
    # TODO: Menghitung harga pesanan dengan iterate ke dalam menu
    for menu in nama_menu_list:
     # Jika nama pesanan sama dengan nama menu, maka akan mendapatkan harga menu sesuai indeks
        if menu == nama_pesanan: 
            index_menu = nama_menu_list.index(menu)
            harga_menu = harga_menu_list[index_menu]
            
            # Menambahkan total harga
            total_harga_idr += int(harga_menu) * banyak_pesanan

# Mencetak Ringkasan Data
print("-RINGKASAN DATA-")
print(f"Berikut ringkasan hasil pembelian Sate Pachill dari {jumlah_pesanan} pesanan.")
print("Menu yang dipesan:")
for i in range(0, jumlah_pesanan):
    print(f"{i+1}. {banyak_pesanan_list[i]} {nama_pesanan_list[i]}")

# Mencetak total harga sesuai currency yang dipilih
total_harga_baru = 0
currency_biaya = input("Pilih mata uang untuk ditampilkan pada total harga (IDR/USD/KRW): ")
if currency_biaya == "USD":
    total_harga_baru = konversi_idr_ke_usd(total_harga_idr)
    print(f"Biaya yang perlu dibayar sebesar USD {total_harga_baru} \n")
elif currency_biaya == "KRW":
    total_harga_baru = konversi_idr_ke_krw(total_harga_idr)
    print(f"Biaya yang perlu dibayar sebesar KRW {total_harga_baru} \n")
else:
    total_harga_baru = total_harga_idr
    print(f"Biaya yang perlu dibayar sebesar IDR {total_harga_baru} \n")

# Memproses Check Out
print("-CHECK OUT-")

# Meminta input currency pembayaran dan kembalian
currency_bayar = input("Pilih mata uang pembayaran (IDR/USD/KRW): ")
currency_kembalian = input("Pilih mata uang kembalian (IDR/USD/KRW): ")
jumlah_pembayaran_idr = 0
jumlah_kembalian_idr = 0

if currency_bayar == "USD":
    jumlah_pembayaran_usd = float(input("Masukkan jumlah pembayaran Anda (dalam USD): "))
    jumlah_pembayaran_idr = konversi_usd_ke_idr(jumlah_pembayaran_usd)
elif currency_bayar == "KRW":
    jumlah_pembayaran_krw = float(input("Masukkan jumlah pembayaran Anda (dalam KRW): "))
    jumlah_pembayaran_idr = konversi_krw_ke_idr(jumlah_pembayaran_krw)
else:
    jumlah_pembayaran_idr = float(input("Masukkan jumlah pembayaran Anda (dalam IDR): "))
print()

# Memproses output
if total_harga_idr > jumlah_pembayaran_idr :
    print("Mohon maaf pembayaran Anda tidak cukup!")
elif total_harga_idr == jumlah_pembayaran_idr :
    print("Selamat menikmati makanan Anda")
else:
    print("Selamat menikmati makanan Anda")

    jumlah_kembalian_idr = jumlah_pembayaran_idr - total_harga_idr
    if currency_kembalian == "USD":
        print(f"Total kembalian Anda adalah USD {konversi_idr_ke_usd(jumlah_kembalian_idr)}")
    elif currency_kembalian == "KRW":
        print(f"Total kembalian Anda adalah KRW {konversi_idr_ke_krw(jumlah_kembalian_idr)}")
    else:
        print(f"Total kembalian Anda adalah IDR {round(jumlah_kembalian_idr, 2)}")

# Mencetak pesan terima kasih
print("Terima kasih telah berbelanja di SisateNG!")
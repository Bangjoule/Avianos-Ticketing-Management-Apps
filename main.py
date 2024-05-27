import random
import string

def generate_ticket_id():
    letters = string.ascii_uppercase
    digits = string.digits
    idPass = random.choice(letters) + "".join(random.choices(digits, k=9))
    return idPass

def cek_jadwal(ticket_id, tickets):
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
            return ticket
    return None

tickets = []

while True:
    print("==============AVIANOS================")
    print("Welcome Avianos, heh. You can choose just two departs from here, bozzo~")
    print("Menu:")
    print("1. Memasukkan Biodata dan Memesan Tiket")
    print("2. Mengecek Jadwal Penerbangan")
    print("3. Menambahkan Barang Bawaan")
    print("4. Menambahkan Makanan")
    print("5. Melakukan Pembayaran")
    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        print("Pilih jenis penerbangan:")
        print("1. Domestik")
        print("2. Internasional")
        flight_type = input("Masukkan pilihan Anda: ")

        if flight_type == "1":
            print("Masukkan Biodata terlebih dahulu")
            bioName = input("Silahkan tulis nama lengkap: ")
            bioDom = input("Silahkan masukan kota asal: ")
            idcard = input("Silahkan masukan nomor KTP anda: ")
            try:
                idcard = int(idcard)
            except ValueError:
                print("Nomor KTP harus berupa angka. Mengarahkan kembali ke menu utama.")
                continue

        elif flight_type == "2":
            print("Masukkan Biodata terlebih dahulu")
            bioName = input("Silahkan tulis nama lengkap: ")
            bioDom = input("Silahkan masukan negara asal: ")
            idcard = input("Silahkan masukan nomor Paspor anda: ")

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 (Domestik) atau 2 (Internasional).")
            retry_flight_type = input("Apakah Anda ingin memilih ulang jenis penerbangan? [Yes/No]").strip().lower()
            if retry_flight_type != "yes":
                print("Mengarahkan kembali ke menu utama.")
                continue

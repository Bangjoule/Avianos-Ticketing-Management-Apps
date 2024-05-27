while True:
    print("==============AVIANOS================")
    print("Welcome to our very narcistic Ticketing Apps, heh. You can choose just two departs from here, bozzo~")
    print("Menu:")
    print("1. Memasukkan Biodata dan Memesan Tiket")
    print("2. Mengecek Jadwal Penerbangan")
    print("3. Menambahkan Barang Bawaan")
    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        print("Pilih jenis penerbangan:")
        print("1. Domestik")
        print("2. Internasional")
        flight_type = input("Masukkan pilihan Anda: ")
print ("hola")
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

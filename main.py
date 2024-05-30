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
while True:
            print(f"Selamat datang, {bioName}. Mau kemana kita hari ini?")
            
            if flight_type == "1":
                print("1. Bandung")
                print("2. Jogja")
                print("3. Denpasar")
                print("4. Jayapura")
                print("5. Batam")
                print("6. Pontianak")
                print("7. Surabaya")
                print("8. Semarang")
                print("9. Sulawesi")
                print("10. Labuan Bajau")
            elif flight_type == "2":
                print("11. Singapura")
                print("12. Australia")
                print("13. Thailand")
                print("14. Brunei")
                print("15. Jepang")
                print("16. Arab")
                print("17. Cina/Beijing")
                print("18. Kamboja")
                print("19. Malaysia")
                print("20. Filipina")
                print("21. Myanmar")
                print("22. Vietnam")
                print("23. Laos")
                print("24. Turki")
                print("25. Korea Selatan")
            
            selection = int(input("Silahkan pilih destinasi yang ingin dituju: "))
            
            if flight_type == "1" and selection > 10:
                print("Maaf, pilihan tersebut tidak ada pada opsi domestik.")
                retry = input("Apakah Anda ingin memilih ulang destinasi? [Yes/No]").strip().lower()
                if retry == "yes":
                    continue
                else:
                    print("Mengarahkan kembali ke menu utama.")
                    break
            elif flight_type == "2" and selection <= 10:
                print("Maaf, pilihan tersebut tidak ada pada opsi internasional.")
                retry = input("Apakah Anda ingin memilih ulang destinasi? [Yes/No]").strip().lower()
                if retry == "yes":
                    continue
                else:
                    print("Mengarahkan kembali ke menu utama.")
                    break

            destination_prices = {
                1: ("Bandung", 800000),
                2: ("Jogja", 900000),
                3: ("Denpasar", 950000),
                4: ("Jayapura", 1500000),
                5: ("Batam", 700000),
                6: ("Pontianak", 650000),
                7: ("Surabaya", 850000),
                8: ("Semarang", 800000),
                9: ("Sulawesi", 1300000),
                10: ("Labuan Bajau", 1400000),
                11: ("Singapura", 2500000),
                12: ("Australia", 5000000),
                13: ("Thailand", 3000000),
                14: ("Brunei", 3500000),
                15: ("Jepang", 5500000),
                16: ("Arab", 8500000),
                17: ("Cina/Beijing", 5000000),
                18: ("Kamboja", 3500000),
                19: ("Malaysia", 2750000),
                20: ("Filipina", 4000000),
                21: ("Myanmar", 3250000),
                22: ("Vietnam", 3500000),
                23: ("Laos", 3750000),
                24: ("Turki", 10000000),
                25: ("Korea Selatan", 7750000)
            }

            if selection in destination_prices:
                destination, price = destination_prices[selection]
                print(f"Penerbangan ke {destination} untuk penumpang bernama {bioName} dengan asal {bioDom}, apakah yakin ingin melanjutkan dengan opsi ini? [Yes/No]")
                confirm = input("[Yes/No]").strip().lower()
                if confirm == "yes":
                    print(f"Penerbangan anda sudah dikonfirmasi dengan harga Rp. {price:,.2f}")
                    ticket_id = generate_ticket_id()
                    print("Your ticket ID is:", ticket_id)
                    tickets.append({
                        'ticket_id': ticket_id,
                        'name': bioName,
                        'origin': bioDom,
                        'destination': destination,
                        'price': price,
                        'baggage': None,
                        'food': [],
                        'food_price': 0
                    })
                    break
                else:
                    print("Penerbangan dibatalkan.")
                    break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

elif choice == "2":
        ticket_id = input("Masukkan Ticket ID Anda: ")
        ticket = cek_jadwal(ticket_id, tickets)
        if ticket:
            print(f"Ticket ID: {ticket['ticket_id']}")
            print(f"Nama Penumpang: {ticket['name']}")
            print(f"Kota/Negara Asal: {ticket['origin']}")
            print(f"Tujuan: {ticket['destination']}")
            print(f"Harga: Rp. {ticket['price']:,.2f}")
            if ticket['baggage']:
                print(f"Barang Bawaan: {ticket['baggage']['weight']} kg dengan harga Rp. {ticket['baggage']['price']:,.2f}")
            else:
                print("Anda tidak membawa barang apa-apa.")
            if ticket['food']:
                print("Makanan: ", ", ".join(ticket['food']))
                print(f"Total Harga Makanan: Rp. {ticket['food_price']:,.2f}")
            else:
                print("Anda tidak memesan makanan.")
        else:
            print("Ticket ID tidak ditemukan.")

elif choice == "3":
        ticket_id = input("Masukkan Ticket ID Anda: ")
        ticket = cek_jadwal(ticket_id, tickets)
        if ticket:
            print("Pilih opsi barang bawaan yang ingin dibawa:")
            options = {
                1: {'weight': 20, 'price': 300000},
                2: {'weight': 25, 'price': 337500},
                3: {'weight': 30, 'price': 375000},
                4: {'weight': 35, 'price': 412500}
            }

            for key, option in options.items():
                print(f"{key}. {option['weight']} kg dengan harga Rp. {option['price']:,.2f}")

            while True:
                try:
                    choice = int(input("Masukkan nomor pilihan (ketik '0' jika ingin batal): ").strip())
                    if choice == 0:
                        print("Pembatalan pilihan barang bawaan.")
                        break
                    elif choice in options:
                        selected_option = options[choice]
                        ticket['baggage'] = {'weight': selected_option['weight'], 'price': selected_option['price']}
                        print(f"Barang bawaan {selected_option['weight']} kg dengan harga Rp. {selected_option['price']:,.2f} telah ditambahkan.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
                except ValueError:
                    print("Input tidak valid. Silakan masukkan nomor yang sesuai.")
        else:
            print("Ticket ID tidak ditemukan.")

# Task 2: Data Type Conversion and User Input

jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")

jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")

print("Tipe data awal jumlah kopi:", type(jumlah_kopi_str))
print("Tipe data awal jumlah roti:", type(jumlah_roti_str))

jumlah_kopi_int = int(jumlah_kopi_str)
jumlah_roti_int = int(jumlah_roti_str)

print("Tipe data setelah konversi:", type(jumlah_kopi_int))
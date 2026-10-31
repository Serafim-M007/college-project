#1. konversi dari str ke int
angka_str = "100"
angka_int = int(angka_str)
print("Konversi dari str ke int:", angka_int + 1000)
print()

#2. konversi dari float ke int
ipk_float = 3.85
ipk_int = int(ipk_float)
print("Konversi dari float ke int:", ipk_int)
print()

#3. konversi dari int ke str
tahun_ini = 2026
pesan = "Tahun ini adalah " + str(tahun_ini)
print(pesan)
print()

#4. konversi dari list ke set(menghapus duplikat)
daftar_angka = [1, 2, 3, 4, 5, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6]
angka_set = set(daftar_angka)
print("Konversi dari list ke set:", angka_set)
print()
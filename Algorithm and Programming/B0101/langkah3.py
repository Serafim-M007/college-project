#1. LIST (Berurutan, bisa dirubah/mutable)
hobi = ["Membaca", "Menulis", "Berenang", "Bersepeda"]
print("Hobi:", hobi)
print("Tipe:", type(hobi))
print()

#2 TUPLE (Berurutan, tidak bisa dirubah/immutable)
koordinat = (-6.3456, 106.7890)
print("Tuple Koordinat:", koordinat)
print("Tipe:", type(koordinat))
print()

#3. Dictionary (Berpasangan, bisa dirubah/mutable  key:value)
mahasiswa = {
    "nama": "Serafim",
    "nim": 12,
    "ipk" : 4.0
}

print("Data Mahasiswa:", mahasiswa)
print("Tipe:", type(mahasiswa))
print()

#4. Set (Unik, tidak berurutan, tidak bisa dirubah/immutable)
number_set = {1, 2, 3, 4, 5, 5, 4, 3}
print("Set Angka:", number_set)
print("Tipe:", type(number_set))
print()
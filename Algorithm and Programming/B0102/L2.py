# 3. Konversi tipe data (type casting)
from L1 import str_nilai_algoritma, str_nilai_basis_data, str_pemrograman_web, sks_per_matkul, is_aktif

nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_pemrograman_web)

#4. Kalkulasi menggunakan variabel
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

# Peneteuan kelulusan semester (Boolean)
# Lulus jika rata-rata nilai >= 75.0 dan status mahasiswa aktif
is_lulus_semester = rata_rata_nilai >= 75.0 and is_aktif

print("\n--HASIL EVALUASI AWAL --")
print(f"Total Nilai: {total_nilai}")
print(f"Rata-rata Nilai: {rata_rata_nilai}")
print(f"Total SKS Diambil: {total_sks_diambil}")
print(f"Kelulusan Semester: {is_lulus_semester}")
# 6. UPDATE VARIABEL DINAMIS
import L3 as dl3
import L2 as dl2

# Mahasiswa mengambil 1 matkul susulan
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5  #NILAI AB

print()
print()
# A. TAMBAHKAN KE LIST
dl3.daftar_matkul.append(matkul_baru)

# B. TAMBAHKAN KE DICTIONARY
dl3.transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi variabel total dan rata-rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = dl2.total_nilai + nilai_jk        #MEMPERBARUI NILAI total_nilai
jumlah_matkul = len(dl3.daftar_matkul)  #MEMPERBARUI jumlah_matkul
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung indeks prestasi kumulatif (IPK) dari dictionary mutu
total_bobot_mutu = sum(dl3.transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL --")
print("Daftar MAtkul Terbaru:", dl3.daftar_matkul)
print("Jumlah Matkul Total:", jumlah_matkul)
print("Rata-rata Angka Baru:", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4):", round(ipk_sementara, 2))
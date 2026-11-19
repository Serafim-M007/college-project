import time

#catat waktu mulai
waktu_mulai = time.perf_counter()

#Kode yang ingin diukur
total = 0
for i in range(10000):
    total += i
    print(i)

#catat waktu selesai
waktu_selesai = time.perf_counter()

#Hitung selisih waktu
lama_eksekusi = waktu_selesai - waktu_mulai

print(f"Hasil perhitungan: {total}")
print(f"Lama waktu eksekusi: {lama_eksekusi:.6f} detik")
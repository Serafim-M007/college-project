import time

class PerekamWaktu:
    def __enter__(self):
        self.mulai = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.selesai = time.perf_counter()
        self.durasi = self.selesai - self.mulai
        print(f"Blok kode selesai dieksekusi dalam {self.durasi:.6f} detik")

#Contoh penggunaan
with PerekamWaktu():
    daftar_kata = [str(x) for x in range(1000)]
    teks = " ".join(daftar_kata)

print(teks)
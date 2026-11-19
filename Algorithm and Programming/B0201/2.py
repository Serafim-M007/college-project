import time
from functools import wraps

def ukur_waktu(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Catat waktu mulai
        mulai = time.perf_counter()
        
        # Panggil fungsi yang ingin diukur
        hasil = func(*args, **kwargs)
        
        # Catat waktu selesai
        selesai = time.perf_counter()
        
        # Hitung selisih waktu
        durasi = selesai - mulai
        
        print(f"Fungsi '{func.__name__}' dieksekusi dalam {durasi:.6f} detik")

        return hasil
    
    return wrapper

@ukur_waktu
def hitung_kuadrat(n):
    return [i **2 for i in range(n)]

@ukur_waktu
def simulasi_proses ():
    time.sleep(2)

hitung_kuadrat(100)
simulasi_proses()
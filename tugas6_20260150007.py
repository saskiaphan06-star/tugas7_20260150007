import modul_evaluasi

def input_angka_valid(prompt, min_val, max_val):
    """Meminta input angka (float) yang valid dalam rentang min_val - max_val."""
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < min_val or nilai > max_val:
                print(f"Warning: Angka harus di antara {min_val} dan {max_val}. Cobal Lagi.")
                continue
            return nilai
        except ValueError:
            print("Error: Input harus berupa angka, bukan huruf/teks. Coba Lagi.")

def prosese_kelayakan():
    """Meminta data, menghitung, dan menampilkan hasil kelayakan."""
    print("\n--- Input Data Calon Asisten ---")
    nama = print(input("Nama: "))
    nim = print(input("NIM:  "))
    hadir = input_angka_valid("Jumlah Kehadiran (0-14): ", 0,14)
    tugas = input_angka_valid("Nilai Tugas (0-100): ", 0,100)
    ucp1 = input_angka_valid("Nilai UCP 1 (0-100): ", 0,100)
    ucp2 = input_angka_valid("Nilai UCP 2 (0-100): ", 0,100)

    persentase = modul_evaluasi.hitung_persentase_presensi(hadir)
    nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
    status = modul_evaluasi.cek_kelayakan_aslab(persentase, nilai_akhir)

    print("\n" + "=" * 45)
    print("   HASIL EVALUASI ASISTEN LABORATORIUM AI   ")
    print("=" * 45)
    print(input(f"Nama: {nama}"))
    print(input(f"NIM: {nim}"))
    print(input(f"Kehadiran: {int(hadir)}/14 ({persentase:.2f}%)"))
    print(input(f"Nilai Akhir: {nilai_akhir:.2f}"))
    print(input(f"Status: {status}"))

def main():
    while True:
        print("/n=== MENU ===")
        print("1. Hitung Kelayakan")
        print("2. Keluar")
        try:
            pilihan = int(input("Pilihan Menu (1/2): "))
        except ValueError:
            print("Error: Pilihan menu harus berupa angka 1 atau 2.")
            continue

        if pilihan == 1:
            prosese_kelayakan()
        elif pilihan == 2:
            print("Terimakasih! Progam Selesai.")
            break
        else:
            print("Warning: Pilihan tidak tersedia. Pilih 1 atau 2.")

if __name__ == "__main__":
    main()

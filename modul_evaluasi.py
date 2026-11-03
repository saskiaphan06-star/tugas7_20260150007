"""Modul Logika Sistem Evalusi Kelayakan Asistem Laboratorium AI.

File ini hanya berisi fungsi (tanpa input() dan print() utama).
"""

def hitung_persentase_presensi(hadir, total_pertemuan=14):
    """Menghitung persentase kehadiran."""
    return (hadir / total_pertemuan) * 100

def hitung_nilai_akhir(tugas, ucp1, ucp2):
    """Menghitung tugas akhir: Tugas 20%, UCP 1 40%, UCP 2 40%."""
    return(tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)

def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    """Mengembalikan status kelayakan calon asisten Laboratorium."""
    if persentase_presensi < 75.0:
        return "DITOLAK (Kehadiran dibawah 75%)"
    elif nilai_akhir >= 75.0:
        return "DITERIMA (Memenuhi syarat)"
    else:
        return "DITOLAK (Nilai akhir kurang)"
    
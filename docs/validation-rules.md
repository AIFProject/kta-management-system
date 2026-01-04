# Validation Rules
Aturan validasi data anggota

## Validasi Kolom Wajib
Data DITOLAK jika salah satu kolom kosong
 - nama_lengkap
 - jenis_kelamin
 - tanggal_lahir
 - organisasi
 - ranting 
 - tahun_masuk

## Validasi Format
jenis kelamin
 - Hanya: L atau P
organisasi
 - Hanya: IPNU dan IPPNU
tanggal_lahir
 - Format: YYYY-MM-DD
 - Tidak boleh tanggal masa depan
tahun_masuk
 - 4 digit angka
 - Tidak boleh lebih dari tahun sekarang
no_hp
 - angka_saja
 - panjang 10-13 digit

## Validasi Konsistensi
 - IPNU -> jenis_kelamin harus L
 - IPPNU -> jenis_kelamin harus P
(jika tidak sesuai -> data ditandai, bukan langsung dihapus)

## Deteksi Duplikasi
Data dianggap duplikat jika:
 - nama_lengkap + tanggal_lahir sama
 - organisasi sama
Duplikat:
 - Tidak dihapus
 - Ditandai untuk dicek manual

## Status Validasi
Setiap baris data punya status:
 - valid
 - invalid
 - duplicate
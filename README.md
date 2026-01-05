# KTA Management System

Sistem pengelolaan data dan Kartu Tanda Anggota (KTA) IPNU-IPPNU tingkat kecamatan berbasis pengolahan data.

Project ini dirancang untuk membantu pengurus orgnaisasi dalam mengelola data secara terstruktur, tervalidasi, dan siap digunakan untuk kebutuhan pelaporan serta penerbitan KTA.

---

## 🎯 Objectives
 - Menstandarkan format data anggota dari seluruh ranting
 - Melakukan validasi dan pembersihan data
 - Mencegah duplikasi data anggota
 - Menghasilkan nomor KTA secara otomatis dan terstruktur
 - Menyediakan laporan keanggotan yang siap digunakan

---

## 🧩 Problem Context
Pendataan anggota IPNU-IPPNU sering dilakukan secara terpisah dengan format yang berbeda-beda, sehingga menyulitkan proses rekapitulasi dan pembuatan KTA.

Project ini hadir sebagai solusi **data-centric** yang fokus pada: 
 - konsistensi
 - akurasi
 - keterlacakan data

---

## 🏗️ Project Structure
kta-management-system/
├── data/
├─├── raw/ # Data asli (tidak di-commit)
├─├── template/ # Template CSV standar
├─├── sample/ # Data dummy untuk testing
├─├── validated/ # Data hasil validasi
├─├── ready_for_kta/ # Data siap cetak KTA
├─├── reports/ # Laporan keanggotaan
|
├─├── docs/ # Dokumentasi sistem
├── scripts/
├─├── validation/ # Validasi data
├─├── processing/ # Generate nomor KTA
├─├── reporting/ # Rekap laporan
|
└── README.md

---

## ⚙️ Tech Stack
 - **Python** - data processing & automation
 - **Pandas** - data validation & transformation
 - **CSV / Excel** - data interchange
 - **Markdown** - documentation

Project ini tidakk menggunakan framework frontend/backend
karena difokuskan pada **manajemen dan kualitas data**.

---

## 🔁 Workflow Overview
CSV dari ranting
↓
Validasi & Cleaning Data
↓
Deteksi Duplikasi
↓
Generate Nomor KTA
↓
Laporan & Data Siap Cetak

---

## 🚀 Features
 - Validasi kolom wajib & format data
 - Deteksi data duplikat
 - Penomoran KTA otomatis
 - Rekap anggota per ranting & organisasi
 - Output data siap cetak dan laporan

---

## 📊 Sample Output
 - `validated_members.csv`
 - `report_jumlah_per_ranting.csv`
 - `report_status_validasi.csv`
 - `anggota_siap_KTA.csv`

---

## 📌 Project Status
**In development**
Data pipeline dan core logic telah selesai dan siap digunakan.

---

## 👤 Author
**MH. Abyan Siddiqi**
Mahasiswa Teknik Informatika
Fokus pada data management & system-oriented development
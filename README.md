# Prediksi Harga Ikan Segar di Sulawesi Tengah Menggunakan Regresi Linear

## Deskripsi

Proyek ini dibuat sebagai tugas mata kuliah Statistik dan Probabilitas. Tujuan dari proyek ini adalah menganalisis faktor-faktor yang memengaruhi harga ikan segar di Sulawesi Tengah serta membuat model prediksi harga menggunakan metode Regresi Linear.

Data yang digunakan terdiri dari beberapa variabel yang dianggap berpengaruh terhadap harga ikan, seperti jenis ikan, berat ikan, kondisi cuaca, jumlah stok yang tersedia, tingkat permintaan pasar, dan lokasi penjualan. Dari data tersebut dibuat model regresi untuk memprediksi harga ikan berdasarkan kondisi yang ada.

## Dataset

Dataset yang digunakan berisi data harga ikan segar dengan beberapa atribut yang memengaruhi harga jual di pasar.

### Variabel Input (X)

* Jenis Ikan
* Berat Ikan (Kg)
* Cuaca
* Stok
* Permintaan
* Lokasi Pasar

### Variabel Output (Y)

* Harga Ikan (Rp)

## Metode yang Digunakan

Metode yang digunakan pada penelitian ini adalah Regresi Linear Berganda. Metode ini dipilih karena dapat digunakan untuk mengetahui hubungan antara beberapa variabel independen dengan satu variabel dependen, yaitu harga ikan.

Tahapan yang dilakukan dalam analisis meliputi:

1. Membaca dan memahami dataset.
2. Melakukan analisis deskriptif.
3. Mengubah data kategorik menjadi data numerik menggunakan One-Hot Encoding.
4. Membagi data menjadi data training dan testing.
5. Melatih model regresi linear.
6. Melakukan prediksi harga ikan.
7. Mengevaluasi hasil model menggunakan MAE, RMSE, dan R² Score.
8. Menampilkan hasil dalam bentuk grafik.

## Tools yang Digunakan

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

## Hasil yang Diperoleh

Dari model yang dibuat, diperoleh prediksi harga ikan berdasarkan faktor-faktor yang terdapat pada dataset. Selain itu, dilakukan evaluasi model untuk melihat tingkat akurasi prediksi menggunakan beberapa metrik statistik.

Visualisasi yang dihasilkan antara lain:

* Distribusi harga ikan
* Grafik perbandingan harga aktual dan harga prediksi
* Grafik pengaruh masing-masing variabel terhadap harga ikan

## Struktur Folder

```text
Prediksi-Harga-Ikan-Sulteng/
│
├── dataset_harga_ikan_sulteng.csv
├── prediksi_harga_ikan.py
├── README.md
```

## Tujuan Proyek

* Menerapkan konsep regresi linear pada data nyata.
* Mengetahui faktor yang memengaruhi harga ikan segar.
* Membuat model prediksi harga ikan menggunakan Python.
* Melatih kemampuan analisis data dan visualisasi.

## Penulis

Nadin Putri Sugianto
F5212510022
Sistem Informasi - Universitas Tadulako
Mata Kuliah Statistik dan Probabilitas

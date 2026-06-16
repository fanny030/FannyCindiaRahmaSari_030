Judul: Jumlah Keluarga Penerima Manfaat (KPM) dan Anggaran Bantuan Sosial Pangan Menurut Provinsi sulawesi tengah, (BPS) badan pusat statistik

Nama: Fanny Cindia Rahma Sari_F5212510030

Mata kuliah: Statistika dan Probabilitas

Studi kasus: Menganalisis pengaruh beberapa variabel pada data penerima manfaat terhadap Realisasi Anggaran menggunakan metode Multiple Linear Regression.

Dataset: Data diperoleh dari file penerima_manfaat_bersih.csv yang telah melalui proses pembersihan data (data cleaning) sehingga siap digunakan untuk analisis dan pemodelan.(BPS) badan pusat statistik Sulawesi Tengah

Variabel: X (Variabel Independen)
1.Kolom ke-2 pada dataset
2.Kolom ke-3 pada dataset
3.Kolom ke-4 pada dataset
Y (Variabel Dependen)
Y=a+b1​X1​+b2​X2​+b3​X3​
1.Kolom ke-5 pada dataset (Realisasi Anggaran)

Jumlah data: 100 data observasi (14 kabupaten/kota,2018-2025), Sesuai jumlah observasi yang terdapat pada file penerima_manfaat_bersih.csv setelah proses pembersihan data.

Metode: Multiple Linear Regression (Scikit-Learn)

Hasil: Y=65.651.130.571.389,8−32.445.608.200(X1​)\+350.614,94(X2​)−86.833,64(X3​)
Keterangan:
X1= Tahun
X2= Rencana KPM
X3= Realisasi KPM
Y = Rencana Anggaran
Hasil Perhitungan
Koefisien Regresi:
ahun = -32.445.608.200
Rencana KPM = 350.614,94
Realisasi KPM = -86.833,64
Intercept:
65.651.130.571.389,8
Evaluasi Model:
MAE = 10.927.263.743,40
RMSE = 16.111.604.336,36
R² = 0,2522

Kesimpulan: Metode Multiple Linear Regression dapat digunakan untuk memprediksi nilai Realisasi Anggaran berdasarkan variabel yang tersedia pada dataset. Tingkat akurasi model dapat dilihat dari nilai R² Score, sedangkan pengaruh masing-masing variabel terhadap target dapat dianalisis melalui koefisien regresi yang dihasilkan oleh model.

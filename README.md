# Laporan Proyek Machine Learning - Sulaiman Muharik

## Domain Proyek

Proses manufaktur semikonduktor modern yang kompleks biasanya berada di bawah pengawasan konsisten melalui pemantauan sinyal/variabel yang dikumpulkan dari sensor atau pos pengukuran proses. Namun, tidak semua sinyal berharga sama dalam sistem pemantauan tertentu. Sinyal yang diukur mengandung kombinasi informasi yang berguna, informasi yang tidak relevan, serta noise. Sering terjadi bahwa informasi yang berguna tertimbun dalam dua terakhir. Insinyur biasanya memiliki jumlah sinyal yang jauh lebih besar daripada yang sebenarnya dibutuhkan. Jika kita mempertimbangkan setiap jenis sinyal sebagai fitur, pemilihan fitur dapat diterapkan untuk mengidentifikasi sinyal yang paling relevan. Insinyur Proses kemudian dapat menggunakan sinyal-sinyal ini untuk menentukan faktor-faktor kunci yang berkontribusi untuk menghasilkan ekskursi hilir dalam proses. Ini akan memungkinkan peningkatan proses keseluruhan, menurunkan waktu untuk belajar, dan mengurangi biaya produksi per unit.


## Business Understanding

### Problem Statements

- Dari serangkaian fitur, fitur apa saja yang berpengaruh pada keberhasilan produksi?
- Dari serangkaian fitur, fitur apa yang paling berkorelasi pada keberhasilan produksi? 
- Bagaimana keberhasilan produksi dengan fitur tertentu?

### Goals

- Mengetahui fitur-fitur yang berpengaruh dengan keberhasilan produksi.
- Mengetahui fitur yang paling berkolerasi dengan keberhasilan produksi.
- Membuat model machine learning yang dapat memprediksi keberhasilan produksi seakurat mungkin dengan fitur-fitur yang ada.

### Solution statements
- Memilih fitur-fitur yang beerpengaruh untuk memudahkan mesin belajar.
- Menggunakan beberapa model algoritma untuk mencapai solusi yang diinginkan.


## Data Understanding

File dataset SECOM terdiri dari 1567 contoh masing-masing memiliki 591 fitur, label yang mewakili hasil lulus/gagal, dan cap waktu untuk setiap contoh. File dataset: [UCI SECOM Dataset](https://www.kaggle.com/paresh2047/uci-semcom).

### Variabel-variabel pada UCI SECOM dataset:
- Time mewakili cap waktu data spesifik, tipe data yang dimiliki adalah DateTime.
- 591 fitur mewakili sinyal/variabel yang dikumpulkan dari sensor atau pos pengukuran proses, tipe data yang dimiliki adalah float.
- Pass/Fail mewakili hasil lulus/gagal untuk pengujian, tipe data yang di miliki adalah integer antara -1 dan 1.

Kolom Time di-drop karena tidak dibutuhkan pada kasus ini. Fitur yang memiliki missing value lebih dari 20% di-drop agar model tidak keliru. Fitur yang memiliki variasi data 0 di-drop karena tidak memberikan informasi apapun. Mengisi missing value untuk memudahkan mesin belajar.


## Data Preparation

- Pairwise correlation.
- Correlation with target.
- Pembagian dataset dengan fungsi train_test_split dari library sklearn.
- Standarisasi.

Pairwise correlation dengan threshold 0.7 dilakukan untuk mengurangi fitur yang memiliki sifat yang mirip atau sama. Membuang fitur yang memiliki korelasi sangat kecil dengan target (Pass/Fail) dengan threshold 0.05. Membagi dataset menjadi train dan test. Melakukan standarisasi untuk memudahkan mesin belajar. 


## Modeling

Algoritma yang digunakan pada permasalahan ini adalah SVM, KNN, Random Forest, dan Boosting. Keempat algoritma tersebut merupakan algoritma yang dapat digunakan untuk melakukan klasifikasi biner. Akurasi yang didapatkan pada ketiga algoritma tersebut adalah 92.36%, 92.04%, 92.36%, dan 92.67% secara berurutan. Dari keempat algortima tersebut didapatkan model yang memiliki akurasi terbaik yang dipilih sebagai model terbaik dangan akurasi 92.67% yaitu algoritma Boosting.


## Evaluation

Pada kasus klasifikasi ini, metrik evaluasi yang digunakan adalah akurasi, precision, recall, dan F1-Score.
- Akurasi mengukur kebaikan model sebagai proporsi hasil yang benar terhadap total kasus.
- Precision adalah perbandingan antara hasil positif yang benar dengan banyaknya data yang diprediksi positif. Presisi = TP/(TP+FP).
- Recall adalah perbandingan antara hasil positif yang benar dengan banyaknya data yang sebenarnya positif. Recall = TP/(TP+FN).
- F1-Score adalah rata-rata harmonik dari precision dan recall, di mana nilai F1-Score yang ideal adalah 1 dan nilai terburuknya adalah 0. F1-Score yang baik mengindikasikan bahwa model memiliki precision dan recall yang baik. 

Algoritma Boosting merupakan algoritma yang terbaik pada proyek ini karena memiliki akurasi dan precision yang terbaik diantara 3 algoritma lainnya. Fitur yang paling berpengaruh pada algoritma ini adalah fitur 90.


**---Ini adalah bagian akhir laporan---**


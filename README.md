# Laporan Proyek Machine Learning - Sulaiman Muharik

## Domain Proyek

Proses manufaktur semikonduktor modern yang kompleks biasanya berada di bawah pengawasan konsisten melalui pemantauan sinyal/variabel yang dikumpulkan dari sensor atau titik pengukuran proses. Namun, tidak semua sinyal berharga sama dalam sistem pemantauan tertentu. Sinyal yang diukur mengandung kombinasi informasi yang berguna, informasi yang tidak relevan, serta noise. Sering terjadi bahwa informasi yang berguna tertimbun dalam dua terakhir. Insinyur biasanya memiliki jumlah sinyal yang jauh lebih besar daripada yang sebenarnya dibutuhkan. Jika kita mempertimbangkan setiap jenis sinyal sebagai fitur, pemilihan fitur dapat diterapkan untuk mengidentifikasi sinyal yang paling relevan. Insinyur Proses kemudian dapat menggunakan sinyal-sinyal ini untuk menentukan faktor-faktor kunci yang berkontribusi untuk menghasilkan ekskursi hilir dalam proses. Ini akan memungkinkan peningkatan proses keseluruhan, menurunkan waktu untuk belajar, dan mengurangi biaya produksi per unit.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Jelaskan mengapa dan bagaimana masalah tersebut harus diselesaikan
- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.
  
  Format Referensi: 
  [Using CRISP-DM to Predict Car Prices](https://medium.com/@christophberns/using-crisp-dm-to-predict-car-prices-f15eb5b14025) 
  [Komponen Model Evaluasi](https://docs.microsoft.com/id-id/azure/machine-learning/component-reference/evaluate-model#metrics-for-classification-models)

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
- Menggunakan beberapa model algoritma untuk mencapai solusi yang diinginkan.


**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding

Dataset yang disajikan pada kasus ini mewakili pilihan fitur-fitur, setiap contoh mewakili entitas produksi tunggal dengan fitur terukur terkait dan label mewakili hasil lulus/gagal untuk pengujian lini internal, figur 2, dan cap waktu tanggal terkait, -1 mewakili lulus dan 1 mewakili gagal dan cap waktu data adalah waktu spesifik tes tertentu. [UCI SECOM Dataset](https://www.kaggle.com/paresh2047/uci-semcom).

### Variabel-variabel pada UCI SECOM dataset:
Data memiliki 2 file, file dataset SECOM terdiri dari 1567 contoh masing-masing dengan 591 fitur, matriks 1567 x 591, dan file label yang berisi klasifikasi dan cap waktu untuk setiap contoh.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation

- Dropping unnecessary feature.
- Handling missing value.
- Handling 0 variation.
- Pairwise correlation.
- Correlation with target.
- Pembagian dataset dengan fungsi train_test_split dari library sklearn.
- Standarisasi.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling

Algoritma yang digunakan pada permasalahan ini adalah KNN, Random Forest, dan Boosting. Ketiga algoritma tersebut merupakan algoritma yang dapat digunakan untuk melakukan klasifikasi biner. Akurasi yang didapatkan pada ketiga algoritmaa tersebut adalah xx, xx, dan xx secara berurutan. Dari ketiga algortima tersebut didapatkan model yang memiliki akurasi terbaik yang dipilih sebagai model terbaik dangan akurasi xx.xx% yaitu algoritma Random Forest.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
(Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.)

Pada kasus klasifikasi ini, metrik evaluasi yang digunakan adalah akurasi, precision, recall, dan F1-Score.
- Akurasi mengukur kebaikan model sebagai proporsi hasil yang benar terhadap total kasus.
- Precision adalah perbandingan antara hasil positif yang benar dengan banyaknya data yang diprediksi positif. Presisi = TP/(TP+FP).
- Recall adalah perbandingan antara hasil positif yang benar dengan banyaknya data yang sebenarnya positif. Recall = TP/(TP+FN).
- F1-Score adalah rata-rata harmonik dari precision dan recall, di mana nilai skor F1 yang ideal adalah 1 dan nilai terburuknya adalah 0. F1_Score yang baik mengindikasikan bahwa model memiliki precision dan recall yang baik. 

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**


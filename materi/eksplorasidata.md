# Eksplorasi Data Iris

Dataset yang digunakan adalah Iris Flower Dataset yang berisi 150 data bunga dengan 4 fitur numerik (sepal_length, sepal_width, petal_length, petal_width) dan 1 fitur kategorikal (species). Dataset ini sering digunakan dalam analisis data dan machine learning untuk klasifikasi.

## 1 Struktur Data

-   Jumlah Baris: 150
-   Jumlah Kolom: 5
-   Dataset asli tidak memiliki missing value.
-   Tipe Data:
    -   4 kolom bertipe float (numerik)
    -   1 kolom bertipe object (kategori/species)

Untuk keperluan pembelajaran, dilakukan simulasi penambahan missing value pada beberapa kolom numerik untuk dianalisis dan ditangani.

## 2 Lima Data Pertama

|N0|sepal_length|sepal_width|petal_length|petal_width|species|
|:-----------|:-----------|:---------:|:----------:|:---------:|------:|
|1|5.1|3.5|1.4|0.2|Iris-setosa|
|2|4.9|3  |1.4|0.2|Iris-setosa|
|3|4.7|3.2|1.3|0.2|Iris-setosa|
|4|4.6|3.1|1.5|0.2|Iris-setosa|
|5|5  |3.6|1.4|0.2|Iris-setosa|

## 3. Statistik Deskriptif

Statistik deskriptif digunakan untuk mengetahui gambaran umum data seperti mean, minimum, maksimum, dan standar deviasi.

||sepal_length|sepal_width|petal_length|petal_width|
|:----|:------:|:------:|:-----:|-------:|
|count|   150  |  150   |  150  |  150   |
|mean |5.84333 |3.054   |3.75867|1.19867 |
|std  |0.828066|0.433594|1.76442|0.763161|
|min  |   4.3  |   2    |   1   |   0.1  |
|25%  |5.1|2.8|1.6|0.3|
|50%  |5.8|3|4.35|1.3|
|75%  |6.4|3.3|5.1|1.8|
|max  |7.9|4.4|6.9|2.5|

## 4. Analisis Awal

-   Rata-rata sepal_length: 5.84
-   Rata-rata sepal_width: 3.05
-   Rata-rata petal_length: 3.76
-   Rata-rata petal_width: 1.20

Dari hasil tersebut terlihat bahwa petal_length memiliki variasi nilai yang cukup besar dibandingkan fitur lainnya, sehingga fitur ini berpotensi baik untuk membedakan spesies bunga.

## 5. Deteksi Outlier

Deteksi outlier dilakukan menggunakan metode Local Outlier Factor.

Metode LOF mengukur kepadatan lokal suatu data dibandingkan dengan kepadatan tetangga terdekatnya. Data dengan kepadatan jauh lebih rendah dibandingkan sekitarnya akan dikategorikan sebagai outlier.

Parameter yang digunakan:

- n_neighbors = 20
- contamination = 0.10
- metric = euclidean

Hasil analisis menunjukkan terdapat sejumlah data yang terdeteksi sebagai outlier berdasarkan nilai kepadatan lokalnya. Outlier ini berpotensi mempengaruhi hasil analisis lanjutan seperti clustering atau perhitungan jarak.

## 6. Penambahan dan Penanganan Missing Value

Dataset Iris asli tidak memiliki missing value. Namun, untuk tujuan analisis dilakukan simulasi penambahan nilai kosong (NaN) pada beberapa kolom numerik.

Setelah dilakukan pengecekan, missing value ditangani menggunakan metode imputasi mean (rata-rata kolom). Metode ini dipilih karena:

- Data bersifat numerik
- Distribusi relatif stabil
- Tidak mengubah pola data secara signifikan

Tahap ini merupakan bagian dari proses data preparation dalam metodologi CRISP-DM.

## 7. Kesimpulan

1. Dataset Iris terdiri dari 150 data dengan 4 fitur numerik dan 1 fitur kategorikal.
2. Statistik deskriptif menunjukkan distribusi data yang cukup baik.
3. Deteksi menggunakan LOF menunjukkan adanya data yang terindikasi sebagai outlier.
4. Simulasi missing value dan proses imputasi dilakukan sebagai bagian dari data preparation.
5. Petal length dan petal width memiliki variasi paling besar dan berpotensi menjadi fitur penting dalam proses klasifikasi.
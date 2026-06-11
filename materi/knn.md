# K-Nearest Neighbors (K-NN)

K-Nearest Neighbors (K-NN) merupakan salah satu algoritma klasifikasi yang sangat populer dalam bidang **machine learning**, khususnya dalam kategori **supervised learning**. Algoritma ini pertama kali diperkenalkan oleh **Evelyn Fix** dan **Joseph Hodges** pada tahun 1951. K-NN bekerja dengan cara mengklasifikasikan suatu data baru berdasarkan kedekatan atau kemiripan dengan data lain yang sudah diketahui kelasnya dalam dataset.

Prinsip utama dari algoritma ini adalah bahwa **data yang memiliki karakteristik mirip akan cenderung berada pada kelas yang sama**. Oleh karena itu, proses klasifikasi dilakukan dengan melihat sejumlah tetangga terdekat dari suatu data baru.

Algoritma K-NN termasuk metode **lazy learning**, yaitu algoritma yang tidak membangun model secara eksplisit selama proses pelatihan. Sebaliknya, seluruh data pelatihan disimpan dan digunakan langsung ketika proses klasifikasi dilakukan.

# Prinsip Dasar K-NN

Prinsip dasar dari K-NN adalah memanfaatkan **perhitungan jarak antar data** untuk menentukan kelompok atau kelas suatu data baru.

Ketika terdapat data baru yang belum diketahui kelasnya, algoritma K-NN akan:

1. Menghitung jarak antara data baru dengan seluruh data pada dataset pelatihan.
2. Menentukan sejumlah tetangga terdekat berdasarkan nilai parameter **k**.
3.  Mengambil **mayoritas kelas** dari tetangga terdekat tersebut.
4.  Menetapkan kelas tersebut sebagai hasil klasifikasi data baru.

Sebagai contoh, jika nilai **k = 3**, maka algoritma akan melihat **3 data terdekat** dari data baru dan menentukan kelas berdasarkan mayoritas dari ketiga data tersebut.

# Euclidean Distance

Euclidean Distance merupakan metode pengukuran jarak yang paling umum digunakan dalam algoritma K-NN. Metode ini menghitung jarak lurus antara dua titik dalam ruang multidimensi.

Rumus:

$$
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
$$

Semakin kecil nilai jarak Euclidean antara dua data, maka semakin mirip kedua data tersebut.

# Jarak Manhattan

Jarak Manhattan adalah metode pengukuran jarak yang menghitung jarak antar titik dalam bentuk **pergerakan horizontal dan vertikal**, seperti jalur jalan pada kota berbentuk grid.

Rumus:

$$
d(A,B) = \sum_{i=1}^{n} |x_i - y_i|
$$

# Jarak Minkowski

Jarak Minkowski merupakan generalisasi dari jarak Euclidean dan Manhattan.

Jika:

- p = 1 → Manhattan Distance
- p = 2 → Euclidean Distance

Rumus:

$$
d(A,B) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{1/p}
$$

# Jarak Chebyshev

Jarak Chebyshev digunakan untuk mengukur jarak maksimum antara dua titik pada salah satu dimensi koordinat.

Rumus:

$$
d(A,B) = \max(|x_i - y_i|)
$$

# Jarak Cosine

Cosine Distance digunakan untuk mengukur **kemiripan antara dua vektor** terutama pada data berdimensi tinggi seperti dokumen teks.

Rumus:

$$
d(A,B) =
1 -
\frac{\sum_{i=1}^{n} x_i y_i}
{\sqrt{\sum_{i=1}^{n} x_i^2}
\cdot
\sqrt{\sum_{i=1}^{n} y_i^2}}
$$

# Jarak Mahalanobis

Mahalanobis Distance mempertimbangkan **distribusi data dan korelasi antar variabel**.

Rumus:

$$
d(A,B) =
\sqrt{(X - Y)^T S^{-1} (X - Y)}
$$

Dimana:

-   $X$ = vektor data pertama
-   $Y$ = vektor data kedua
-   $S⁻¹$ = invers matriks kovarians

# Prosedur Algoritma K-NN

Langkah-langkah algoritma:

1.  Tentukan nilai **k**.
2.  Hitung jarak data baru dengan seluruh data dataset.
3.  Urutkan jarak dari yang terkecil.
4.  Ambil **k tetangga terdekat**.
5.  Tentukan kelas berdasarkan **mayoritas kelas**.

# Kelebihan K-NN

1.  Mudah dipahami dan diimplementasikan.
2.  Tidak memerlukan proses training yang kompleks.
3.  Dapat digunakan untuk klasifikasi dan regresi.
4.  Efektif untuk dataset kecil hingga menengah.

# Kekurangan K-NN

1.  Lambat jika dataset sangat besar.
2.  Sensitif terhadap outlier.
3.  Pemilihan nilai **k** sangat mempengaruhi hasil.
4.  Sensitif terhadap skala data sehingga perlu normalisasi.

# Contoh Penerapan

Algoritma K-NN digunakan dalam:

-   Pengenalan wajah
-   Sistem rekomendasi
-   Klasifikasi penyakit
-   Pengenalan tulisan tangan
-   Data mining

# Kesimpulan

K-Nearest Neighbors (K-NN) merupakan algoritma klasifikasi sederhana namun efektif. Dengan memanfaatkan konsep **kedekatan jarak antar data**, algoritma ini mampu menentukan kelas suatu data baru.

Meskipun memiliki keterbatasan pada dataset besar, K-NN tetap menjadi algoritma yang populer karena kemudahan implementasi dan akurasi yang cukup baik pada berbagai kasus klasifikasi.

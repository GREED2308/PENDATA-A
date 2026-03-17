# Missing Values

Missing values merupakan kondisi ketika suatu atribut pada dataset tidak memiliki nilai atau bernilai kosong. Permasalahan ini sering terjadi dalam proses pengumpulan data, baik karena kesalahan input data, kegagalan sistem, data yang tidak tersedia pada saat pengumpulan, maupun karena adanya kesalahan dalam proses penyimpanan data.

Dalam proses analisis data maupun data mining, keberadaan missing values dapat menjadi masalah yang cukup serius. Data yang tidak lengkap dapat mempengaruhi kualitas hasil analisis dan menyebabkan model yang dihasilkan menjadi kurang akurat. Oleh karena itu, sebelum data digunakan dalam proses analisis lebih lanjut, perlu dilakukan penanganan terhadap nilai yang hilang tersebut.

Terdapat beberapa metode yang dapat digunakan untuk menangani missing values. Beberapa metode yang umum digunakan antara lain menghapus data yang memiliki nilai kosong, mengganti nilai yang hilang dengan nilai rata-rata (mean), median, atau modus, serta menggunakan metode estimasi berbasis algoritma machine learning.

Salah satu metode yang cukup efektif untuk menangani missing values adalah metode **Weighted K-Nearest Neighbor Imputation (WKNNI)**. Metode ini memanfaatkan konsep kedekatan antar data untuk memperkirakan nilai yang hilang berdasarkan data yang memiliki karakteristik paling mirip.

## Metode Weighted K-Nearest Neighbor (WKNN)

Weighted K-Nearest Neighbor (WKNN) merupakan pengembangan dari metode K-Nearest Neighbor (KNN) yang digunakan untuk melakukan imputasi terhadap nilai yang hilang pada dataset. Metode ini bekerja dengan cara mencari sejumlah data tetangga terdekat dari suatu data yang memiliki nilai kosong.

Pada metode KNN biasa, setiap tetangga memiliki pengaruh yang sama dalam menentukan nilai estimasi. Namun pada metode WKNN, setiap tetangga diberikan bobot berdasarkan tingkat kedekatannya terhadap data target. Data yang memiliki jarak lebih dekat akan memiliki bobot yang lebih besar dibandingkan data yang memiliki jarak lebih jauh.

Dengan menggunakan pendekatan ini, nilai estimasi yang dihasilkan akan lebih akurat karena mempertimbangkan tingkat kemiripan antar data.

## Perhitungan Jarak Menggunakan Euclidean Distance

Dalam metode WKNN, tingkat kedekatan antar data biasanya dihitung menggunakan jarak Euclidean. Jarak ini digunakan untuk mengukur seberapa mirip suatu data dengan data lainnya berdasarkan atribut yang dimiliki.

Rumus Euclidean Distance adalah sebagai berikut:

$$d(x,y) = √((x1 - y1)² + (x2 - y2)² + ... + (xn - yn)²)$$

Semakin kecil nilai jarak yang dihasilkan, maka semakin tinggi tingkat kemiripan antara kedua data tersebut.

## Estimasi Nilai Menggunakan Weighted Average

Setelah jarak antar data dihitung, langkah selanjutnya adalah menentukan beberapa tetangga terdekat berdasarkan nilai jarak terkecil. Kemudian nilai dari tetangga tersebut digunakan untuk memperkirakan nilai yang hilang dengan menggunakan metode rata-rata berbobot (Weighted Average).

Rumus yang digunakan adalah sebagai berikut:

$$
X = \frac{\sum (w_i \times y_i)}{\sum w_i}
$$

Keterangan:

- wi = bobot dari tetangga ke-i
- yi = nilai atribut pada tetangga ke-i

Melalui metode ini, tetangga yang memiliki jarak lebih dekat akan memberikan kontribusi yang lebih besar terhadap nilai estimasi dibandingkan tetangga yang memiliki jarak lebih jauh.

Dengan demikian, metode WKNN dapat digunakan sebagai salah satu teknik yang efektif dalam menangani missing values pada dataset sebelum dilakukan proses analisis data lebih lanjut.
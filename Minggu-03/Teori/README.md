# Materi teori minggu ke 3

## Hirarki Analytics
bisa di lihat pada gambar di bawah ini

<img src="https://github.com/lourenson10107/img/blob/master/Hirarki.png">

## Membangun Data Foundations & Warehouse
terlepas dari tujuan/ tingkat minat dalam mempelajari teknik data /data engineering, sangat penting untuk mengetahui dengan pasti apa itu
rekayasa data. penulis asli airflow mengkarakteristik rekayasa data dalam postnya yang fantastis "the rise of data engineer".

Diantar banyak hal berharga yang dilakukan para insinyur data, salah satu keahlian mereka yang sangat dicari adalah kemampuan untuk merancang , membangun, dan memelihara data warehouse.

**contoh gambar data yang di ubah dari data mentah menjadi data yang baik**

<img src="img/blob/master/Proses-Etl.png">

contoh spesifik yang menyoroti peran data warehouse untuk berbagai perusahaan dalam berbagai tahap :
### 1. Membangun Analytics di 500px :
tantangan yang dihadapi 500px ketika mencoba untuk tumbuh melampaui kecocokan pasar produk. Dia menjelaskan secara rinci proses bagaimana ia membangun gudang data dari tanah dan ke atas.
### 2. Mengukur Platform Eksperimentasi Airbnb :
menunjukkan bagaimana tim teknik data Airbnb membangun pipa data khusus untuk mendukung alat internal seperti kerangka pelaporan eksperimen. Pekerjaan ini sangat penting dalam membentuk dan mengukur budaya pengembangan produk Airbnb.
### 3. Menggunakan ML untuk Memprediksi Nilai Rumah di Airbnb :
model pembelajaran mesin pemberian skor offline membutuhkan banyak pekerjaan rekayasa data di muka. Khususnya, banyak tugas yang terkait dengan rekayasa fitur, bangunan, dan data pelatihan backfilling menyerupai karya rekayasa data.

## ETL: Extract, Transform, dan Load
kepanjangan dari *etl* adalah EKSTRACT, TRANSFORM, LOAD
1. **EXTRACT :** adalah langkah di mana sensor menunggu sumber data hulu ke darat (misalnya sumber hulu bisa berupa mesin atau log yang dibuat pengguna, salinan basis data relasional, dataset eksternal ... dll). Setelah tersedia, kami mengangkut data dari lokasi sumber mereka ke transformasi lebih lanjut.
2. **TRANSFORM :** adalah jantung dari pekerjaan ETL mana pun, di mana kami menerapkan logika bisnis dan melakukan tindakan seperti penyaringan, pengelompokan, dan agregasi untuk menerjemahkan data mentah ke dalam dataset analisis siap. Langkah ini membutuhkan banyak pemahaman bisnis dan pengetahuan domain.
3. **LOAD :** memuat data yang diproses dan mengangkutnya ke tujuan akhir.

**berikut contoh gambar proses ETL**

<img src="images/git-tut3.png">

## Dua Paradigma: SQL- vs JVM-Centric ETL
terdapat 2 paradigma yang digunakan untuk membangun *etl* :
1. **ETL JVM-sentris** biasanya dibangun dalam bahasa berbasis JVM (seperti Java atau Scala). Saluran pipa data teknik dalam bahasa JVM ini sering melibatkan transformasi data pemikiran dengan cara yang lebih penting, misalnya dalam hal pasangan nilai kunci. Menulis Fungsi yang Ditetapkan Pengguna (UDFs) kurang menyakitkan karena seseorang tidak perlu menulisnya dalam bahasa yang berbeda, dan pekerjaan pengujian dapat lebih mudah untuk alasan yang sama. Paradigma ini cukup populer di kalangan insinyur.
2. **ETL SQL-sentris** biasanya dibangun dalam bahasa seperti SQL, Presto, atau Hive. Pekerjaan ETL sering didefinisikan dengan cara deklaratif , dan hampir semuanya berpusat di sekitar SQL dan tabel. Menulis UDFs terkadang merepotkan karena seseorang harus menuliskannya dalam bahasa yang berbeda (misalnya Java atau Python), dan pengujian dapat menjadi lebih menantang karena ini. Paradigma ini populer di kalangan ilmuwan data.































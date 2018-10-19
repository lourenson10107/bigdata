# Materi Pertemuan ke 5 (Teori)

## Panduan Data Engineer 

### Ikhtisar
*Di bagian ketiga ini (terakhir) akan dibahas tentang konsep dari framework data engineering dan membedah pola desain untuk membangung framework tersebut, kemudian akan fokus ke beberapa contoh spesifik yang sering digunakan oleh AriBnb, yang bertujuan agar pembaca dapat mengembangkan sendiri untuk abstraksi framework.*

###  Dari Pipelines Ke Kerangka Kerja
Seperti yang telah kita pelajari dari Bagian II , DAG Aliran Udara dapat menjadi rumit secara acak. Terkadang, perhitungan data bahkan mengikuti aliran kontrol seperti logika. Misalnya, jika Anda tertarik untuk mencabang aliran data setelah pemeriksaan bersyarat spesifik, Anda dapat menerapkan BranchPythonOperator . Jika Anda ingin alur kerja berlanjut hanya jika suatu kondisi terpenuhi, Anda dapat menggunakan ShortCircuitOpeartor . Operator-operator ini, dikombinasikan dengan prinsip konfigurasi sebagai kode adalah apa yang membuat ETL Airflow fleksibel dan fleksibel. Namun, Aliran Udara dapat melakukan lebih banyak lagi.

Diskusi kami sejauh ini terbatas pada desain pipa tunggal yang berdiri sendiri, tetapi kami dapat menerapkan prinsip yang sama untuk pembuatan saluran pipa -  cara untuk menghasilkan DAG secara dinamis dan dinamis dengan cepat. Ini pada dasarnya adalah apa yang dilakukan oleh kerangka kerja rekayasa data : ia menghasilkan berbagai instantiasi dari DAG Aliran Udara yang mengotomatisasi alur kerja data. Berikut adalah bagaimana Maxime, penulis asli Airflow menggambarkannya :

    Untuk membangun alur kerja secara dinamis dari kode ... Contoh yang sangat sederhana adalah skrip Aliran Air yang membaca file konfigurasi YAML dengan daftar nama tabel, dan membuat sedikit alur kerja untuk setiap tabel, yang dapat melakukan hal-hal seperti memuat tabel ke dalam target database, mungkin menerapkan aturan dari file konfigurasi di sekitar pengambilan sampel, retensi data, penganoniman ... Sekarang Anda memiliki abstraksi ini ... Anda dapat membuat potongan alur kerja baru tanpa melakukan banyak pekerjaan. Ternyata ada banyak sekali kasus penggunaan untuk jenis pendekatan ini.

**Alat-alat untuk meningkatkan rantai nilai**

1. Bayangkan bahwa ketika kerangka pelaporan eksperimen secara otomatis menghasilkan 
metrik tingkat pengguna dan menghitung statistik untuk eksperimen, para ilmuwan data 
sekarang dapat mencurahkan lebih banyak waktu untuk menganalisis perubahan dalam metrik
utama, menafsirkan perilaku pengguna, dan menyoroti dampak dari perubahan produk.

2. Demikian pula, ketika kerangka metrik secara otomatis menghasilkan tabel OLAP 
dengan cepat, para ilmuwan data dapat menghabiskan lebih banyak waktu untuk memahami
tren, mengidentifikasi kesenjangan, dan menyampaikan perubahan produk ke perubahan 
bisnis.

3. Contoh lain adalah kerangka kerja yang mengabstrakkan pekerjaan teknik yang 
diperlukan untuk memproduksi model ML batch offline. Para ilmuwan data tidak perlu 
lagi khawatir tentang dependensi paket, pengaturan lingkungan virtual, atau 
penyebaran. Mereka dapat menghabiskan waktu untuk pemodelan.

### Pola Desain Untuk Kerangka Rekayasa Data
Secara umum ada tiga lapis kerangka kerja rekayasa data yang dirancang dengan baik: 
1. lapisan input
2. lapisan pemrosesan data
3. lapisan keluaran

**seperti Gambar dibawah ini**


1. **Input:** Ini adalah tempat pengguna akhir menentukan bagaimana DAG mereka harus dikonfigurasi. Pengalaman pengguna sangat penting di sini. Biasanya, input bisa berupa file konfigurasi statis (misalnya YAML atau HOCON), atau bisa juga sesuatu yang rumit seperti UI web. Tujuannya di sini adalah untuk menangkap kebutuhan pengguna.

2. **Pemrosesan Data:**  Ini adalah inti dari kerangka kerja rekayasa data, di mana saluran pipa ETL dipakai secara dinamis. Kode yang mencapai ini biasanya disebut sebagai pabrik DAG , yang secara aneh menangkap gagasan bahwa DAG dibuat satu per satu, seperti di pabrik.

3. **Output:** DAG yang dihasilkan dari langkah sebelumnya membuat data turunan, dan hasilnya sering disimpan dalam tabel Hive hilir, disajikan dalam lapisan UI / visualisasi yang dirancang dengan baik, atau hanya dikonsumsi oleh pipa hilir atau kerangka kerja

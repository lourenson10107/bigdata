# Materi  Teori pertemuan ke 4

## Pemodelan Data
pemodelan data merupakan proses desain dimana orang dengan hati hati mendefenisikan
skema tabel dan relasi data untuk menanggkap metrik dan dimensi bisnis.
  pendekatan analitik pertama ini sering melibatkan proses desain yang di sebut pemodelan
  data.

## Pemodelan data, normalisasi, skema bintang
secara umum tabel yang sudah di normalkan memiliki skema yang lebih sederhana, data yang
lebih terstandardisasi, dan lebih sedikit data yang redudansi.

salah satu pola desain yang menyeimbangkan trade-off dan paling sering di gunakan di Airbnb
yaitu **Skema Bintang**. di namakan skema bintang karena tabel yang disusun berbentuk sperti bintang
pola ini berfokus pada pembuatan tabelyang di normalisasi, khususnya tabel fakta dan
dimensi.

**contoh gambar Skema Star**
.........



## tabel fakta dan Dimensi

1. **Tabel Fakta** biasanya berisi data tranksaksional titik ke waktu yang artinya setiap baris
dalam tabel bisa sangat sederhana dan sering di presentasikan sebagai unit transaksi.
karena kesederhanaan, maka sering menjadi sumber tabel keenaran dari metrik yang berasal.

2. **Tabel Dimensi** bisanya berisi atribut yang berubah perlahan-lahan dari entitas 
tertentu, dan atribut terkadang dapat di atur dalm struktur  hierarkis. atribut dimensi 
dapat digambungkan dengan tabel fakta, selama kunci asing berada pada tabel fakta.

## mempartisi data dan mengisi ulang historis
### partisi data

teknik yang paling efektif untuk meningkatkan kinerja kueri adalah dengan mempartisi data.
partisi data yang sederhana untuk dimengerti yaitu semua data dalam satu potongan, kita
membaginya menjadi potongang lainya/ potongan mandiri.
data dari potongan yang sama akan di berikan kunci partisi yang sama, yang berarti bahwa
setiap bagian dari data dapat dicari dengan sangat cepat.

### pengukuran data historis
keuntungan lain dari menggunakan datestamp sebagai kunci partisi adalah kemudahan pengukuran data.
ketika pipa ETL di bangun, itu menghitung metrik dan dimensi ke depan bukan ke belakang.






















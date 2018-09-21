# 5. Struktur Data

# 5.1. Tipe data daftar

**berikut ini merupakan method yang di gunakan di tipe data daftar/List seperti :**
1. append
2. extend
3. insert
4. remove
5. pop
6. clear
7. index
8. count
9. sort
10. reverse, DLL


## 1. Menggunakan Daftar sebagai Tumpukan
    >>> stack = [3, 4, 5]
    >>> stack.append(6)
    >>> stack.append(7)
    >>> stack
    [3, 4, 5, 6, 7]
perintah di atas merupakan perintah yang menggunakan method append() yang berfungsi untuk menumpuk data yang pertama dengan data yang ditambahkan, jika kita menambahkan method POP maka hasilnya seperti ini.

    >>> stack.pop()
    7

Pop() berfungsi untuk mengambil data atau item dari data terakhir kali di tambahkan

## 2. Menggunakan Daftar sebagai Antrian
menggunakan daftar sebagai antrian, dimana elemen pertama yang ditambahkan adalah
elemen pertama yang diambil ("masuk pertama, pertama keluar")

    >>> from collections import deque
    >>> queue = deque(["ongen", "eric", "Michael"])
    >>> queue.append("Terry")
    >>> queue.append("emanuel")
    >>> queue.popleft()
    'ongen'
    >>> queue.popleft()
    'eric'
    >>> queue
    deque(['Michael', 'Terry', 'emanuel'])
    >>>
    
jadi maksud dari perintah di atas adalah data yang masuk pertama adalah "ongen" dan seharusnya 
data yang di ambil adalah "ongen", sementara data yang baru ditambahkan *Terry*, *emanuel* akan 
ditambahkan ke daftar antrian selanjutnya. yaitu  *'Michael', 'Terry', 'emanuel'*.

## 3. Daftar Pemahaman

cara yang ringkas untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan lain atau dapat dilakukan, atau untuk menciptakan kelanjutan dari elemen-elemen yang memenuhi suatu kondisi tertentu.

contoh, asumsikan kita ingin membuat daftar nilai, seperti:

    >>> hitung = []
    >>> for x in range(10):
    ...             hitung.append(x**2)
    ...
    >>> hitung
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


untuk mendapatkan data atau nilai yang sama seperti di atas, bisa menggunakan cara seperi di bawah
ini untuk mempermudah di mengerti atau ringkas :

    >>> hitung = list(map(lambda x: x**2, range(10)))
    >>> hitung
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    
atau dengan cara lain :
     
    >>> hitung = [x**2 for x in range(10)]
    >>> hitung
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


contoh lainnya :

menggambungkan data atau elemen dari dua daftar yang tidak sama
     
    >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    
hasilnya :

    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    

 dan sama dengan hasilnya jika menggunakan perintah seperti ini 
 
    >>> gabung = []
    >>> for x in [1,2,3]:
    ...     for y in [3,1,4]:
    ...             if x !=y:
    ...                     gabung.append((x, y))
    ...
hasilnya :

    >>> gabung
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


    
## 4. Pengertian Daftar Bersarang

contoh :
    di bawah ini merupakan contoh dari matriks 3x4 yang artinya datanya terdapat 3 daftar
    dan panjang data dari satu daftar adalah 4.

    >> matrix = [
    ...     [1, 2, 3, 4],
    ...     [5, 6, 7, 8],
    ...     [9, 10, 11, 12],
    ... ]

kemudian hasil nya seperti di bawah ini jika mentransformasikan baris dan kolom 
datanya, 
hasilnya bisa dilihat di bawah ini :
    
    >>> [[row[i] for row in matrix] for i in range(4)]
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
  
hasil akan sama saja seperti dibawah ini.

    >>> transposed = []
    >>> for i in range(4):
    ...     transposed.append([row[i] for row in matrix])
    ...
    >>> transposed
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# 5.2. Satement del

pernyataan ini merupakan fungsi untuk menghapus item atau data dari daftar yang di berikan indeksnya,
bukan nilainya. *del* juga digunakan untuk menghapus irisan dari daftar atau
menghapus seluruh daftar.

**contoh :**

    >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
    >>> del a[0]
    >>> a
    [1, 66.25, 333, 333, 1234.5]
    >>> del a[2:4]
    >>> a
    [1, 66.25, 1234.5]
    >>> del a[:]
    >>> a
    []

fungsi *del* juga dapat digunakan untuk menghapus seluruh variabel dengan perintah 
dibawah ini :

    >>> del a
    
yang mana "a" adalah nama variabelnya.

# 5.3. Tuples dan Sequences

Karena Python adalah bahasa yang sedang berkembang, tipe data sequence lainnya dapat 
ditambahkan. Ada juga tipe data sequence standar lainnya seperti  : tuple.

Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:

    >>> t = 12345, 54321, 'hello!'
    >>> t[0]
    12345
    >>> t
    (12345, 54321, 'hello!')
    >>> # Tuples may be nested:
    ... u = t, (1, 2, 3, 4, 5)
    >>> u
    ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
    

pada tupel keluaran selalu diapit dalam tanda kurung, sehingga tuple yang disarangkan 
ditafsirkan dengan benar, contoh penulisan yang salah :

    >>> # Tuples are immutable:
    ... t[0] = 88888
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

Tidak mungkin untuk menetapkan ke masing-masing item tuple, namun dimungkinkan untuk 
membuat tuple yang berisi objek yang bisa berubah, seperti daftar.

Meskipun tuples mungkin tampak mirip dengan daftar, tuples sering digunakan dalam 
situasi yang berbeda dan untuk tujuan yang berbeda. Tuples tidak dapat diubah

# 5.4. Set
Python juga termasuk tipe data untuk set . Satu set adalah koleksi tak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Mengatur objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

**contoh untuk melihat data yang sama tak telihat dua kali ketika di tampilkan, dan juga mengecek apakah data
tersebut memang ada atau tidak**

    >>> warna = {'merah', 'orange', 'biru', 'hijau', 'hitam', 'merah'}
    >>> print(warna)
    {'biru', 'hitam', 'orange', 'merah', 'hijau'}
    >>> 'merah' in warna
    True
    >>> 'kuning' in warna
    False
    
**contoh operasi pada huruf-huruf yang unik pada dua kata**

    >>> a = set('abracadabra')
    >>> b = set('alacazam')
    >>> a                                  # huruf unik pada a
    {'a', 'r', 'b', 'c', 'd'}
    >>> a - b                              # huruf yang tidak ada pada b
    {'r', 'd', 'b'}
    >>> a | b                              # gabungan huruf antara a dan b
    {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    >>> a & b                              # huruf yang ada atau sama pada a dan b
    {'a', 'c'}
    >>> a ^ b                              # huruf dalam a dan b yang tidak ada/ sama di keduanya
    {'r', 'd', 'b', 'm', 'z', 'l'}


# 5.5. Dictionaries
Tipe data lain yang berguna dibangun ke dalam Python adalah dictionary, dictionary kadang-kadang ditemukan dalam bahasa lain sebagai “associative memories” or “associative arrays”. Tidak seperti sequences, yang diindeks oleh berbagai angka, dictionary diindeks oleh kunci , yang bisa menjadi jenis yang tidak berubah,string dan angka selalu bisa menjadi kunci.\

contoh kecil menggunakan dictionary :

    >>> tel = {'jack': 4098, 'sape': 4139}
    >>> tel['guido'] = 4127
    >>> tel
    {'jack': 4098, 'sape': 4139, 'guido': 4127}
    >>> tel['jack']
    4098
    >>> del tel['sape']
    >>> tel['irv'] = 4127
    >>> tel
    {'jack': 4098, 'guido': 4127, 'irv': 4127}
    >>> list(tel)
    ['jack', 'guido', 'irv']
    >>> sorted(tel)
    ['guido', 'irv', 'jack']
    >>> 'guido' in tel
    True
    >>> 'jack' not in tel
    False
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    tel

    tel['jack']

    del tel['sape']
    tel['irv'] = 4127
    tel

    list(tel)

    sorted(tel)

    'guido' in tel

    'jack' not in tel


# 5.6. Teknik Looping

Ketika mengulang melalui dictionaries, kunci dan nilai yang terkait dapat diambil pada saat
yang sama menggunakan items()method

    >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    >>> for k, v in knights.items():
    ...     print(k, v)
    ...
    gallahad the pure
    robin the brave
 
menggunakan method enumerate() untuk memberikan urutan pada indeksnya.

    >>> for i, v in enumerate(['tic', 'tac', 'toe']):
    ...     print(i, v)
    ...
    0 tic
    1 tac
    2 toe

mengulang lebih dari dua sequences pada saat yang sama, menggunakan method zip().

    >>> pertanyaan = ['nama', 'hobi', 'warna favorit']
    >>> jawab = ['Lourenson', 'ngegame', 'merah']
    >>> for p, j in zip(pertanyaan, jawab):
    ...     print('{0} Kamu ? saya adalah {1}.'.format(p, j))
    ...
    nama Kamu ? saya adalah Lourenson.
    hobi Kamu ? saya adalah ngegame.
    warna favorit Kamu ? saya adalah merah.



mengulang urutan secara terbalik, dengan urutannya selisih dua.

    >>> for i in reversed(range(1, 10, 2)):
    ...     print(i)
    ...
    9
    7
    5
    3
    1


# 5.7. Lebih lanjut tentang Kondisi
Kondisi yang digunakan dalam whiledan ifpernyataan dapat mengandung operator,
Operator perbandingan indan memeriksa apakah suatu nilai terjadi (tidak terjadi) secara berurutan. Operator dan membandingkan apakah dua objek benar-benar objek yang sama; ini hanya penting untuk objek yang bisa berubah seperti daftar. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.not inisis not

**contoh menetapkan hasil perbandingan atau ekspresi boolean ke suatu variabel**

    >>> string1, string2, string3 = '', 'ongen', 'saptenno'
    >>> non_null = string1 or string2 or string3
    >>> non_null
    'ongen'

Perhatikan bahwa dengan Python, tidak seperti C, tugas tidak dapat terjadi di dalam ekspresi. Pemrogram C mungkin mengeluh tentang hal ini, tetapi menghindari kelas umum masalah yang dihadapi dalam program C: mengetikkan =ekspresi ketika ==dimaksudkan.


# 5.8. Membandingkan Sequences dan Jenis Lain
Objek Sequences dapat dibandingkan dengan objek lain dengan jenis Sequences yang sama. Perbandingan ini menggunakan Sequences leksikografis : pertama dua item pertama dibandingkan, dan jika mereka berbeda, ini menentukan hasil perbandingan; jika keduanya sama, dua item berikutnya akan dibandingkan, dan seterusnya, hingga urutannya habis. Jika dua item untuk dibandingkan adalah urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu Sequences adalah sub-Sequences awal yang lain, Sequences yang lebih pendek adalah yang lebih kecil (lebih kecil). Pemesanan Lexicographical untuk string menggunakan nomor poin kode Unicode untuk memesan karakter individu. Beberapa contoh perbandingan antara urutan jenis yang sama:

    (1, 2, 3)              < (1, 2, 4)
    [1, 2, 3]              < [1, 2, 4]
    'ABC' < 'C' < 'Pascal' < 'Python'
    (1, 2, 3, 4)           < (1, 2, 4)
    (1, 2)                 < (1, 2, -1)
    (1, 2, 3)             == (1.0, 2.0, 3.0)
    (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

Perhatikan bahwa membandingkan objek dari berbagai jenis dengan <atau >legal asalkan objek memiliki metode perbandingan yang tepat.

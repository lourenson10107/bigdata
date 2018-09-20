# 5. Struktur Data

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
menggunakan daftar sebagai antrian, dimana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, pertama keluar")

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


    
    
    
    
    

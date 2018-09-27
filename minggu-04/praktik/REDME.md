### 6. Modules
Modul adalah file yang berisi defenisi dan pernyataan Python, nama file adalah nama modul
dengan akhiran *.py* dana nama modul sebagai striang

**contoh**
filenya di berikan nama *fibo.py* kemudian di save pada folder python di drive (D:)

    # Fibonacci numbers module
    def fib(n):    # write Fibonacci series up to n
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

sebelum menjalankan perintah impor kita harus melakuakan perintah berikut ini :

    >>> import sys
    >>> sys.path.append(r'D:\python')
perintah di atas berguna agar python bisa mengetahui file yang aka di impor terletak di lokasi penyimpanan apa.
jika sudah kita akan menginpor modul ini maka kita harus menggunakan perintah :

    >>> import fibo
    
 yang artinya import merupakan fungsinya kemudian fibo merupakan nama dari modul 
 yang di buat dan ingin kita import.
 dan hasil yang di dapatkan seperti ini :
 
     >>> fibo.fib(1000) =>> merupakan perintahnya
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 ==>> hasilnya.
 
 
#### 6.1 lebih lanjut tentang modules

modul dapat berisi pernyataan yang dapat di eksekusi serta defenisi fungsi.

**varian yang mengimpor nama modul langsung ke tabel simbol pengimpor**
    
    >>> from fibo import fib, fib2
    >>> fib(500)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
    
**varian utuk menginpor semua nama yang di definisikan oleh modul **

    >>> from fibo import *
    >>> fib(500)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


##### 6.1.1 melaksanakan modules sebagai skrip
dapat di gunakan sebagai sript dan juga modul yang dapat di impor, karena kode yang mem-parsing baris perinah
hanya berjalan jika modul dijalankan sebagai file utama.

##### 6.1.2 Jalur pecarian modules
ketika sebuah modul bernama *spam* diimpor, interpreter pertama mencari modul built-in 
dengan nama itu.

##### 6.1.3. "Dikompilasi" file Python
Untuk mempercepat pemuatan modul, Python menyimpan versi terkompilasi dari setiap
modul di *__pycache__*
dua keadaan python tidak memeriksa cache :

1. selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang di muat
langsung dari baris perintah
2. python tidak akan memeriksa cache apabila modules sumber tidak ada.

#### 6.2. Modul Standar
Beberapa modul dibangun ke interpreter; ini memberikan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke primitif sistem operasi seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya.

    >>> import sys
    >>> sys.ps1
    '>>> '
    >>> sys.ps2
    '... '
    >>> sys.ps1 = 'C> '
    C> print ('ongen')
    ongen
    C>
Variabel sys.ps1dan sys.ps2menentukan string yang digunakan sebagai petunjuk utama 
dan sekunder ,Kedua variabel ini hanya ditentukan jika interpreter berada dalam mode 
interaktif.


#### 6.3. Fungsi dir()

Fungsi built-in dir()digunakan untuk mencari tahu nama-nama yang didefinisikan modul.
**contoh**

    >>> import fibo, sys
    >>> dir(fibo)
    ['__name__', 'fib', 'fib2']
    >>> dir(sys)  

#### 6.4. Paket
Paket adalah cara menyusun ruang nama modul Python dengan menggunakan "nama modul 
bertitik".

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:
    
    import sound.effects.echo
















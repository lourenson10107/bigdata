### 6. Modules
Modul adalah file yang berisi defenisi dan pernyataan Python, nama file adalah nama modul
dengan akhiran *.py* dana nama modul sebagai striang

**contoh**
filenya di berikan nama *fibo.py*

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

jika kita akan menginpor modul ini maka kita harus menggunakan perintah :

    >>> import fibo
 yang artinya import merupakan fungsinya kemudian fibo merupakan nama dari modul 
 yang di buat dan ingin kita import.
 
 
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


##### 6.1.1 melaksanakan modules sebagai script
dapat di gunakan sebagai sript dan juga modul yang dapat di impor, karena kode yang mem-parsing baris perinah
hanya berjalan jika modul dijalankan sebagai file utama.

##### 6.1.2 Jalur pecarian modules
ketika sebuah modul bernama *spam* diimpor, interpreter pertama mencari modul built-in 
dengan nama itu.










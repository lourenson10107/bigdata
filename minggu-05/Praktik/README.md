# BAB 10

## 10.1. Antarmuka Sistem Operasi 
fungsi untuk berinteraksi dengan sistem operasi:
  
    >>> import os
    >>> os.getcwd()      # Return the current working directory
    'C:\\Python37'
    >>> os.chdir('/server/accesslogs')   # Change current working directory
    >>> os.system('mkdir today')   # Run the command mkdir in the system shell
    0
    
Built-in dir()dan help()fungsi berguna sebagai bantuan interaktif untuk bekerja dengan
modul besar seperti os:

    >>> import os
    >>> dir(os)
    <returns a list of all module functions>
    >>> help(os)
    <returns an extensive manual page created from the module's docstrings>
    
modul *shutil* menyediakan antarmuka tingkat yang lebih tinggi dan lebih mudah digunakan
    
    >>> import shutil
    >>> shutil.copyfile('data.db', 'archive.db')
    'archive.db'
    >>> shutil.move('/build/executables', 'installdir')
    'installdir'
   
## 10.2. File Wildcard
modul glob menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard:

    >>> import glob
    >>> glob.glob('*.py')
    ['primes.py', 'random.py', 'quote.py']
    
## 10.3. Argumen Baris Perintah
modul sys sebagai daftar untuk disimpan dalam atribut argv. contohnya seperti dibawah ini :

    >>> import sys
    >>> print(sys.argv)
    ['demo.py', 'one', 'two', 'three']
    

    
## 10.4. Kesalahan Output Redirection dan Penghentian Program   
modul *sys* jga memiliki atribut untuk stdin, stdout, dan stderr yang berguna untuk
memancarka peringatan dan pesan kesalahan  :

    >>> sys.stderr.write('Warning, log file not found starting a new one\n')
    Warning, log file not found starting a new one

## 10.5. Pencocokan Pola String
modul *re* untu pengelolaan string yang canggih. dan untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:
    
    >>> import re
    >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    ['foot', 'fell', 'fastest']
    >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
    'cat in the hat'

## 10.6. Matematika
modul *math* memberikan akses ke mendasari C fungsi perpustakaan untuk
floating point matematika:

    >>> import math
    >>> math.cos(math.pi / 4)
    0.70710678118654757
    >>> math.log(1024, 2)
    10.0

## 10.7. Akses Internet
ada dua modul intuk mengakses internet :
1. urllib.request : untuk mengambil data dari URL
2. smtplib : untuk mengirim email.

      *urllib.request*
      
        >>> from urllib.request import urlopen
        >>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
        ...     for line in response:
        ...         line = line.decode('utf-8')  # Decoding the binary data to text.
        ...         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        ...             print(line)

        <BR>Nov. 25, 09:43:32 PM EST

      *smtplib*
      
        >>> import smtplib
        >>> server = smtplib.SMTP('localhost')
        >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
        ... """To: jcaesar@example.org
        ... From: soothsayer@example.org
        ...
        ... Beware the Ides of March.
        ... """)
        >>> server.quit()

## 10.8. Tanggal dan Waktu
modul *datetime* memasok kelas untuk memanipulasi tanggal dan waktu di kedua 
cara sederhana dan kompleks.

    >>> # dates are easily constructed and formatted
    >>> from datetime import date
    >>> now = date.today()
    >>> now
    datetime.date(2003, 12, 2)
    >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
    '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

    >>> # dates support calendar arithmetic
    >>> birthday = date(1964, 7, 31)
    >>> age = now - birthday
    >>> age.days
    14368

## 10.9. Kompresi Data
Pengarsipan data umum dan kompresi format secara langsung didukung 
oleh modul termasuk: *zlib, gzip, bz2, lzma, zipfiledan tarfile*.

    >>> import zlib
    >>> s = b'witch which has which witches wrist watch'
    >>> len(s)
    41
    >>> t = zlib.compress(s)
    >>> len(t)
    37
    >>> zlib.decompress(t)
    b'witch which has which witches wrist watch'
    >>> zlib.crc32(s)
    226805979  

## 10.10. Pengukuran Kinerja
pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja 
relatif dari pendekatan yang berbeda untuk masalah yang sama. Python 
menyediakan alat pengukuran yang menjawab pertanyaan-pertanyaan itu dengan segera.
modul *timeit* merupakan cara cepat untuk  menunjukkan keunggulan kinerja yang sederhana

    >>> from timeit import Timer
    >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    0.57535828626024577
    >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
    0.54962537085770791

## 10.11. Kontrol Kualitas
modul *doctest* menyediakan alat untukmemindai modul dan memvalidasi tes tertanam dalam docstrings program in

    def average(values):
        """Computes the arithmetic mean of a list of numbers.

        >>> print(average([20, 30, 70]))
        40.0
        """
        return sum(values) / len(values)

    import doctest
    doctest.testmod()   # automatically validate the embedded tests

# BAB 11
## 11.1. Pemformatan Output
modul *reprlib* menyediakan versi *repr()* disesuaikan untuk menampilkan disingkat 
kontainer besar atau sangat bersarang:

    >>> import reprlib
    >>> reprlib.repr(set('supercalifragilisticexpialidocious'))
    "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

## 11.2. Templating
modul *string* ermasuk serbaguna Templatekelas dengan sintaks disederhanakan 
cocok untuk editing oleh pengguna akhir. Ini memungkinkan pengguna untuk 
menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.

    >>> from string import Template
    >>> t = Template('${village}folk send $$10 to $cause.')
    >>> t.substitute(village='Nottingham', cause='the ditch fund')
    'Nottinghamfolk send $10 to the ditch fund.'

## 11.3. Bekerja dengan Tata Letak Rekaman Data Biner
modul *struct* menyediakan pack()dan unpack()fungsi untuk bekerja dengan format 
rekaman biner variabel panjang.

    import struct

    with open('myfile.zip', 'rb') as f:
        data = f.read()

    start = 0
    for i in range(3):                      # show the first 3 file headers
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

        start += 16
        filename = data[start:start+filenamesize]
        start += filenamesize
        extra = data[start:start+extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)

        start += extra_size + comp_size     # skip to the next header

## 11.4. Multi-threading
Threading adalah teknik untuk memisahkan tugas yang tidak tergantung 
secara berurutan. Thread dapat digunakan untuk meningkatkan respon dari 
aplikasi yang menerima input pengguna sementara tugas lain berjalan di latar belakang.

    import threading, zipfile

    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile

        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('Finished background zip of:', self.infile)

    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')

    background.join()    # Wait for the background task to finish
    print('Main program waited until background was done.')

## 11.5. Logging
modul *logging* menawarkan sistem logging fitur dan fleksibel penuh. Pada yang 
paling sederhana, pesan log dikirim ke file atau ke sys.stderr:

    import logging
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')

  *hasil outputnya :*
  
    WARNING:root:Warning:config file server.conf not found
    ERROR:root:Error occurred
    CRITICAL:root:Critical error -- shutting down

## 11.6. Weak References
Python melakukan manajemen memori otomatis (penghitungan referensi untuk 
sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus).
Memori dibebaskan tak lama setelah referensi terakhir untuk itu telah dihapuskan.

    >>> import weakref, gc
    >>> class A:
    ...     def __init__(self, value):
    ...         self.value = value
    ...     def __repr__(self):
    ...         return str(self.value)
    ...
    >>> a = A(10)                   # create a reference
    >>> d = weakref.WeakValueDictionary()
    >>> d['primary'] = a            # does not create a reference
    >>> d['primary']                # fetch the object if it is still alive
    10
    >>> del a                       # remove the one reference
    >>> gc.collect()                # run garbage collection right away
    0
    >>> d['primary']                # entry was automatically removed
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        d['primary']                # entry was automatically removed
      File "C:/python37/lib/weakref.py", line 46, in __getitem__
        o = self.data[key]()
    KeyError: 'primary'

## 11.7. Alat untuk Bekerja dengan Daftar
Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar bawaan. 
Namun, kadang-kadang ada kebutuhan untuk implementasi alternatif dengan 
trade-off kinerja yang berbeda.
modul *array* menyediakan array()objek yang seperti daftar yang menyimpan 
data hanya homogen dan menyimpannya lebih kompak.

    >>> from array import array
    >>> a = array('H', [4000, 10, 700, 22222])
    >>> sum(a)
    26932
    >>> a[1:3]
    array('H', [10, 700])


## 11.8. Aritmatika Titik Apung Desimal
modul *decimal* menawarkan *Decimaldatatype* untuk titik desimal aritmatika 
floating. Dibandingkan dengan float implementasi floating point biner, kelas 
sangat membantu

    >>> from decimal import *
    >>> round(Decimal('0.70') * Decimal('1.05'), 2)
    Decimal('0.74')
    >>> round(.70 * 1.05, 2)
    0.73

# BAB 12
## 12.1. Pendahuluan
Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari pustaka standar. Aplikasi kadang-kadang akan membutuhkan versi tertentu dari sebuah perpustakaan, karena aplikasi mungkin mengharuskan bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi antarmuka perpustakaan yang sudah tidak terpakai.
Ini berarti mungkin tidak mungkin untuk satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A memerlukan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah untuk menciptakan lingkungan virtual , pohon direktori mandiri yang berisi instalasi Python untuk versi tertentu Python, ditambah sejumlah paket tambahan.

## 12.2. Menciptakan Lingkungan Virtual
Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut *venv*. venvbiasanya akan menginstal versi terbaru Python yang Anda miliki.

membuat lingkungan virtual, putuskan direktori tempat Anda ingin menempatkannya, dan jalankan venvmodul sebagai skrip dengan jalur direktori:
    
    python3 -m venv tutorial-env

*Di Windows, jalankan:*

    tutorial-env\Scripts\activate.bat

*Di Unix atau MacOS, jalankan:*

    source tutorial-env/bin/activate

## 12.3. Mengelola Paket dengan pip

Anda dapat menginstal, meng-upgrade, dan menghapus paket menggunakan program 
yang disebut **pip**

    (tutorial-env) $ pip search astronomy
    skyfield               - Elegant astronomy for Python
    gary                   - Galactic astronomy and gravitational dynamics.
    novas                  - The United States Naval Observatory NOVAS astronomy library
    astroobs               - Provides astronomy ephemeris to plan telescope observations
    PyAstronomy            - A collection of astronomy related tools for Python.
    ...  

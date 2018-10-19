# 10. Brief Tour of the Standard Library


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

#

























































































    
    
    
    
    
    
    
    
    



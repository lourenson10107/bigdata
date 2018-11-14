# Pengantar Struktur Data
### DataFrame
*DataFrame* adalah struktur data tabular yang disusun pada kolom dan baris berurut. Untuk membuatnya lebih jelas, mari lihat contoh pembuatan sebuah DataFrame (tabel) dari kamus sebuah daftar. 

Contoh berikut menunjukkan sebuah kamus berisi dua kunci, Name dan Age, dan daftar nilainya.

    import pandas as pd
    import numpy as np
 
    name_age = {'Name' : ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
    'Age' : [32, 55, 20, 43, 30]}
    data_frame = pd.DataFrame(name_age)
    print (data_frame)

hasil yang keluar seperti ini :

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


### Series
*Series* adalah struktur data pandas kedua yang akan saya bicarakan. Series adalah object satu dimensi (1D) yang serupa dengan kolom di dalam tabel. Jika kita ingin membuat sebuah Series untuk daftar nama, kita dapat melakukan di bawah ini:

    series = pd.Series(['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
    index = [1, 2, 3, 4, 5])
    print (series)
    
hasil output :

XXXXXXXXXXXXXXXXXxxxxxxxxxx


# Pelajaran 1

### Create Data
**contoh**

    names = ['Bob','Jessica','Mary','John','Mel']
    births = [968, 155, 77, 578, 973]
untuk menggambungkan data bisa menggunakan perintah *zip*

    zip
    
    BabyDataSet = list(zip(names,births))
    BabyDataSet

**hasil yang di kerjakan :**

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


seperti contoh dibawah ini *df* akan menjadi objek dataframe yang akan disimpan dengan format yang mirip seperti tabel sql
:

    df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
    df
    
hasilnya : 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

### Prepare Data
untuk memeriksa tipe data 

    df.dtypes

untuk memeriksa data dari kolom kelahiran

    df.Births.dtype

hasilnya outpunya bisa dilihat :
.......................................

### Analyze Data

dalam kasus ini, yaitu menemukan nama paling popular atau nama bayi dengan angka
kelahiran tertinggi, bisa digunakan atribut **max** untuk menemukan nilai maksumum dan
juga mengurutkan menggunakan dataframe dan memilih baris atas.

contoh :

    Sorted = df.sort_values(['Births'], ascending=False)
    Sorted.head(1)

hasil :
Names	Births
4	Mel	973

    df['Births'].max()
hasil :
973

atau bisa liat gambar praktik yang di kerjakan :

..............................................................


### Present Data

Di sini kita dapat memplot kolom Kelahiran dan memberi label grafik untuk 
menunjukkan kepada pengguna akhir titik tertinggi pada grafik.

plot () adalah atribut convinient di mana panda memungkinkan Anda dengan 
mudah memplot data dalam dataframe Anda. Kami belajar bagaimana menemukan 
nilai maksimum kolom Kelahiran di bagian sebelumnya. 

    # Create graph
    df['Births'].plot()

    # Maximum value in the data set
    MaxValue = df['Births'].max()

    # Name associated with the maximum value
    MaxName = df['Names'][df['Births'] == df['Births'].max()].values

    # Text to display on graph
    Text = str(MaxValue) + " - " + MaxName

    # Add text to graph
    plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                     xycoords=('axes fraction', 'data'), textcoords='offset points')

    print("The most popular name")
    df[df['Births'] == df['Births'].max()]
    #Sorted.head(1) can also be used


maka keluaran/ output seperti ini:

Nama-nama	Kelahiran
4	Mel	973

*dalam kasus ini grafik tidak muncul, mungkin karna penginstalan lib nya belum benar*

hasil pengerjaan bisa dilihat pada gambar dibwah ini :

.......................................













































































    
    
    
    
    
    
    
    

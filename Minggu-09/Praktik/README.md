## Mencoba Jupyter

**Dasbor Notebook**

<img src="https://github.com/lourenson10107/bigdata/blob/master/Minggu-09/img/dasboard%20jupyter.png">

**Editor Notebook**

<img src="https://github.com/lourenson10107/bigdata/blob/master/Minggu-09/img/notebook%20edytor.png">

## Instalasi Jupyter Notebook

1. menggunakan **Anaconda** :

dengan menginstal anaconda di perangkat komputer anda maka **jupyter** sudah bisa digunakan, karena di dalam **Anaconda** sudah terdapat **Jupyter**

2. menggunakan **PIP** :

dengan memberikan perintah seperti dibwah ini

      python3 -m pip install --upgrade pip
      python3 -m pip install jupyter

## menginstal Karnel

dengan menginstal jupyter maka secara default terinstal karnel *ipython* dan untuk menginstal karnel yang lain maka 
harus menambahkan karnel tambahan, jika menjalankan jupyter pada python 3 kita dapat mengatur karnel python 2 apabila versi
*pip* lebih dari 9.0 

untuk mengecek versi pip bisa menggunakan perintah :

    python2 -m pip --version
      
kemudian untuk melakukan penginstalan karnelnya, bisa menggunakan perintah dibawah ini :

    python2 -m pip install ipykernel
    python2 -m ipykernel install --user

atau menggunakan conda :

    conda create -n ipykernel_py2 python=2 ipykernel
    source activate ipykernel_py2
    python -m ipykernel install --user

dalam perintah di atas menggunakan python 2 apabila ingin menggunakan python 3, maka lakukan langkah yang sama akan tetapi *python2 diganti dengan python 3* 

## Menjalankan Jupyter

untuk memulai bisa menggunakan :

    jupyter notebook
    
kemudian secara otomatis akan menjalankan browser kemudian akan membuka localhost dengan url : http://localhost:8888, dan tampilan yang akan muncul seperti gambar dibawah ini :

<img src="https://github.com/lourenson10107/bigdata/blob/master/Minggu-09/img/tampilan%20awal.png">

**Menjalankan notebook server menggunakan ip atau port khusus :**

     jupyter notebook --port 9999
dalam kasus ini menggunakan port 9999 karena secara default menggunakan port 8888

**Menjalankan notebook server tanpa membuka browser : **

    jupyter notebook --no-browser

**untuk mendapatkan bantuan tentang opsi notebook server**

    jupyter notebook --help

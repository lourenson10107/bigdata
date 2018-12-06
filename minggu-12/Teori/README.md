# Minggu 12

### Selecting Subsets of Data (Memilih Subset Data)

contoh : 
(pastikan sudah menginport semua lib yang di perlukan)

    >>> college = pd.read_csv('data/college.csv', index_col='INSTNM')
    >>> city = college['CITY']
    >>> city.head()

**hasilnya**

    INSTNM
    Alabama A & M University Normal
    University of Alabama at Birmingham Birmingham
    Amridge University Montgomery
    University of Alabama in Huntsville Huntsville
    Alabama State University Montgomery
    Name: CITY, dtype: object


### Selecting DataFrame rows (Memilih baris DataFrame)

contoh penggunaan : 

Baca di dataset perguruan tinggi, dan atur indeks sebagai nama institusi:

    >>> college = pd.read_csv('data/college.csv', index_col='INSTNM')
    >>> college.head()
    
<img src="https://github.com/lourenson10107/img/blob/master/dataaframe.png">






















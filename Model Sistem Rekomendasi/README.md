# **Laporan Proyek Machine Learning - Sandy Tirta Yudha**

## Project Overview

Proyek ini bertujuan untuk membangun sistem rekomendasi smartphone yang dapat membantu pengguna memilih perangkat yang sesuai dengan preferensi dan kebutuhannya. Sistem ini mengintegrasikan berbagai fitur teknis dan performa dari beragam model smartphone untuk menghasilkan rekomendasi yang dipersonalisasi.

**Sumber Dataset** :
1. https://www.kaggle.com/datasets/abdulmalik1518/mobiles-dataset-2025 : Berisi informasi spesifikasi teknis seperti RAM, penyimpanan, ukuran layar, harga, dan fitur lainnya dari berbagai smartphone.
2. https://www.kaggle.com/datasets/ireddragonicy/antutu-benchmark : Menyediakan data skor benchmark performa untuk berbagai perangkat, digunakan untuk menilai kinerja keseluruhan smartphone.

**Metode yang Digunakan:** :
1. Weight Sum Model (WSM) : Pendekatan berbasis multi-kriteria yang memberikan bobot pada setiap fitur penting (misalnya, performa, harga, baterai) untuk menghitung skor total dan mengurutkan pilihan smartphone.


# Business Understanding


## Problem Statement

1. Bagaimana cara membantu pengguna memilih smartphone yang sesuai dengan preferensi dan kebutuhan mereka dari banyaknya pilihan yang tersedia di pasar?

2. Bagaimana mengidentifikasi dan memprioritaskan fitur teknis smartphone yang paling relevan berdasarkan preferensi?

3. Bagaimana membangun sistem rekomendasi yang efisien dan dapat diandalkan berdasarkan data teknis dan benchmark performa?



## Goals

1. Menyediakan sistem rekomendasi smartphone yang dapat memfilter dan menyarankan perangkat terbaik sesuai kebutuhan pengguna.

2. Mengidentifikasi fitur utama yang memengaruhi keputusan pembelian, dan menyusun prioritas penilaian berdasarkan jenis penggunaan.

3. Mengimplementasikan metode berbasis bobot (WSM) yang dapat menghitung skor komposit dari beberapa fitur penting dan mengurutkan pilihan secara objektif.


## Solution Statements
Untuk mencapai tujuan proyek, digunakan pendekatan sistem rekomendasi berbasis multi-kriteria:

1. Menerapkan pendekatan sistem rekomendasi, yaitu Weighted Sum Model (WSM) untuk membangun model dalam memberikan rekomendasi smartphone berdasarkan spesifikasi teknis dan performa.
2. Melakukan eksplorasi data (EDA) untuk menganalisis pengaruh fitur-fitur seperti RAM, kapasitas baterai, dan harga terhadap relevansi smartphone dalam konteks penggunaan gaming.


# Import Library


Mengimpor library yang akan digunakan


```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
import seaborn as sns
import os
import re
import tensorflow as tf
from scipy.stats import boxcox
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from scipy.special import boxcox
from tensorflow.keras.models import load_model
from google.colab import drive
drive.mount('/content/drive')
```




# **Data Understanding**

Proses dimulai dengan membaca dataset utama "Mobiles Dataset (2025).csv" yang telah diunduh dari Kaggle, yang berisi informasi spesifikasi smartphone untuk pelatihan model; namun karena kolom processor hanya mencantumkan nama prosesor tanpa data performa, digunakan dua dataset tambahan dari AnTuTu Benchmark, yaitu Android_SoC.csv dan iOS_Performance.csv, untuk menambahkan skor benchmark sebagai representasi kemampuan prosesor, dan seluruh data kemudian ditransformasikan secara dasar tanpa penambahan atau pengurangan nilai sebagai persiapan untuk tahap Exploratory Data Analysis (EDA).


### Data Loading


```python
file_path = "/content/drive/MyDrive/ML Terapan/Recommendation/Mobiles Dataset (2025).csv"
path_dataset = "/content/drive/MyDrive/ML Terapan/Recommendation/Android_SoC.csv"
```

## **Dataset 1**

Memuat dataset "Mobiles Dataset (2025).csv", yang berisi informasi lengkap mengenai spesifikasi teknis dan fitur berbagai smartphone, seperti RAM, penyimpanan, ukuran layar, kapasitas baterai, kamera, harga, serta jenis prosesor, yang akan digunakan sebagai data utama dalam proses pelatihan model rekomendasi.


```python
file_path = "/content/drive/MyDrive/ML Terapan/Recommendation/Mobiles Dataset (2025).csv"
df_ponsel = pd.read_csv(file_path, encoding="ISO-8859-1")

print("Pratinjau Dataset Ponsel:")
display(df_ponsel.head())
```

```python
print(df_ponsel["Processor"].unique())
```

Program tersebut digunakan untuk menampilkan semua nilai unik yang terdapat dalam kolom **"Processor"** pada dataset smartphone. Tujuan dari langkah ini adalah untuk mengeksplorasi dan memahami keragaman jenis prosesor yang digunakan dalam berbagai perangkat, serta membantu dalam proses analisis lebih lanjut seperti kategorisasi, pengelompokan, atau identifikasi prosesor-prosesor populer dan langka.


```python
df_ponsel = df_ponsel.copy()
pola_merek = r"^(Apple|Samsung|Qualcomm|MediaTek|HiSilicon|Google)\s+"
pola_jaringan = r"\s+(?:5G|4G)$"
df_ponsel["Processor"] = df_ponsel["Processor"].str.replace(pola_merek, "", regex=True) \
                                              .str.replace(pola_jaringan, "", regex=True)

peta_koreksi_prosesor = {
    "Snapdragon 7 Plus Gen 3": "Snapdragon 7+ Gen 3",
    "Dimensity 8000-Max": "Dimensity 8000",
    "Dimensity 7025-Ultra": "Dimensity 7025",
    "Snapdragon 6s 4G Gen 1": "Snapdragon 6 Gen 1",
    "Snapdragon 6s Gen 1": "Snapdragon 6 Gen 1",
    "Snapdragon 7s Gen 1": "Snapdragon 7 Gen 1",
    "Snapdragon 6s Gen 3": "Snapdragon 6 Gen 3",
    "Dimensity 1200-AI": "Dimensity 1200",
    "Dimensity 1300T": "Dimensity 1300",
    "Kirin 710F": "Kirin 710",
    "G35": "Helio G35",
    "G99": "Helio G99",
    "MT6762G Helio G25": "Helio G25",
    "Helio P22T": "Helio P22",
    "Dimensity 8300-Ultra": "Dimensity 8300"
}

df_ponsel["Processor"] = df_ponsel["Processor"].replace(peta_koreksi_prosesor)

print("Hasil Unik (Versi 1):")
print(df_ponsel["Processor"].unique())
```

Data pada kolom **"Processor"** telah diperbarui untuk memastikan konsistensi penulisan dan akurasi nama prosesor. Proses ini mencakup normalisasi nama-nama prosesor yang sebelumnya memiliki ejaan berbeda namun merujuk pada entitas yang sama. Dengan perbaikan ini, analisis selanjutnya—seperti visualisasi, klasifikasi, atau pencarian hubungan terhadap harga dan performa—akan menjadi lebih akurat dan representatif.


```python
df_ponsel.info()
```

Dataset pertama terdiri dari **930 baris data** dan **15 kolom fitur**, yang seluruhnya telah terisi (non-null). Sebagian besar kolom (14 dari 15) memiliki tipe data **object**, yang menunjukkan bahwa meskipun nilainya berupa angka, masih berbentuk **string** atau teks—misalnya pada kolom **RAM**, **Battery Capacity**, dan **Launched Price** di berbagai negara. Hanya kolom **Launched Year** yang bertipe numerik (**int64**). Hal ini menunjukkan bahwa dataset masih perlu dilakukan **pembersihan dan konversi tipe data** (misalnya dari string ke float atau integer) agar dapat dianalisis secara kuantitatif dalam tahap selanjutnya seperti EDA atau pemodelan machine learning.



## **Dataset 2**
Dataset kedua (Android_SoC.csv) memuat informasi mengenai performa berbagai prosesor (SoC) Android, termasuk skor CPU, GPU, dan Total Score berdasarkan benchmark. Data ini akan digunakan untuk melengkapi dataset utama melalui penggabungan berdasarkan nama prosesor.


```python
file_path = "/content/drive/MyDrive/ML Terapan/Recommendation/Android_SoC.csv"
df_chipset = pd.read_csv(file_path)
pd.set_option('display.max_colwidth', None)

print("\nPratinjau Dataset Prosesor:")
display(df_chipset.head())
```

Kolom `Device` yang merepresentasikan nama prosesor memiliki format tidak konsisten, sehingga perlu dilakukan pembersihan (cleaning) agar siap digunakan untuk analisis dan penggabungan data.


```python
df_chipset = df_chipset.copy()

# Definisikan satu fungsi utama untuk membersihkan semua string
def bersihkan_nama_chipset(nama_string):
    """
    Fungsi ini mengambil satu string nama prosesor dan melakukan
    semua langkah pembersihan yang diperlukan.
    """
    if not isinstance(nama_string, str):
        return ""

    # Ekstrak teks
    nama_baru = re.search(r'([^\(]+)', nama_string)
    nama_baru = nama_baru.group(0) if nama_baru else ""

    # Daftar pola regex untuk pembersihan berurutan
    pola_pembersihan = [
        (r"\s+", " "),
        (r'^\d+\s+', ''),
        (r"^(Apple|Samsung|Qualcomm|MediaTek|HiSilicon|Google)\s+", ""),
        (r"\s+(?:5G|4G)$", ""),
    ]

    # Terapkan setiap pola regex
    for pola, pengganti in pola_pembersihan:
        nama_baru = re.sub(pola, pengganti, nama_baru)

    return nama_baru.strip()

# Terapkan fungsi komprehensif ini ke seluruh kolom
df_chipset["Device"] = df_chipset["Device"].apply(bersihkan_nama_chipset)

# Definisikan pemetaan untuk standardisasi nama
peta_standarisasi_chipset = {
    "Dimensity 8200/8200 Ultra": "Dimensity 8200",
    "Kirin 9000S1": "Kirin 9000S",
    "Dimensity 8350 Ultimate": "Dimensity 8350",
    "Snapdragon 888 Plus": "Snapdragon 888+",
    "Snapdragon 480 Plus": "Snapdragon 480+",
    "Dimensity 8400-Max": "Dimensity 8400",
    "Snapdragon 778G Plus": "Snapdragon 778G+",
    "Dimensity 8300-Ultra": "Dimensity 8300"
}

# Terapkan pemetaan
df_chipset["Device"] = df_chipset["Device"].replace(peta_standarisasi_chipset)
df_chipset.head()
```

Kolom Device telah melalui proses pembersihan sehingga format nama prosesor kini konsisten dan siap digunakan dalam tahap analisis lanjutan.


```python
df_chipset.info()
```

Struktur dataset kedua terdiri dari 210 entri dengan 6 kolom, yang mencakup informasi platform, kategori, nama prosesor (Device), serta skor kinerja CPU, GPU, dan total performa berdasarkan benchmark.


## Dataset Merger
Penggabungan dilakukan dengan mencocokkan kolom **"Processor"** dari dataset pertama dan kolom **"Device"** dari dataset kedua, karena keduanya merepresentasikan nama prosesor. Dari dataset kedua, hanya kolom **"Total Score"** yang ditambahkan ke dataset pertama karena sudah mencerminkan gabungan performa CPU dan GPU.



```python
# Merge df1 with df2 based Processor and Device
data_gabungan = df_ponsel.merge(
    df_chipset[["Device", "Total Score"]],
    left_on="Processor",
    right_on="Device",
    how="left"
).rename(
    columns={"Total Score": "Performance Score"}
).drop(
    columns=["Device"]
)

print("Data setelah digabungkan dan dirapikan:")
display(data_gabungan.head())
```

Dataset telah berhasil digabung dengan menambahkan kolom **Performance Score** dari data benchmark, dan selanjutnya dilakukan transformasi data tanpa mengubah isi sebagai persiapan untuk Exploratory Data Analysis (EDA).


```python
# Fungsi ini akan digunakan untuk kolom Kamera dan Ukuran Layar.
def ekstrak_nilai_maksimal(teks):
    """Mencari semua angka dalam string, mengubahnya menjadi float, dan mengembalikan nilai terbesarnya."""
    if pd.isna(teks):
        return np.nan

    # Menemukan semua angka (termasuk desimal) dalam string
    angka_ditemukan = re.findall(r"\d+\.?\d*", str(teks))

    if not angka_ditemukan:
        return np.nan

    return max(map(float, angka_ditemukan))

# Transformasi kolom-kolom spesifik
data_gabungan["Company Name"] = data_gabungan["Company Name"].str.lower()

# Membersihkan dan mengubah tipe data RAM, menangani kasus khusus
data_gabungan["RAM"] = data_gabungan["RAM"].apply(lambda x: "12GB" if "8GB / 12GB" in str(x) else x)
data_gabungan["RAM"] = data_gabungan["RAM"].str.replace("GB", "", regex=False).astype(float)

# Membersihkan dan mengubah tipe data Berat Ponsel dan Kapasitas Baterai
data_gabungan["Mobile Weight"] = data_gabungan["Mobile Weight"].str.replace("g", "", regex=False).astype(float)
data_gabungan["Battery Capacity"] = data_gabungan["Battery Capacity"].str.replace(",", "", regex=False).str.replace("mAh", "", regex=False).astype(float)

# Menerapkan fungsi helper ke kolom Kamera dan Ukuran Layar
kolom_untuk_ekstraksi = ["Front Camera", "Back Camera", "Screen Size"]
for kolom in kolom_untuk_ekstraksi:
    data_gabungan[kolom] = data_gabungan[kolom].apply(ekstrak_nilai_maksimal)

# Membersihkan semua kolom harga
data_gabungan["Launched Price (Pakistan)"] = data_gabungan["Launched Price (Pakistan)"].replace("Not available", np.nan)
data_gabungan["Launched Price (Pakistan)"] = pd.to_numeric(
    data_gabungan["Launched Price (Pakistan)"].str.replace("PKR|,", "", regex=True),
    errors='coerce'
)

# Penanganan untuk kolom harga lainnya
info_harga = {
    "Launched Price (India)": "INR|,",
    "Launched Price (China)": "¥|CNY|,",
    "Launched Price (USA)": "USD|,",
    "Launched Price (Dubai)": "AED|,"
}

for kolom, simbol in info_harga.items():
    data_gabungan[kolom] = data_gabungan[kolom].str.replace(simbol, "", regex=True).astype(float)

# mengganti nama kolom untuk menyertakan satuan
pemetaan_nama_kolom = {
    "Mobile Weight": "Mobile Weight (g)",
    "RAM": "RAM (GB)",
    "Front Camera": "Front Camera (MP)",
    "Back Camera": "Back Camera (MP)",
    "Battery Capacity": "Battery Capacity (mAh)",
    "Screen Size": "Screen Size (inches)",
    "Launched Price (Pakistan)": "Launched Price (Pakistan/PKR)",
    "Launched Price (India)": "Launched Price (India/INR)",
    "Launched Price (China)": "Launched Price (China/CNY)",
    "Launched Price (USA)": "Launched Price (USA/USD)",
    "Launched Price (Dubai)": "Launched Price (Dubai/AED)"
}

data_gabungan.rename(columns=pemetaan_nama_kolom, inplace=True)

print("Tampilan data setelah transformasi:")
display(data_gabungan.head())
```

Tabel di atas merupakan hasil transformasi dari proses penggabungan dua dataset berdasarkan kolom Processor (pada dataset 1) dan kolom Device (pada dataset 2). Seluruh kolom numerik seperti berat ponsel, RAM, kamera depan dan belakang, kapasitas baterai, ukuran layar, serta harga peluncuran dalam berbagai mata uang telah dibersihkan dan dikonversi ke format numerik yang seragam. Selain itu, kolom Performance Score ditambahkan dari dataset kedua sebagai representasi gabungan dari skor CPU dan GPU. Nilai pada kolom ini digunakan untuk menilai performa keseluruhan prosesor setiap ponsel.

Namun, masih terdapat nilai kosong (NaN) pada kolom Performance Score, yang menunjukkan bahwa tidak semua prosesor pada dataset utama memiliki padanan skor performa dalam dataset kedua. Meskipun demikian, hasil transformasi ini sudah siap digunakan untuk tahap Exploratory Data Analysis (EDA) dan pengolahan data lanjutan tanpa mengubah informasi asli dari dataset awal.


# Exploratory Data Analysis (EDA)

Setelah memperoleh dataset, langkah berikutnya adalah melakukan Exploratory Data Analysis (EDA), yaitu proses analisis awal untuk memahami struktur, pola distribusi, serta hubungan antar fitur dalam data sebelum membangun model. Tujuan utama EDA adalah mengidentifikasi nilai kosong (missing values), pencilan (outliers), sebaran data, dan korelasi antar variabel guna menentukan strategi preprocessing yang sesuai.

EDA biasanya dilakukan dengan pendekatan statistik deskriptif seperti menghitung rata-rata, median, dan deviasi standar, serta visualisasi data menggunakan grafik seperti histogram, boxplot, dan scatter plot. Melalui EDA, kita dapat mengungkap potensi isu dalam data dan melakukan penyesuaian awal yang penting agar proses pemodelan machine learning dapat berjalan lebih efektif dan menghasilkan output yang akurat.


## Deskripsi Variabel


```python
data_gabungan.info()
```

Langkah pertama dalam eksplorasi data adalah **menganalisis struktur dataset** untuk memahami jenis data yang tersedia. Berdasarkan output di atas, dataset ini terdiri dari **934 entri ponsel** dan **16 kolom fitur**, yang mencakup informasi lengkap terkait spesifikasi perangkat keras, harga peluncuran dalam berbagai mata uang, tahun peluncuran, serta skor performa perangkat.

Berikut adalah deskripsi masing-masing kolom dalam dataset:

1. **Company Name** *(object)* – Menunjukkan nama produsen atau merek ponsel, seperti *Apple, Samsung, Xiaomi, Oppo*.
2. **Model Name** *(object)* – Menampilkan nama model spesifik dari ponsel, misalnya *iPhone 16 128GB*, *Galaxy S24 Ultra*, dll.
3. **Mobile Weight (g)** *(float64)* – Berat ponsel dalam gram, berpengaruh terhadap kenyamanan penggunaan fisik.
4. **RAM (GB)** *(float64)* – Kapasitas RAM dalam gigabyte, memengaruhi kemampuan multitasking perangkat.
5. **Front Camera (MP)** *(float64)* – Resolusi kamera depan dalam megapiksel, menentukan kualitas foto selfie dan video call.
6. **Back Camera (MP)** *(float64)* – Resolusi kamera belakang utama dalam megapiksel, berperan penting dalam hasil fotografi utama.
7. **Processor** *(object)* – Jenis prosesor atau chipset yang digunakan, seperti *A17 Bionic*, *Snapdragon 8 Gen 2*, *Dimensity 9200*, dll.
8. **Battery Capacity (mAh)** *(float64)* – Kapasitas baterai dalam satuan mAh, memengaruhi daya tahan perangkat selama penggunaan.
9. **Screen Size (inches)** *(float64)* – Ukuran diagonal layar dalam inci, mempengaruhi tampilan visual dan kenyamanan pengguna.
10. **Launched Price (Pakistan/PKR)** *(float64)* – Harga peluncuran dalam mata uang Rupee Pakistan. Memiliki beberapa nilai kosong.
11. **Launched Price (India/INR)** *(float64)* – Harga peluncuran dalam Rupee India.
12. **Launched Price (China/CNY)** *(float64)* – Harga peluncuran dalam Yuan Tiongkok.
13. **Launched Price (USA/USD)** *(float64)* – Harga peluncuran dalam Dolar Amerika Serikat.
14. **Launched Price (Dubai/AED)** *(float64)* – Harga peluncuran dalam Dirham Uni Emirat Arab.
15. **Launched Year** *(int64)* – Tahun saat ponsel tersebut pertama kali dirilis ke pasar.
16. **Performance Score** *(float64)* – Skor performa keseluruhan dari prosesor ponsel, berdasarkan data benchmark seperti *AnTuTu*, yang mencerminkan gabungan kemampuan CPU dan GPU. Beberapa entri masih memiliki nilai kosong pada kolom ini.

Dari keseluruhan fitur, kolom harga peluncuran dalam berbagai mata uang dapat dijadikan **variabel target** untuk analisis prediktif atau sistem rekomendasi harga, sementara fitur-fitur seperti spesifikasi perangkat dan performa dapat berfungsi sebagai **variabel input (independen)** untuk mendukung analisis tersebut.


```python
data_gabungan.describe()
```

Berdasarkan hasil deskriptif statistik dari fitur numerik dalam dataset, dapat disimpulkan beberapa hal penting sebagai berikut:

1. **Launched Year (Tahun Peluncuran)**

   * Perangkat dalam dataset diluncurkan dalam rentang waktu antara **2014 hingga 2025**, dengan median tahun peluncuran berada di tahun **2023**, menunjukkan dominasi data dari perangkat modern.

2. **Launched Price (Harga Peluncuran)**

   * Harga peluncuran bervariasi secara signifikan antar negara.

     * Di Pakistan (PKR): berkisar dari **15.999** hingga **604.999 PKR**
     * Di India (INR): mulai dari **5.999** hingga **274.999 INR**
     * Di China (CNY): antara **499** hingga **17.999 CNY**
     * Di Amerika Serikat (USD): dari **79 USD** hingga **39.622 USD**
     * Di Dubai (AED): dari **299** hingga **11.099 AED**
   * Perbedaan rentang harga ini mencerminkan keberagaman **kelas perangkat** (entry-level hingga flagship), namun juga mengindikasikan potensi **outlier** yang perlu diperiksa lebih lanjut.

3. **Screen Size (Ukuran Layar)**

   * Ukuran layar berkisar dari **5.0 hingga 14.6 inci**, dengan median **6.67 inci**, sesuai dengan standar smartphone saat ini. Nilai maksimum kemungkinan berasal dari perangkat tablet.

4. **Battery Capacity (Kapasitas Baterai)**

   * Kapasitas baterai berkisar antara **2000 mAh** hingga **11.200 mAh**.
   * Nilai ekstrem menunjukkan kemungkinan keberadaan perangkat **non-smartphone standar**, seperti tablet, gaming phone, atau rugged device.

5. **RAM (Memori)**

   * RAM tersedia dari **1 GB hingga 16 GB**, dengan nilai median **8 GB**.
   * Distribusi ini merepresentasikan spektrum produk dari **ponsel murah hingga premium**.

6. **Front Camera (Kamera Depan)**

   * Resolusi kamera depan berkisar antara **2 MP hingga 60 MP**, dengan nilai rata-rata sekitar **18 MP**.

7. **Back Camera (Kamera Belakang)**

   * Resolusi kamera belakang sangat bervariasi, dari **5 MP hingga 200 MP**, yang menunjukkan peningkatan signifikan pada kualitas fotografi di ponsel masa kini.

8. **Mobile Weight (Berat Ponsel)**

   * Berat ponsel berkisar antara **135 gram** hingga **732 gram**, dengan rata-rata **228 gram**.
   * Nilai maksimum yang tinggi menunjukkan kemungkinan adanya **perangkat lipat, tablet kecil, atau rugged phone**.

9. **Performance Score (Skor Performa)**

   * Skor performa berdasarkan benchmark berkisar dari **25.673** hingga **1.709.461**, dengan nilai median sekitar **291.832**.
   * Rentang ini mencerminkan perbedaan kemampuan antara perangkat **entry-level** dan **flagship terbaru**.

10. **Missing Values (Data Hilang)**

* Hanya terdapat **satu nilai yang hilang** pada kolom **Launched Price (Pakistan/PKR)**, sehingga **penanganan missing value** dapat dilakukan dengan pendekatan sederhana seperti imputasi median atau mean.



```python
data_gabungan.shape
```

## Univariate Analysis

Univariate Analysis merupakan proses analisis satu variabel untuk memahami distribusi dan karakteristiknya. Analisis ini biasanya dilakukan melalui visualisasi seperti histogram, boxplot, dan countplot agar pola data lebih mudah diamati.

Dalam dataset ini, terdapat dua jenis fitur:

* **Fitur Numerik**:
  Meliputi `Mobile Weight (g)`, `RAM (GB)`, `Front Camera (MP)`, `Back Camera (MP)`, `Battery Capacity (mAh)`, `Screen Size (inches)`, berbagai kolom harga peluncuran (`Launched Price` dalam PKR, INR, CNY, USD, AED), serta `Launched Year`. Semua fitur ini bersifat kontinu.

* **Fitur Kategorikal**:
  Termasuk `Company Name`, `Model Name`, dan `Processor`, yang berisi data berupa label atau kategori.

Analisis univariat akan membantu mendeteksi pola umum, outlier, serta distribusi nilai dari masing-masing fitur sebelum melanjutkan ke tahap analisis multivariat atau pemodelan.



```python
# Daftar kolom yang berisi data kuantitatif atau numerik (angka)
kolom_numerik = [
    "Mobile Weight (g)",
    "RAM (GB)",
    "Front Camera (MP)",
    "Back Camera (MP)",
    "Battery Capacity (mAh)",
    "Screen Size (inches)",
    "Launched Price (Pakistan/PKR)",
    "Launched Price (India/INR)",
    "Launched Price (China/CNY)",
    "Launched Price (USA/USD)",
    "Launched Price (Dubai/AED)",
    "Launched Year",
    "Performance Score"
]

# Daftar kolom yang berisi data kualitatif atau kategorikal (teks/label)
kolom_kategorikal = [
    "Company Name",
    "Model Name",
    "Processor"
]

print("Fitur Numerik:", kolom_numerik)
print("\nFitur Kategorikal:", kolom_kategorikal)
```

### Categorical Features


```python
sns.set_theme(style="whitegrid")

print("--- Analisis Distribusi Fitur Kategorikal ---")
for fitur in kolom_kategorikal:
    print(f"\n\n================ Analisis untuk Fitur: {fitur} ================")

    frekuensi_data = data_gabungan[fitur].value_counts()
    persentase_data = (frekuensi_data / len(data_gabungan)) * 100

    tabel_ringkasan = pd.DataFrame({
        'Frekuensi': frekuensi_data,
        'Persentase (%)': persentase_data.round(1)
    })

    print("Tabel Ringkasan Distribusi:")
    print(tabel_ringkasan)

    plt.figure(figsize=(12, 6))
    plot_distribusi = sns.countplot(
        data=data_gabungan,
        y=fitur,
        order=frekuensi_data.index,
        palette='viridis'
    )

    plot_distribusi.set_title(f'Distribusi Data untuk Fitur "{fitur}"', fontsize=16)
    plot_distribusi.set_xlabel('Jumlah Sampel (Frekuensi)', fontsize=12)
    plot_distribusi.set_ylabel(f'Kategori {fitur}', fontsize=12)

    plt.tight_layout()
    plt.show()
```

![Output 0](images_submission/output_0.png)

![Output 1](images_submission/output_1.png)

![Output 2](images_submission/output_2.png)

Berdasarkan analisis data yang disajikan, dapat disimpulkan bahwa dataset ponsel ini didominasi oleh beberapa merek populer, dengan Oppo menjadi yang paling banyak muncul (13.8%), diikuti oleh Apple (10.4%) dan Samsung (9.9%). Sebaliknya, merek seperti iQOO dan Sony memiliki jumlah perwakilan yang sangat sedikit.

Salah satu karakteristik paling menonjol dari dataset ini adalah keragaman yang sangat tinggi pada fitur nama model dan prosesor. Terdapat ratusan model ponsel yang unik, di mana sebagian besar model hanya memiliki satu atau dua sampel, yang menunjukkan bahwa koleksi data tidak terfokus pada beberapa perangkat populer saja, melainkan mencakup spektrum pasar yang luas.

Demikian pula, variasi yang signifikan ditemukan pada jenis prosesor yang digunakan. Meskipun chipset unggulan seperti Snapdragon 8 Gen 2 menjadi yang paling umum, terdapat lebih dari dua ratus jenis prosesor berbeda dalam dataset, dengan banyak di antaranya hanya muncul sekali. Secara keseluruhan, dataset ini mencerminkan lanskap pasar ponsel yang sangat beragam dengan spesifikasi yang bervariasi, meskipun sampelnya lebih cenderung berasal dari merek-merek terkemuka.


### Numerical Features


```python
kolom_numerik = data_gabungan.select_dtypes(include='number').columns
fig = plt.figure(figsize=(20, 15))

for i, nama_kolom in enumerate(kolom_numerik):
    ax = fig.add_subplot( (len(kolom_numerik) + 3) // 4, 4, i + 1)
    data_gabungan[nama_kolom].hist(ax=ax, bins=50)
    ax.set_title(f'Distribusi {nama_kolom}')

fig.tight_layout()
plt.show()
```

![Output 3](images_submission/output_3.png)

### **Distribusi Fitur Numerik – Analisis Visual**

1. **Mobile Weight (g)**

   * Distribusi berat ponsel cenderung terkonsentrasi pada kisaran **190 gram**, yang juga merupakan nilai median dari data.
   * Meskipun sebagian besar perangkat memiliki bobot dalam kisaran wajar, terdapat **outlier dengan bobot sangat tinggi** (hingga lebih dari 700 gram), yang kemungkinan berasal dari perangkat khusus seperti tablet atau rugged phone.

2. **RAM (GB)**

   * RAM paling umum adalah **8 GB**, diikuti oleh **4 GB**, **6 GB**, dan **12 GB**.
   * Distribusi menunjukkan kecenderungan pabrikan untuk menetapkan RAM pada jumlah tertentu, terutama kelipatan genap, dengan **8 GB sebagai standar umum** saat ini.

3. **Front Camera (MP)**

   * Resolusi kamera depan memiliki sebaran yang cukup variatif, dengan puncak jumlah sampel berada di sekitar **8 MP**, **17 MP**, dan **32 MP**.
   * Tidak terdapat pola distribusi yang jelas, namun sebagian besar perangkat memiliki resolusi antara **5 hingga 32 MP**.

4. **Back Camera (MP)**

   * Kamera belakang paling sering ditemukan pada resolusi **50 MP**, dengan puncak distribusi sangat mencolok.
   * Rentang resolusi sangat luas hingga **200 MP**, namun sebagian besar data terkonsentrasi pada resolusi di bawah **75 MP**.

5. **Battery Capacity (mAh)**

   * Kapasitas baterai menunjukkan distribusi yang **cukup simetris dengan puncak di 5000 mAh**, menjadikannya kapasitas standar di banyak perangkat.
   * Mayoritas perangkat memiliki baterai di bawah **6000 mAh**, sementara nilai ekstrem di atas 8000 mAh sangat jarang.

6. **Screen Size (inches)**

   * Ukuran layar didominasi oleh perangkat dengan ukuran antara **6 hingga 6.8 inci**, dengan nilai terbanyak sekitar **6.7 inci**.
   * Terdapat outlier dengan ukuran layar lebih dari **10 inci**, yang kemungkinan berasal dari tablet.

7. **Launched Price (PKR, INR, CNY, USD, AED)**

   * Distribusi harga peluncuran di berbagai negara menunjukkan pola yang **mirip dan miring ke kanan (right-skewed)**.
   * Artinya, sebagian besar perangkat memiliki harga **di kisaran rendah hingga menengah**, sedangkan **hanya sedikit perangkat dengan harga sangat tinggi**, mencerminkan kelas flagship atau premium.

8. **Launched Year**

   * Jumlah perangkat meningkat signifikan setiap tahun, dengan **puncak tertinggi pada tahun 2024**, menandakan bahwa mayoritas data berasal dari perangkat terbaru.
   * Distribusi **miring ke kiri (left-skewed)**, mengindikasikan dominasi perangkat modern dalam dataset.

9. **Performance Score**

   * Skor performa memiliki distribusi yang **menyebar luas dan tidak teratur**, namun lebih dari **setengah perangkat memiliki skor di bawah 500.000**.
   * Ini menunjukkan banyaknya perangkat dengan kinerja sedang hingga rendah, meskipun terdapat juga flagship dengan skor di atas 1 juta.


## Multivariate Analysis

Tahap selanjutnya adalah melakukan Analisis Multivariat, yaitu pendekatan statistik yang digunakan untuk mengevaluasi hubungan antara dua atau lebih variabel dalam sebuah dataset. Tujuan utamanya adalah untuk mengidentifikasi pola, keterkaitan, atau korelasi antar fitur yang dapat memberikan wawasan lebih mendalam serta mendukung proses pemodelan dan pengambilan keputusan.
Pada analisis ini, variabel `Launched Price (China/CNY)` dipilih sebagai fokus korelasi, karena Tiongkok merupakan negara produsen smartphone terbesar di dunia, sehingga harga peluncuran di wilayah ini dinilai paling representatif sebagai acuan utama.


### Categorical Features


```python
# Loop melalui setiap kolom kategorikal
for col in kolom_kategorikal:
    if col == 'Model Name':
        print("Membuat plot khusus untuk 'Model Name' (20 termahal)...")

        # Hitung rata-rata harga untuk setiap model
        harga_per_model = data_gabungan.groupby('Model Name')['Launched Price (China/CNY)'].mean()

        # Urutkan dan ambil 20 model teratas
        top_20_models = harga_per_model.sort_values(ascending=False).head(20)

        # Buat visualisasi untuk data yang sudah diringkas ini
        plt.figure(figsize=(15, 7))
        ax = sns.barplot(x=top_20_models.index, y=top_20_models.values, palette='viridis')

        ax.set_title('Rata-rata Harga untuk 20 Model Termahal', fontsize=16)
        ax.set_xlabel('Model Name', fontsize=12)
        ax.set_ylabel('Rata-rata Harga (CNY)', fontsize=12)
        plt.xticks(rotation=45, ha='right')

    else:
        plt.figure(figsize=(12, 5))

        ax = sns.barplot(x=col, y="Launched Price (China/CNY)", data=data_gabungan, palette="Set3", errorbar=None)

        ax.set_title(f"Rata-rata Harga Peluncuran (China/CNY) Berdasarkan {col}", fontsize=14)
        ax.set_xlabel(col, fontsize=12)
        ax.set_ylabel('Rata-rata Harga (China/CNY)', fontsize=12)

    plt.tight_layout()
plt.show()
```

![Output 4](images_submission/output_4.png)

![Output 5](images_submission/output_5.png)

![Output 6](images_submission/output_6.png)

Dari analisis data grafik, dapat disimpulkan bahwa harga ponsel sangat dipengaruhi oleh tiga faktor utama:

1. `Merek (Company Name)`: Merek adalah penentu harga yang paling kuat. Terdapat kesenjangan harga yang jelas antara merek premium seperti Apple dan Huawei dibandingkan dengan merek yang lebih ekonomis.

2. `Model`: Jenis model spesifik, terutama yang inovatif seperti ponsel lipat (contoh: Galaxy Z Fold), secara drastis meningkatkan harga. Ini menunjukkan bahwa teknologi pada model lebih berpengaruh daripada sekadar namanya.

3. `Prosesor`: Chipset kelas atas (flagship) secara konsisten ditemukan pada ponsel berharga mahal, sementara mayoritas prosesor lain digunakan untuk perangkat di segmen harga menengah ke bawah.


### Numerical Features


```python
sns.pairplot(data_gabungan, diag_kind = 'kde')
```

![Output 7](images_submission/output_7.png)

Dari grafik pairplot diatas, jika fokus pada sumbu "Launched Price (China/CNY)" dimana merupakan fitur target, dapat disimpulkan bahwa:

Fitur `Performance Score` menunjukkan korelasi positif yang paling jelas dengan harga; semakin tinggi skor performa, semakin tinggi pula harganya. Fitur-fitur lain seperti `ukuran layar`, `kapasitas baterai`, dan `berat ponsel` juga memperlihatkan tren positif yang serupa, meskipun lebih lemah, di mana kenaikannya cenderung diikuti oleh kenaikan harga.

Sementara itu, fitur seperti `RAM`, `resolusi kamera`, dan `tahun peluncuran` menunjukkan pola yang sangat acak terhadap harga, yang mengindikasikan bahwa fitur-fitur ini bukanlah prediktor harga yang baik secara individual. Adapun kolom harga dalam mata uang lain (USD, INR, dll.) memiliki korelasi linear yang sangat kuat karena pada dasarnya merepresentasikan nilai yang sama, sehingga bersifat redundan dan tidak perlu dianalisis lebih lanjut sebagai fitur prediktor.


```python
corr_df = data_gabungan[kolom_numerik].corr().round(2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_df, annot=True, cmap='RdBu_r', fmt=".2f", linewidths=0.5, ax=ax)
ax.set_title('Matriks Korelasi Antar Fitur Numerik', fontsize=20)

plt.show()
```

![Output 8](images_submission/output_8.png)

### **Analisis Korelasi Antar Fitur Numerik**

Berdasarkan matriks korelasi, beberapa hubungan yang menonjol antara fitur-fitur numerik dapat diidentifikasi sebagai berikut:

1. **Korelasi Harga Peluncuran Antar Negara**

   * Harga peluncuran di negara-negara berbeda (PKR, INR, CNY, USD, AED) menunjukkan **korelasi sangat kuat satu sama lain** (nilai korelasi > 0.9), menandakan bahwa harga antar negara bergerak **proporsional dan saling mengikuti**.
   * Fitur-fitur harga ini juga memiliki korelasi yang **cukup tinggi dengan skor performa** (sekitar 0.68–0.71), menunjukkan bahwa **perangkat yang lebih mahal cenderung memiliki performa lebih tinggi**.

2. **RAM (GB)**

   * Memiliki korelasi cukup tinggi dengan **Performance Score** (0.72), mengindikasikan bahwa semakin besar RAM, semakin tinggi pula skor performa.
   * RAM juga berkorelasi cukup signifikan dengan harga peluncuran di semua negara (sekitar 0.42–0.48), terutama **Launched Price China/CNY (0.43)**.

3. **Mobile Weight (g)**

   * Memiliki **korelasi sangat kuat dengan Screen Size (0.98)** dan **Battery Capacity (0.85)**.
   * Artinya, **ponsel yang lebih besar dan berbaterai lebih kuat cenderung memiliki bobot yang lebih berat**, yang konsisten secara fisik.

4. **Screen Size (inches)**

   * Berkorelasi kuat dengan **Battery Capacity (0.88)** dan **Mobile Weight**, memperkuat temuan bahwa **ponsel dengan layar besar biasanya memiliki kapasitas baterai besar dan bobot lebih tinggi**.

5. **Performance Score**

   * Selain dengan RAM, skor performa juga berkorelasi kuat dengan **Launched Price di beberapa negara**:

     * PKR: 0.71
     * INR: 0.70
     * CNY: 0.70
     * USD: 0.68
     * AED: 0.67
   * Ini menegaskan bahwa **performa ponsel sangat terkait dengan harga**, khususnya pada perangkat flagship atau premium.

6. **Kamera dan Tahun Peluncuran**

   * Kamera depan dan belakang menunjukkan korelasi rendah terhadap performa dan harga.
   * Tahun peluncuran hanya memiliki **korelasi lemah hingga sedang terhadap fitur lainnya**, namun cenderung naik bersamaan dengan **RAM, kamera, dan performa**, mencerminkan peningkatan teknologi dari tahun ke tahun.


# **Data Preparation**

Setelah melakukan eksplorasi data, tahap selanjutnya adalah data preparation yang bertujuan untuk memastikan kualitas data sebelum digunakan dalam model machine learning. Tahapan ini mencakup pembersihan data dengan menangani missing values dan outlier, transformasi fitur agar distribusinya lebih normal, serta encoding variabel kategorikal menggunakan metode seperti one-hot atau label encoding. Selain itu, dilakukan juga reduksi dimensi untuk mengurangi kompleksitas data dan menghindari overfitting, serta standarisasi atau normalisasi fitur numerik agar berada pada skala yang seragam. Seluruh data kemudian dibagi menjadi data latih dan data uji untuk keperluan pelatihan dan evaluasi model secara adil dan terukur.


```python
data_gabungan.info()
```

Dataset yang digunakan memiliki total 16 fitur, terdiri dari 12 fitur numerik bertipe float64, 1 fitur numerik bertipe int64, dan 3 fitur kategorikal bertipe object. Semua fitur memiliki 934 entri, namun terdapat missing value pada dua fitur: Launched Price (Pakistan/PKR) dengan 1 nilai yang hilang, dan Performance Score dengan 224 nilai yang hilang. Struktur ini mencerminkan bahwa data masih berada dalam kondisi awal, sebelum dilakukan proses pembersihan dan transformasi lebih lanjut.


```python
data_gabungan.drop(columns=["Launched Price (Pakistan/PKR)", "Launched Price (India/INR)",
                              "Launched Price (USA/USD)", "Launched Price (Dubai/AED)",
                              "Processor"], inplace=True)

data_gabungan.head()
```

Sebagai langkah awal dalam proses data preparation, dilakukan penghapusan beberapa fitur yang dianggap redundan atau tidak relevan untuk sistem rekomendasi. Fitur-fitur seperti **"Launched Price (Pakistan/PKR)"**, **"Launched Price (India/INR)"**, **"Launched Price (USA/USD)"**, dan **"Launched Price (Dubai/AED)"** dihapus karena informasi harga sudah cukup diwakili oleh **"Launched Price (China/CNY)"**. Selain itu, fitur **"Processor"** juga dihapus karena kemampuannya telah direpresentasikan secara lebih kuantitatif oleh fitur **"Performance Score"**, sehingga tidak perlu dimasukkan kembali.


```python
data_gabungan.info()
```

Setelah dilakukan proses penghapusan fitur, struktur dataset kini terdiri dari 11 kolom. Kolom-kolom seperti **"Launched Price (Pakistan/PKR)"**, **"Launched Price (India/INR)"**, **"Launched Price (USA/USD)"**, **"Launched Price (Dubai/AED)"**, dan **"Processor"** telah dihapus karena dianggap tidak diperlukan. Dataset saat ini telah lebih ringkas dan fokus pada fitur-fitur utama yang relevan untuk pengembangan sistem rekomendasi smartphone, termasuk fitur numerik seperti berat, RAM, kamera, kapasitas baterai, ukuran layar, harga dalam CNY, tahun rilis, serta skor performa.


Cek Missing Value


```python
data_gabungan.isnull().sum()
```

Kode program tersebut digunakan untuk mendeteksi nilai yang hilang (missing values) pada setiap kolom dalam dataset. Hasilnya menunjukkan bahwa hanya kolom **"Performance Score"** yang memiliki **224 nilai kosong (missing)**, sementara kolom lainnya lengkap. Kemungkinan besar, hal ini terjadi akibat proses penggabungan dua dataset sebelumnya, di mana sebagian data dari salah satu dataset tidak memiliki nilai performa yang tersedia.


```python
missing_values_performance_score = data_gabungan["Performance Score"].isna().groupby(data_gabungan["Company Name"]).sum()
print(missing_values_performance_score)
```

Berdasarkan data di atas, terlihat bahwa sebagian besar perangkat dengan nilai `Performance Score` yang hilang berasal dari merek **Apple**, yang memiliki 97 entri. Hal ini kemungkinan disebabkan oleh keterbatasan pada dataset kedua yang digunakan dalam proses penggabungan, di mana data benchmark performa yang tersedia hanya mencakup prosesor atau SoC untuk perangkat **Android**. Akibatnya, perangkat non-Android seperti iPhone tidak memiliki nilai performa yang dapat dipadankan, sehingga kolom `Performance Score` untuk merek Apple menjadi kosong.


## Menangani Missing Values & Outliers

Langkah kedua dalam proses data preparation adalah penanganan missing values dan outliers. Berdasarkan hasil sebelumnya, ditemukan cukup banyak data kosong khususnya pada perangkat Apple. Untuk menjaga keakuratan dan relevansi nilai pada fitur `Performance Score`—yang memiliki peran krusial dalam analisis—diputuskan untuk menghapus seluruh baris yang mengandung missing values, alih-alih melakukan imputasi.

Sementara itu, untuk mengatasi outliers, digunakan metode **Box-Cox Transformation**, yaitu teknik transformasi non-linear yang diterapkan pada fitur numerik dengan nilai positif guna menormalkan distribusi data sekaligus mereduksi pengaruh outliers.

Adapun alasan memilih metode Box-Cox antara lain:

* Dapat menangani outliers tanpa harus menghapus data, sehingga tidak ada informasi yang hilang, hanya bentuk distribusinya yang diubah.
* Membantu membuat distribusi data lebih mendekati normal, yang penting untuk model regresi atau teknik statistik lain yang mengasumsikan normalitas.
* Lebih unggul dibanding log transformation, karena Box-Cox mampu menyesuaikan jenis transformasi secara otomatis sesuai pola distribusi data, sehingga hasilnya lebih optimal.



```python
df = data_gabungan[data_gabungan["Performance Score"].notnull()]
missing_summary = df.isnull().sum()
print(missing_summary)

df_original = df.copy()
```

Setelah proses penghapusan baris dengan nilai kosong dilakukan, kini seluruh kolom pada dataset telah bersih dari missing values, termasuk kolom Performance Score yang sebelumnya memiliki banyak nilai kosong. Dengan demikian, dataset telah siap untuk tahapan analisis dan pemodelan lebih lanjut.


```python
df.info()
```

Setelah proses pembersihan data dilakukan, dataset kini terdiri dari 710 entri yang lengkap dan bebas dari missing values. Seluruh fitur yang tersisa, baik numerik maupun kategorikal, telah siap digunakan untuk tahap analisis lebih lanjut.


```python
df.describe()
```

```python
# Visualisasi outlier menggunakan boxplot untuk setiap fitur numerik
fitur_numerik = df.select_dtypes(include='number').columns
jumlah_fitur = len(fitur_numerik)
jumlah_baris = (jumlah_fitur + 3) // 4

fig, ax_array = plt.subplots(nrows=jumlah_baris, ncols=4, figsize=(15, jumlah_baris * 4))
ax_array = ax_array.flatten()

for idx, kolom in enumerate(fitur_numerik):
    sns.boxplot(data=df, x=kolom, ax=ax_array[idx])
    ax_array[idx].set_title(kolom)

for k in range(idx + 1, len(ax_array)):
    fig.delaxes(ax_array[k])

plt.tight_layout()
plt.show()
```

![Output 9](images_submission/output_9.png)

Gambar boxplot di atas menunjukkan bahwa hampir semua fitur numerik dalam dataset memiliki outlier, ditandai dengan titik-titik di luar batas kotak plot. Fitur seperti Launched Price, Battery Capacity, Screen Size, dan Performance Score terlihat memiliki banyak nilai ekstrem. Oleh karena itu, diperlukan penanganan lebih lanjut, seperti menggunakan transformasi Box-Cox, agar distribusi data menjadi lebih normal dan dampak outlier terhadap model dapat diminimalkan tanpa kehilangan informasi penting.


```python
from scipy.stats import boxcox
import numpy as np

data_transformed = df.copy()

fitur_numerik = [
    "Mobile Weight (g)", "Back Camera (MP)",
    "Battery Capacity (mAh)", "Screen Size (inches)",
    "Launched Price (China/CNY)", "Performance Score"
]

nilai_lambda_boxcox = {}
nilai_shift_boxcox = {}

for kolom in fitur_numerik:
    min_val = data_transformed[kolom].min()
    if min_val <= 0:
        shift = abs(min_val) + 1e-6
        data_transformed[kolom] = data_transformed[kolom] + shift
        nilai_shift_boxcox[kolom] = shift
    else:
        nilai_shift_boxcox[kolom] = 0

    transformed_values, lambda_val = boxcox(data_transformed[kolom])
    data_transformed[kolom] = transformed_values
    nilai_lambda_boxcox[kolom] = lambda_val

print("Transformasi Box-Cox selesai.")
```

Kode di atas menerapkan transformasi Box-Cox pada beberapa fitur numerik dalam dataset untuk mengatasi outlier tanpa harus menghapus atau mengubah nilai asli secara drastis. Dengan cara ini, distribusi data menjadi lebih mendekati normal dan pengaruh nilai ekstrem bisa diminimalkan.


```python
# Menampilkan boxplot untuk mendeteksi outlier pada fitur numerik
kolom_numerik = df.select_dtypes(include='number').columns
total_plot = len(kolom_numerik)
baris = total_plot // 4 + int(total_plot % 4 != 0)

fig, sumbu = plt.subplots(nrows=baris, ncols=4, figsize=(15, 4 * baris))
sumbu = sumbu.flatten()

for idx, kolom in enumerate(kolom_numerik):
    sns.boxplot(x=df[kolom], ax=sumbu[idx])
    sumbu[idx].set_title(kolom)

for kosong in range(idx + 1, len(sumbu)):
    fig.delaxes(sumbu[kosong])

plt.tight_layout()
plt.show()
```

![Output 10](images_submission/output_10.png)

Setelah transformasi Box-Cox, distribusi data menjadi lebih normal dan outlier berkurang. Meski beberapa outlier masih ada, datanya kini lebih siap untuk analisis atau pemodelan lanjutan.


## Encoding for Categorical Feature

Langkah ketiga dalam data preparation adalah mengubah fitur kategorikal menjadi format numerik agar dapat digunakan dalam model machine learning.

### Teknik yang Digunakan:

* **Target Encoding** untuk `Company Name`:
  Mengubah nama perusahaan menjadi nilai berdasarkan rata-rata *Performance Score* masing-masing. Metode ini mempertahankan hubungan antara merek dan performa tanpa menambah dimensi.

* **Label Encoding** untuk `Model Name`:
  Setiap model dikodekan menjadi angka unik. Dipilih karena jumlah model sangat banyak dan *One-Hot Encoding* akan membuat dimensi data membengkak.

### Alasan Pemilihan:

* Target Encoding efektif menangkap pengaruh brand terhadap performa.
* Label Encoding efisien dan mencegah *curse of dimensionality* akibat banyaknya kategori model.


```python
# Encoding target untuk kolom 'Company Name' berdasarkan rata-rata skor performa
rata_rata_skor_perusahaan = df.groupby("Company Name")["Performance Score"].mean()
df["Company Name Encoded"] = df["Company Name"].map(rata_rata_skor_perusahaan)

# Buat dictionary mapping untuk encoding dan decoding
mapping_perusahaan = rata_rata_skor_perusahaan.to_dict()
mapping_kebalikan_perusahaan = {nilai: nama for nama, nilai in mapping_perusahaan.items()}

# Label Encoding untuk 'Model Name'
encoder_model = LabelEncoder()
df["Model Name Encoded"] = encoder_model.fit_transform(df["Model Name"])

# Buat dictionary mapping untuk model
mapping_model = dict(zip(df["Model Name"], df["Model Name Encoded"]))
mapping_kebalikan_model = {kode: nama for nama, kode in mapping_model.items()}

# Hapus kolom kategorikal asli
df.drop(columns=["Company Name", "Model Name"], inplace=True)

df.head()
```

```python
df.describe()
```

## Standarization

Langkah terakhir adalah standardisasi untuk menyamakan skala fitur numerik. Proses ini mengubah data agar memiliki rata-rata 0 dan standar deviasi 1 menggunakan Standard Scaler.

Tujuan:

- Menyeimbangkan kontribusi tiap fitur dalam model.
- Menghindari dominasi fitur dengan skala besar yang dapat menurunkan performa model.


```python
# Daftar fitur numerik yang akan dilakukan standardisasi
fitur_numerik = [
    "Mobile Weight (g)", "RAM (GB)", "Front Camera (MP)", "Back Camera (MP)",
    "Battery Capacity (mAh)", "Screen Size (inches)",
    "Launched Price (China/CNY)", "Performance Score", "Launched Year"
]

standarisasi = StandardScaler()
df[fitur_numerik] = standarisasi.fit_transform(df[fitur_numerik])

df.head()
```

```python
df.describe().apply(lambda kolom: kolom.round(4))
```

Setelah proses standardisasi, seluruh fitur numerik memiliki nilai rata-rata (mean) mendekati 0 dan standar deviasi (std) mendekati 1, menandakan bahwa data telah berada dalam skala yang seragam.


# Modelling

Setelah tahap Data Preparation, proses dilanjutkan dengan membangun model machine learning. Dalam sistem rekomendasi ini digunakan pendekatan **Content-Based Filtering**, karena data yang tersedia hanya mencakup informasi spesifikasi dari masing-masing smartphone. Metode yang digunakan untuk membangun sistem rekomendasi adalah **Weighted Sum Model (WSM)**.



```python
# Bobot preferensi berdasarkan jenis penggunaan pengguna
preferensi_bobot = {
    "gaming": {
        "Performance Score": 0.6,
        "RAM (GB)": 0.2,
        "Battery Capacity (mAh)": 0.12,
        "Launched Year": 0.08,
        "Screen Size (inches)": 0.005,
        "Back Camera (MP)": 0.002,
        "Front Camera (MP)": 0.001,
        "Mobile Weight (g)": 0.002
    },
    "fotografi": {
        "Back Camera (MP)": 0.35,
        "Front Camera (MP)": 0.35,
        "RAM (GB)": 0.08,
        "Performance Score": 0.08,
        "Launched Year": 0.10,
        "Screen Size (inches)": 0.03,
        "Battery Capacity (mAh)": 0.02,
        "Mobile Weight (g)": 0.01
    },
    "penggunaan_normal": {
        "Battery Capacity (mAh)": 0.30,
        "Performance Score": 0.28,
        "RAM (GB)": 0.15,
        "Mobile Weight (g)": 0.10,
        "Launched Year": 0.12,
        "Screen Size (inches)": 0.03,
        "Back Camera (MP)": 0.015,
        "Front Camera (MP)": 0.005
    }
}
```

Variabel di atas berisi bobot untuk masing-masing fitur yang akan digunakan dalam model rekomendasi, yaitu Weighted Sum Model, guna menentukan tingkat kepentingan setiap fitur dalam proses rekomendasi.


## Model Weighted Sum Model (WSM)
Weighted Sum Model (WSM) adalah metode yang menggunakan skoring untuk mengurutkan dan memilih alternatif terbaik berdasarkan preferensi pengguna. Dalam konteks sistem rekomendasi smartphone, WSM menghitung skor total setiap smartphone dengan menjumlahkan nilai fitur yang telah dinormalisasi, dikalikan dengan bobot yang ditentukan sesuai preferensi pengguna.

Saat menerapkan WSM dalam rekomendasi smartphone, setiap perangkat mendapatkan Ranking Score berdasarkan bobot fitur yang relevan. Misalnya, untuk pengguna yang fokus pada gaming, perhatian lebih diberikan pada skor kinerja, RAM, dan daya baterai, sementara untuk pengguna yang lebih memperhatikan fotografi, fitur kamera menjadi prioritas. Skor dihitung dengan menjumlahkan hasil perkalian antara bobot preferensi dan nilai fitur masing-masing smartphone. Setelah semua skor dihitung, smartphone diurutkan berdasarkan Ranking Score tertinggi, sehingga menghasilkan daftar rekomendasi terbaik tanpa memerlukan model pembelajaran mesin.


```python
def hitung_skor_wsm(data_ternormalisasi, preferensi_pengguna, harga_maksimal):
    """
    Menghitung skor rekomendasi smartphone menggunakan metode Weighted Sum Model (WSM),
    disesuaikan dengan batas harga dan preferensi pengguna.

    Parameter:
    data_ternormalisasi (DataFrame): Dataset smartphone yang telah distandardisasi menggunakan StandardScaler.
                                     Semua fitur numerik memiliki skala yang setara.

    preferensi_pengguna (str): Tipe preferensi berdasarkan kebutuhan, digunakan untuk menentukan bobot penilaian.
                               Pilihan yang tersedia:
                               - "gaming": Fokus pada performa tinggi, kapasitas baterai besar, dan RAM besar.
                               - "photography": Menitikberatkan pada kualitas kamera dan layar.
                               - "normal usage": Mengedepankan kenyamanan sehari-hari, seperti bobot ringan dan baterai awet.

    harga_maksimal (float): Nilai maksimum harga yang ditentukan oleh pengguna sebagai batas atas.

    Output:
    DataFrame: Daftar smartphone yang memenuhi kriteria harga dan dihitung skornya berdasarkan WSM,
               diurutkan dari nilai tertinggi.
    """

    # Validasi preferensi yang diberikan
    if preferensi_pengguna not in preferensi_bobot:
        raise ValueError("Preferensi tidak dikenali. Pilih salah satu: 'gaming', 'photography', atau 'normal usage'.")

    # Filter berdasarkan harga yang diinginkan
    data_terfilter = data_ternormalisasi[data_ternormalisasi["Launched Price (China/CNY)"] <= harga_maksimal].copy()

    if data_terfilter.empty:
        return "Tidak ditemukan smartphone yang cocok dengan batas harga dan preferensi yang diberikan."

    # Ambil bobot sesuai preferensi
    bobot = preferensi_bobot[preferensi_pengguna]

    # Untuk fitur berat, dibalik nilainya karena makin ringan makin baik
    data_terfilter["Mobile Weight (g)"] = 1 / (data_terfilter["Mobile Weight (g)"] + 1e-9)

    # Hitung skor WSM
    fitur = list(bobot.keys())
    nilai_bobot = list(bobot.values())
    data_terfilter["Skor WSM"] = np.dot(data_terfilter[fitur], nilai_bobot)

    # Urutkan berdasarkan skor tertinggi
    hasil = data_terfilter.sort_values(by="Skor WSM", ascending=False)

    return hasil
```

Fungsi di atas merupakan implementasi dari model Weighted Sum Model (WSM) untuk sistem rekomendasi smartphone. Model ini menghitung skor rekomendasi dengan menjumlahkan nilai fitur yang telah dinormalisasi dan dikalikan dengan bobot sesuai preferensi pengguna, seperti gaming, photography, atau normal usage. Smartphone yang melebihi batas harga maksimal pengguna akan disaring terlebih dahulu, dan fitur berat perangkat dibalik nilainya agar semakin ringan bernilai lebih baik. Hasil akhir berupa daftar smartphone yang sesuai dengan preferensi dan harga pengguna, diurutkan berdasarkan skor tertinggi.


## Result Model Weighted Sum Model (WSM)


```python
numerical_features = [
    "Mobile Weight (g)", "RAM (GB)", "Front Camera (MP)", "Back Camera (MP)",
    "Battery Capacity (mAh)", "Screen Size (inches)", "Launched Price (China/CNY)",
    "Performance Score", "Launched Year"
]

# Buat Company Mapping dan Model Mapping
company_mapping = {name: idx for idx, name in enumerate(df_original["Company Name"].unique())}
model_mapping = {name: idx for idx, name in enumerate(df_original["Model Name"].unique())}

# Reverse mapping untuk decode
reverse_company_mapping = {v: k for k, v in company_mapping.items()}
reverse_model_mapping = {v: k for k, v in model_mapping.items()}

boxcox_lambdas = {"Launched Price (China/CNY)": 0.5}

# Fit scaler ke data numerik
scaler = StandardScaler()
scaler.fit(df[numerical_features])

def calculate_wsm(df, preference, max_price):
    weights = {
        "Performance Score": 0.4,
        "Battery Capacity (mAh)": 0.2,
        "Screen Size (inches)": 0.1,
        "RAM (GB)": 0.2,
        "Launched Price (China/CNY)": 0.1,
    }

    # Filter harga
    df_filtered = df[df["Launched Price (China/CNY)"] <= max_price].copy()

    # Hitung skor WSM
    df_filtered["WSM Score"] = sum(df_filtered[feature] * weight for feature, weight in weights.items())

    return df_filtered.sort_values("WSM Score", ascending=False)

user_preference = "gaming"
max_price = 2500

# Transformasi Box-Cox untuk harga
max_price_transformed = boxcox([max_price], boxcox_lambdas["Launched Price (China/CNY)"])[0]

# Dummy array untuk transformasi harga
dummy_array = np.zeros((1, len(numerical_features)))
price_index = numerical_features.index("Launched Price (China/CNY)")
dummy_array[0, price_index] = max_price_transformed

# Standarisasi harga
max_price_standardized = scaler.transform(dummy_array)[0, price_index]

# Pastikan df dan df_original memiliki index yang sejajar
df["Company Name"] = df_original["Company Name"]
df["Model Name"] = df_original["Model Name"]

# Buat encoded column
df["Company Name Encoded"] = df["Company Name"].map(company_mapping)
df["Model Name Encoded"] = df["Model Name"].map(model_mapping)

# Hitung rekomendasi WSM
df_recommendation = calculate_wsm(df, user_preference, max_price_standardized)

# Decode nama perusahaan dan model
df_recommendation["Company Name"] = df_recommendation["Company Name Encoded"].map(reverse_company_mapping)
df_recommendation["Model Name"] = df_recommendation["Model Name Encoded"].map(reverse_model_mapping)

columns_order = ["Company Name", "Model Name"] + [
    col for col in df_recommendation.columns if col not in ["Company Name", "Model Name"]
]
df_recommendation = df_recommendation[columns_order]

# Hapus encoded columns
df_recommendation = df_recommendation.drop(columns=["Company Name Encoded", "Model Name Encoded"])

# Ambil kolom numerik asli dari df_original berdasarkan Company dan Model Name
df_recommendation = df_recommendation.merge(
    df_original[["Company Name", "Model Name"] + numerical_features],
    on=["Company Name", "Model Name"],
    suffixes=("", "_original")
)

for col in numerical_features:
    df_recommendation[col] = df_recommendation[f"{col}_original"]
    df_recommendation.drop(columns=[f"{col}_original"], inplace=True)

df_recommendation.head(10)
```

Tabel di atas menunjukkan rekomendasi 10 smartphone terbaik untuk pengguna yang fokus pada gaming dengan batas harga maksimum 2500 CNY. Setiap smartphone diurutkan berdasarkan Ranking Score yang dihitung menggunakan Weighted Sum Model (WSM), mempertimbangkan fitur penting seperti kinerja, kapasitas baterai, dan kualitas kamera.


## **Evaluation**

Setelah proses pemodelan menggunakan pendekatan **Weighted Sum Model (WSM)**, tahap evaluasi dilakukan untuk mengetahui seberapa baik sistem dalam memberikan rekomendasi produk yang sesuai dengan preferensi pengguna, dalam hal ini adalah **smartphone untuk kebutuhan gaming**.

Evaluasi dilakukan menggunakan metrik **Precision**, yang mengukur persentase rekomendasi yang benar-benar sesuai dengan kriteria yang telah ditentukan pengguna. Kriteria relevansi untuk preferensi **gaming** ditentukan sebagai berikut:

* **RAM ≥ 12 GB**
* **Performance Score ≥ 400.000**

Berikut ini adalah hasil analisis relevansi dari 10 rekomendasi teratas oleh model WSM:

| No | Model Name           | RAM (GB) | Performance Score | WSM Score | Relevan (Gaming) |
| -- | -------------------- | -------- | ----------------- | --------- | ---------------- |
| 0  | Galaxy Tab S9 Ultra  | 12.0     | 991506.0          | 2.627545  | ✅                |
| 1  | OnePlus Pad Pro      | 12.0     | 1272265.0         | 2.586813  | ✅                |
| 2  | Pad 3 Pro 512GB      | 16.0     | 1272265.0         | 2.566047  | ✅                |
| 3  | Pad GT Pro           | 12.0     | 1272265.0         | 2.541765  | ✅                |
| 4  | MagicPad 3           | 12.0     | 1272265.0         | 2.467811  | ✅                |
| 5  | MagicPad 2           | 16.0     | 1272265.0         | 2.444959  | ✅                |
| 6  | Galaxy Tab S8 Ultra  | 12.0     | 991506.0          | 2.313310  | ✅                |
| 7  | Pad 3 Pro 256GB      | 12.0     | 1272265.0         | 2.300863  | ✅                |
| 8  | Galaxy Tab S9+ 256GB | 12.0     | 991506.0          | 2.244627  | ✅                |
| 9  | X200 Pro 512GB       | 16.0     | 1701249.0         | 2.177002  | ✅                |

**Jumlah relevan: 10 dari 10 rekomendasi**
 **Precision = 10 / 10 = 100%**

## **Kesimpulan**

* Model **WSM berhasil mencapai tingkat presisi 100%** dalam memberikan rekomendasi untuk preferensi gaming, berdasarkan dua kriteria utama: kapasitas RAM dan skor performa.
* Seluruh 10 produk yang direkomendasikan memiliki RAM minimal 12 GB dan skor performa jauh di atas ambang batas 400.000, menunjukkan bahwa sistem secara efektif mampu menyaring produk-produk dengan spesifikasi tinggi.
* Skor WSM juga menunjukkan peringkat produk secara berurutan, di mana produk dengan kombinasi fitur unggulan memiliki skor lebih tinggi. Ini berarti sistem tidak hanya memilih produk yang relevan, tetapi juga mengurutkannya secara optimal berdasarkan kualitas fitur.
* Tidak ada produk yang masuk daftar tetapi gagal memenuhi syarat spesifikasi, yang menandakan **akurasi tinggi dan minim kesalahan dalam pemfilteran.**


## **Conclusion**

Evaluasi model **Weighted Sum Model (WSM)** menunjukkan bahwa pendekatan ini **sangat efektif** untuk membangun sistem rekomendasi berbasis spesifikasi teknis. Dengan Precision mencapai 100%, sistem menunjukkan performa yang **sangat baik** dalam memahami dan menerjemahkan preferensi pengguna terhadap perangkat gaming.

### Pencapaian dari sisi **Business Understanding**:

1. Fitur utama seperti RAM dan skor performa berhasil diidentifikasi sebagai kriteria paling penting untuk kebutuhan gaming.
2. Pengolahan data seperti normalisasi dan transformasi (misalnya Box-Cox) mendukung pemodelan yang akurat dan stabil.
3. Sistem rekomendasi berbasis fitur telah berhasil dibangun dan menunjukkan hasil yang relevan dengan kebutuhan pengguna.

### Pencapaian dari sisi **Solution Goals**:

1. Proses ekstraksi dan seleksi fitur dilakukan dengan baik sehingga hanya fitur penting yang digunakan dalam pemodelan.
2. Model WSM berhasil diimplementasikan secara efektif untuk menghasilkan rekomendasi yang presisi.
3. Evaluasi metrik Precision menegaskan bahwa sistem tidak hanya akurat secara teknis, tetapi juga relevan secara praktis.

### Dampak dari **Solution Statement**:

1. Tahap preprocessing seperti pembersihan dan transformasi data memberikan kontribusi besar terhadap keberhasilan model.
2. Pemilihan WSM memungkinkan pemeringkatan produk berdasarkan bobot fitur yang disesuaikan dengan preferensi pengguna.
3. Evaluasi berbasis relevansi memberikan jaminan bahwa sistem tidak hanya mengurutkan, tapi juga menyesuaikan dengan kebutuhan pengguna secara aktual.


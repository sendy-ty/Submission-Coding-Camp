
# Laporan Proyek Machine Learning - Sandy Tirta Yudha

## Domain Proyek

Meningkatkan efektivitas latihan di pusat kebugaran telah menjadi perhatian utama dalam mendukung kesehatan masyarakat masa kini, khususnya terkait efisiensi dalam membakar kalori. Memahami secara mendalam jenis-jenis aktivitas yang mampu membakar kalori secara optimal tidak hanya penting bagi individu yang ingin mencapai target kebugaran pribadi, tetapi juga berdampak besar pada kesehatan populasi secara umum. Berdasarkan data dari World Health Organization (WHO, 2020), aktivitas fisik yang cukup berperan penting dalam menurunkan risiko berbagai penyakit kronis. Sayangnya, sebagian besar penduduk dunia masih belum mencapai standar aktivitas fisik yang dianjurkan. Terbatasnya waktu dalam kehidupan modern memperumit situasi ini, sehingga diperlukan pemahaman yang lebih komprehensif mengenai efektivitas berbagai jenis latihan dalam mengoptimalkan pembakaran kalori dalam durasi yang terbatas.

Gough et al. (2018) menemukan bahwa masyarakat kini semakin cenderung memilih program latihan yang mampu memberikan hasil maksimal dengan durasi yang lebih singkat. Pergeseran ini mencerminkan kebutuhan akan efisiensi dalam berolahraga, terutama di tengah keterbatasan waktu yang dihadapi banyak orang di era modern. Oleh karena itu, penting untuk mengetahui jenis latihan yang paling efektif dalam membakar kalori dalam waktu yang terbatas. Selain faktor efisiensi, aspek psikososial juga berperan penting dalam keberhasilan program kebugaran. McAuley et al. (2011) menyoroti bahwa motivasi, rasa percaya diri, dan dukungan sosial berkontribusi besar terhadap seberapa intens dan konsisten seseorang menjalani latihan. Dengan demikian, efektivitas latihan tidak hanya ditentukan oleh faktor fisik semata, tetapi juga oleh kondisi mental dan sosial yang menyertainya.

Dalam skala kesehatan masyarakat secara keseluruhan, memahami seberapa efektif berbagai jenis latihan gym dalam membakar kalori memiliki peran strategis dalam merancang intervensi kesehatan yang lebih tepat sasaran. Hal ini menjadi semakin penting seiring dengan meningkatnya kasus penyakit akibat gaya hidup pasif, seperti obesitas, diabetes tipe 2, dan gangguan jantung. Dengan memanfaatkan wawasan mengenai efektivitas tiap jenis latihan, program kebugaran dapat disusun secara lebih optimal guna menyesuaikan dengan keterbatasan waktu dan sumber daya yang sering dihadapi oleh masyarakat saat ini. Oleh karena itu, penelitian yang mendalami efisiensi pembakaran kalori dalam aktivitas kebugaran bukan hanya berguna untuk meningkatkan hasil latihan individu, tetapi juga berkontribusi dalam mendukung kebijakan kesehatan publik yang bertujuan menurunkan prevalensi penyakit kronis.

Pemanfaatan algoritma machine learning memungkinkan analisis dan identifikasi aktivitas gym yang paling efisien dalam mendukung tujuan kebugaran. Beberapa algoritma yang digunakan antara lain k-Nearest Neighbors (KNN), Random Forest, dan Boosting. Algoritma KNN mampu memberikan saran jenis latihan yang sesuai dengan profil dan karakteristik masing-masing individu. Sementara itu, Random Forest memproses berbagai variabel untuk menghasilkan prediksi yang lebih akurat terkait jumlah kalori yang terbakar. Di sisi lain, Boosting terus menyempurnakan hasil prediksi dengan mempelajari pola kesalahan sebelumnya, sehingga meningkatkan akurasi model secara keseluruhan. Melalui pendekatan ini, pusat kebugaran dapat menyediakan rekomendasi latihan yang bersifat personal, membantu individu mencapai target kebugaran mereka secara lebih efektif, serta mendorong gaya hidup sehat secara luas dalam masyarakat. Data yang digunakan diambil dari kaggle yang bisa diakses dari link [berikut](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data).

Dataset ini menyediakan informasi menyeluruh mengenai kondisi fisik individu yang berlatih di pusat kebugaran. Data mencakup elemen demografis seperti `usia` dan `jenis_kelamin`, serta indikator komposisi tubuh seperti `berat_badan`, `tinggi_badan`, `BMI`, dan `persentase_lemak`. Selain itu, terdapat juga metrik kebugaran jantung seperti `Max_BPM`, `Avg_BPM`, dan `esting_BPM`. Nilai `BMI` dan `persentase_lemak` digunakan untuk mengidentifikasi komposisi tubuh, di mana `persentase_lemak` dianggap lebih akurat dalam menilai kadar lemak tubuh, khususnya pada individu dengan otot yang dominan.

Variabel lain yang disertakan adalah kebiasaan latihan, meliputi `Jenis_Olahraga`, `Durasi_Sesi`, `Kalori_Terbakar`, dan `Frekuensi_Olahraga`, yang menggambarkan pola dan intensitas aktivitas fisik. Aktivitas seperti HIIT atau kardio, yang termasuk latihan intensitas tinggi, umumnya menghasilkan `Avg_BPM` yang lebih tinggi dan membakar lebih banyak kalori dibandingkan dengan latihan ringan seperti yoga. Penambahan fitur seperti `Asupan_Air` dan `Tingkat_Pengalaman` memberikan konteks tambahan mengenai kebiasaan hidrasi dan tingkat familiaritas peserta terhadap latihan, yang turut memengaruhi performa dan detak jantung saat istirahat. Informasi yang lengkap ini membuka peluang untuk menyusun program kebugaran yang lebih personal dan sesuai kebutuhan masing-masing individu.



# Business Understanding



## Problem Statement


1. Bagaimana strategi yang tepat untuk memaksimalkan jumlah kalori yang terbakar selama sesi latihan fisik?

2. Apa langkah-langkah yang dapat dilakukan untuk mengatur pola latihan agar selaras dengan tujuan penurunan kadar lemak tubuh yang diinginkan?

3. Apakah terdapat perbedaan kecenderungan dalam memilih jenis latihan antara pria dan wanita?

4. Sejauh mana tingkat keahlian atau pengalaman seseorang dalam berolahraga memengaruhi pilihan latihan yang mereka lakukan?


## Goals



1. Mengembangkan model prediktif untuk memperkirakan jumlah kalori yang dibakar selama aktivitas latihan.

2. Membangun sistem prediksi untuk memperkirakan kadar lemak tubuh berdasarkan data latihan dan faktor terkait.

3. Mengidentifikasi perbedaan kecenderungan latihan antara jenis kelamin pria dan wanita.

4. Menganalisis preferensi jenis latihan berdasarkan tingkat kemahiran atau pengalaman individu.


## Solution



1. Menerapkan empat algoritma machine learning untuk membangun model prediktif dalam mengestimasi kalori yang terbakar serta kadar lemak tubuh.

2. Melakukan eksplorasi data (EDA) guna menganalisis sejauh mana faktor jenis kelamin dan tingkat keahlian memengaruhi pilihan dalam aktivitas latihan.


# Impor Library


Mengimpor Library yang dibutuhkan


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
import shutil
import os
from google.colab import drive
from sklearn.feature_selection import SelectFromModel
from sklearn.datasets import make_regression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, mean_absolute_error, mean_squared_error, r2_score, explained_variance_score, roc_auc_score, precision_recall_curve
import kagglehub
import warnings
warnings.filterwarnings('ignore')
from sklearn.inspection import permutation_importance
from sklearn.model_selection import validation_curve
```

# Data Understanding


Memahami dan mengidentifikasi karakteristik data


### Data Loading


Dataset diambil dari platform kaggle pada tautan berikut https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data


```python
drive.mount('/content/drive')
csv_file_path = '/content/drive/My Drive/ML Terapan/Predictive/gym_members_exercise_tracking.csv'
```

Data dipindahkan ke dalam drive untuk membuatnya lebih mudah digunakan.


```python
file_sumber = '/content/drive/My Drive/ML Terapan/Predictive/gym_members_exercise_tracking.csv'
folder_tujuan = '/content/Predictive'
os.makedirs(folder_tujuan, exist_ok=True)
file_tujuan = os.path.join(folder_tujuan, 'gym_members_exercise_tracking.csv')
shutil.copy(file_sumber, file_tujuan)
print(f"File berhasil disalin ke: {file_tujuan}")
```

```python
csv_file_path = file_tujuan
df = pd.read_csv(csv_file_path)
print("Dataset dimuat dengan shape:", df.shape)
```

Dengan menggunakan fungsi .head() dan .shape, data dibuka melalui dataframe dan ditampilkan data head nya.


```python
data = pd.read_csv("/content/Predictive/gym_members_exercise_tracking.csv")
print(data.shape)
data.head()
```

973 rekod data terdiri dari 15 jenis informasi yang dapat dianalisis.


## Exploratory Data Analysis (EDA)



### Deskripsi Variabel


#### Arti Variabel


Berikut ini adalah arti dari setiap variabel yang akan digunakan.


| Variabel                           | Keterangan |
|-------------------------------------|-------------------|
| Age                                  | 	Usia pengguna pusat kebugaran yang dinyatakan dalam tahun.|
| Gender                               |Kategori jenis kelamin dari pengunjung (Laki-laki atau Perempuan).|
| Weight (kg)                          | Berat badan pengunjung pusat kebugaran dalam Kilogram |
| Height (m)                           |Tinggi badan peserta pusat kebugaran, dinyatakan dalam sentimeter.|
| Max_BPM                              | Detak jantung maksimum per menit yang dicapai oleh pengguna.|
| Avg_BPM                              |Rata-rata detak jantung per menit selama aktivitas.|
| Resting_BPM                          | 	Detak jantung per menit saat pengguna dalam kondisi istirahat.|
| Session_Duration (hours)            | Lama waktu penggunaan fasilitas kebugaran dalam jam.|
| Calories_Burned                      | Total kalori yang dibakar selama sesi latihan, diukur dalam satuan kalori.|
| Workout_Type                         | Jenis aktivitas latihan yang dilakukan (HIIT, Strength, Cardio, atau Yoga).|
| Fat_Percentage                       | Persentase kadar lemak tubuh dari peserta pusat kebugaran(%) |
| Water_Intake (liters)               | Volume konsumsi air selama sesi latihan, diukur dalam liter.|
| Workout_Frequency (days/week)       | 	Jumlah hari latihan atau kunjungan ke gym dalam satu minggu.|
| Experience_Level                     | Tingkat kemahiran dalam melakukan latihan dalam tiga tingkatan (1, 2, 3) |
| BMI                                  | Nilai indeks massa tubuh (IMT) dari pengguna pusat kebugaran.|



Nilai variabel dibahas lebih lanjut dibawah ini, sebagian besar variabel dalah variabel numerik


Nilai variabel `Workout_Type` yang berarti Jenis Latihan, dijelaskan sebagai berikut :

| Variabel                           | Keterangan |
|-------------------------------------|-------------------|
| HIIT| High-Intensity Interval Training merupakan jenis latihan berdurasi singkat namun intens, yang diselingi waktu istirahat dan variasi gerakan secara cepat.|
| Strength| Latihan fisik yang difokuskan untuk meningkatkan kekuatan otot, biasanya melalui aktivitas seperti mengangkat beban atau melakukan bench press bench-press |
| Yoga| 	Latihan yang memadukan postur tubuh, teknik pernapasan, serta meditasi untuk menunjang kesehatan fisik dan keseimbangan mental.|
|Cardio|	Aktivitas yang berfungsi untuk menaikkan detak jantung dan mempercepat pernapasan, mencakup latihan seperti berlari, bersepeda, atau menggunakan treadmill dengan tingkat intensitas bervariasi.|




#### Tipe Variabel


```python
data.info()
```

Terdapat enam variabel dengan tipe data int64, dua variabel bertipe object, dan tujuh variabel bertipe float64. Variabel dengan tipe float64 seluruhnya termasuk dalam kategori numerik, sedangkan variabel bertipe object diklasifikasikan sebagai variabel kategorikal. Untuk tipe int64, dua variabel dapat dikategorikan sebagai data kategorikal, sementara empat lainnya merupakan variabel numerik.


#### Data Describe


```python
data.describe()
```

Data statistik tersebut memperlihatkan nilai simpangan baku yang relatif besar, yang mengindikasikan adanya variasi yang cukup mencolok antara satu responden dengan yang lainnya. Keberagaman ini dapat mencerminkan cakupan demografis yang luas dalam dataset, sehingga memungkinkan dilakukannya analisis terhadap berbagai karakteristik responden.


#### Data Cleaning




```python
pd.DataFrame({'Jumlah Missing Value': data.isna().sum()})
```

Tidak ditemukan adanya data yang kosong.


```python
data[data.duplicated()].shape[0]
```

Tidak ditemukan adanya duplikat/ganda.


#### Outlier


Boxplot digunakan untuk menampilkan sebaran data secara visual.


```python
fitur_numerik = [
    "Age", "Weight (kg)", "Height (m)", "Max_BPM", "Avg_BPM", "Resting_BPM",
    "Session_Duration (hours)", "Calories_Burned", "Fat_Percentage",
    "Water_Intake (liters)", "Workout_Frequency (days/week)",
    "Experience_Level", "BMI"
]

plt.figure(figsize=(24, 18))

for idx, fitur in enumerate(fitur_numerik):
    plt.subplot(7, 2, idx + 1)
    sns.histplot(data=data, x=fitur, kde=True, color='mediumblue', bins=30)
    mean_val = data[fitur].mean()
    median_val = data[fitur].median()

    plt.axvline(mean_val, color='red', linestyle='--', label=f'Rata-rata: {mean_val:.2f}')
    plt.axvline(median_val, color='green', linestyle='--', label=f'Median: {median_val:.2f}')

    plt.title(f'Distribusi {fitur}', fontsize=12, fontweight='bold')
    plt.xlabel(fitur, fontsize=10)
    plt.ylabel('Frekuensi', fontsize=10)
    plt.legend()
    plt.tight_layout()

plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()
```

![Output 0](images/output_0.png)

Tampilan grafik menunjukkan bahwa terdapat beberapa datum yang berada di luar batas kuartil pada beberapa fitur, seperti pada distribusi berat badan dan BMI. Meskipun demikian, data-data tersebut masih dapat dianggap wajar dalam konteks pusat kebugaran. Hal ini dikarenakan pusat kebugaran merupakan tempat yang mengakomodasi berbagai program, termasuk program penurunan berat badan. Oleh karena itu, memiliki berat badan yang tinggi bukan merupakan anomali. Demikian pula, data kalori terbakar juga memiliki beberapa datum yang berada di luar kuartil atas. Namun, ini tidak serta merta menjadi pencilan yang harus dihilangkan. Hal ini dikarenakan sangat memungkinkan bagi seseorang yang mahir dalam latihan kebugaran untuk membakar kalori dalam jumlah yang lebih besar dalam satu kali sesi latihan. Selain itu, beberapa faktor seperti jenis latihan, durasi sesi, dan tingkat keahlian dapat mempengaruhi jumlah kalori yang terbakar. Dalam hal ini, data tersebut masih relevan dan dapat memberikan wawasan yang berharga tentang pola latihan dan pencapaian tujuan kebugaran bagi anggota pusat kebugaran.


#### Koreksi tipe data


Dua kolom informasi bertipe int64 dapat diperlakukan sebagai data kategorik. Oleh karena itu dibuatlah kolom baru mengunakan data tersebut dengan mengubah jenis data menjadi string. Selanjutnya string tersebut diubah menjadi tipe data object agar bisa dikenali filter tipe object seperti data kategorik lainnya.


```python
data['Workout_Frequency_cat'] = data['Workout_Frequency (days/week)'].apply(lambda x: str(x))
data['Experience_Level_cat'] = data['Experience_Level'].apply(lambda x: str(x))

data['Workout_Frequency_cat'] = data['Workout_Frequency_cat'].astype("object")
data['Experience_Level_cat'] = data['Experience_Level_cat'].astype("object")
```

### Analisis Univariat


```python
fitur_numerik = ['Age',
                 'Weight (kg)',
                 'Height (m)',
                 'Max_BPM',
                 'Avg_BPM',
                 'Resting_BPM',
                 'Session_Duration (hours)',
                 'Calories_Burned',
                 'Fat_Percentage',
                 'Water_Intake (liters)',
                 'Workout_Frequency (days/week)',
                 'Experience_Level',
                 'BMI']

fitur_kategorik = ['Gender', 'Workout_Type', 'Workout_Frequency_cat', 'Experience_Level_cat']
print("Daftar fitur numerik:", fitur_numerik)
print("Daftar fitur kategorikal:", fitur_kategorik)
```

```python
fitur_kategorikal = ['Gender', 'Workout_Type', 'Workout_Frequency_cat', 'Experience_Level_cat']
total_unik = data[fitur_kategorikal].nunique()
nilai_kategorikal = data[fitur_kategorikal].apply(lambda x: x.unique())
pd.DataFrame({"Jumlah Nilai Unik": total_unik, "Nilai yang Tersedia": nilai_kategorikal})
```

Ada 4 variabel kategorik yang bisa digunakan untuk mengelompokkan data.


```python
tipe_olahraga = data['Workout_Type'].value_counts()
tipe_olahraga
```

```python
label = tipe_olahraga.index.tolist()
size = tipe_olahraga.values.tolist()
plt.figure(figsize=(8, 6))
sns.barplot(x=size, y=label, palette='viridis')
plt.xlabel('Persentase')
plt.ylabel('Tipe Olahraga')
plt.title('Distribusi Tipe Olahraga')
for i, v in enumerate(size):
    plt.text(v + 0.5, i, f'{v:.1f}%', va='center')

plt.show()
```

![Output 1](images/output_1.png)

Penyebaran jumlah pelanggan berdasarkan jenis latihan terlihat cukup seimbang, dengan latihan Strength menjadi yang paling populer, meskipun selisihnya tidak terlalu signifikan dibandingkan jenis latihan lain.


```python
data['Workout_Frequency_cat'] = data['Workout_Frequency_cat'].astype('category')
data['Experience_Level_cat'] = data['Experience_Level_cat'].astype('category')

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

fitur_kategorikal = ["Gender", "Workout_Type", "Workout_Frequency_cat", "Experience_Level_cat"]
deskripsi_fitur = ["Jenis Kelamin", "Jenis Latihan", "Frekuensi Latihan", "Tingkat Kemahiran"]

for i, fitur in enumerate(fitur_kategorikal):
    count_data = data[fitur].value_counts().sort_index()
    x = count_data.index
    y = count_data.values

    axes[i].barh(x, y, color=['steelblue', 'darkorange', 'forestgreen', 'firebrick'])

    judul = "\n".join(textwrap.wrap(f"Jumlah Data {deskripsi_fitur[i]}", width=40))
    axes[i].set_title(judul, size=12)
    axes[i].set_xlabel("Jumlah")

    for idx, value in enumerate(y):
        axes[i].text(value + 5, idx, str(value), va='center')

plt.tight_layout()
plt.show()
```

![Output 2](images/output_2.png)

Pada pusat kebugaran, jumlah pengunjung laki-laki sedikit lebih banyak dibandingkan perempuan, namun perbedaan jumlahnya tidak signifikan. Sebagian besar pengunjung datang untuk berolahraga sebanyak tiga kali seminggu. Menariknya, sebagian besar anggota memiliki tingkat keahlian yang rendah hingga sedang, di mana tingkat keahlian tertinggi mempunyai jumlah anggota paling sedikit. Hal ini menunjukkan bahwa pusat kebugaran ini melayani berbagai kalangan dengan tingkat keahlian yang berbeda-beda.


```python
fig, axes = plt.subplots(3, 5, figsize=(15, 9))
axes = axes.flatten()

labels = ["Tahun", "Kilogram", "Meter", "Detak Menit", "Detak Menit", "Detak Menit",
          "Jam", "Kalori", "Persen", "Liter", "Hari/Minggu", "Tingkat", ""]

fitur_numerik = ['Age', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM', 'Resting_BPM',
                 'Session_Duration (hours)', 'Calories_Burned', 'Fat_Percentage',
                 'Water_Intake (liters)', 'Workout_Frequency (days/week)',
                 'Experience_Level', 'BMI']
deskripsi_fitur = ['Usia', 'Berat Badan', 'Tinggi Badan', 'Maks BPM', 'Rata-rata BPM', 'Istirahat BPM',
                   'Sesi Durasi', 'Kalori Terbakar', 'Persentase Lemak', 'Asupan Air',
                   'Frekuensi Latihan', 'Tingkat Pengalaman', 'BMI']

for i, fitur in enumerate(fitur_numerik):
    if i < len(axes):
        colors = ['skyblue', 'lightgreen', 'lightcoral', 'mediumpurple', 'lightyellow',
                  'lightpink', 'lightgoldenrodyellow', 'lightcyan', 'wheat', 'powderblue']
        color = colors[i % len(colors)]

        sns.histplot(data=data, x=fitur, kde=True, ax=axes[i], color=color)

        judul = "\n".join(textwrap.wrap(f"Histogram {deskripsi_fitur[i]}", width=30))
        axes[i].set_title(judul, fontsize=10, pad=10)
        axes[i].set_xlabel(labels[i], fontsize=8)
        axes[i].set_ylabel("Frekuensi", fontsize=8)

        axes[i].tick_params(axis='both', which='major', labelsize=7)
        axes[i].grid(True, linestyle='--', alpha=0.7)

for j in range(i+1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()
```

![Output 3](images/output_3.png)

Variabel `Durasi Latihan` dan `Kalori Terbakar` memperlihatkan distribusi data yang cukup simetris dan normal. Variabel seperti `Berat Badan`, `Tinggi Badan`, dan `BMI` menunjukkan distribusi miring ke kanan (positif), yang menandakan bahwa mayoritas anggota memiliki nilai di bawah rata-rata. Sebaliknya, variabel `Kadar Lemak Tubuh` dan `Asupan Air` menunjukkan distribusi miring ke kiri (negatif), yang berarti kebanyakan anggota memiliki nilai di atas rata-rata. Sementara itu, variabel `Usia`, `Max BPM`, `Resting BPM`, `Avg BPM`, `Frekuensi Latihan`, dan `Tingkat Kemahiran` tidak menunjukkan distribusi normal. Usia dan BPM (maksimal, rata-rata, dan istirahat) menunjukkan distribusi bimodal atau pola yang tidak teratur. Frekuensi latihan dan tingkat kemahiran juga menunjukkan distribusi tidak normal. Berdasarkan visualisasi plot, terdapat variasi dan pola yang berbeda untuk setiap variabel, yang mungkin memerlukan pendekatan analisis yang berbeda untuk setiap variabel.


### Analisis Multivariat


#### 1. Analisis Berbagai Distribusi Kategori Berdasarkan Jenis Kelamin


```python
# Mengatur ukuran keseluruhan untuk semua subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
fig.suptitle("Analisis Distribusi Kategori Berdasarkan Jenis Kelamin")

# Membuat subset data untuk setiap jenis kelamin
data_male = data.query("Gender == 'Male'")
data_female = data.query("Gender == 'Female'")

# Subplot untuk Tingkat Kemahiran
sns.barplot(x="Experience_Level_cat", y="Experience_Level", data=data_male, ax=axes[0, 0], palette="Blues")
axes[0, 0].set_title("Tingkat Kemahiran: Laki-laki")
axes[0, 0].set_xlabel("Tingkat Kemahiran")
axes[0, 0].set_ylabel("Rata-rata Tingkat")
axes[0, 0].tick_params(axis='x')

sns.barplot(x="Experience_Level_cat", y="Experience_Level", data=data_female, ax=axes[0, 1], palette="Oranges")
axes[0, 1].set_title("Tingkat Kemahiran: Perempuan")
axes[0, 1].set_xlabel("Tingkat Kemahiran")
axes[0, 1].set_ylabel("Rata-rata Tingkat")
axes[0, 1].tick_params(axis='x')

# Subplot untuk Frekuensi Latihan
sns.boxplot(x="Workout_Frequency_cat", y="Workout_Frequency (days/week)", data=data_male, ax=axes[0, 2], palette="Blues")
axes[0, 2].set_title("Frekuensi Latihan: Laki-laki")
axes[0, 2].set_xlabel("Frekuensi per minggu")
axes[0, 2].set_ylabel("Frekuensi")
axes[0, 2].tick_params(axis='x')

sns.boxplot(x="Workout_Frequency_cat", y="Workout_Frequency (days/week)", data=data_female, ax=axes[1, 2], palette="Oranges")
axes[1, 2].set_title("Frekuensi Latihan: Perempuan")
axes[1, 2].set_xlabel("Frekuensi per minggu")
axes[1, 2].set_ylabel("Frekuensi")
axes[1, 2].tick_params(axis='x')

# Subplot untuk Tipe Latihan
workout_type_order = sorted(data['Workout_Type'].unique())
male_workout_counts = data_male['Workout_Type'].value_counts().reindex(workout_type_order)
female_workout_counts = data_female['Workout_Type'].value_counts().reindex(workout_type_order)

male_female_workout = pd.DataFrame({'Laki-laki': male_workout_counts, 'Perempuan': female_workout_counts}).reset_index()
male_female_workout.columns = ['Workout_Type', 'Laki-laki', 'Perempuan']

male_female_workout.melt(id_vars=['Workout_Type'], value_vars=['Laki-laki', 'Perempuan'],
                         var_name='Gender', value_name='Count')

sns.barplot(x="Workout_Type", y="Count", hue="Gender", data=male_female_workout.melt(id_vars=['Workout_Type'],
                                                                                   value_vars=['Laki-laki', 'Perempuan'],
                                                                                   var_name='Gender',
                                                                                   value_name='Count'),
            ax=axes[1, 0], palette=['#1f77b4', '#ff7f0e'])
axes[1, 0].set_title("Tipe Latihan Berdasarkan Jenis Kelamin")
axes[1, 0].set_xlabel("Jenis Latihan")
axes[1, 0].set_ylabel("Jumlah")
axes[1, 0].tick_params(axis='x', rotation=45)

# Subplot untuk Tingkat Kemahiran Berdasarkan Usia
sns.pointplot(x="Experience_Level_cat", y="Age", data=data_male, ax=axes[1, 1], palette="Blues", markers="o")
axes[1, 1].set_title("Tingkat Kemahiran vs Usia: Laki-laki")
axes[1, 1].set_xlabel("Tingkat Kemahiran")
axes[1, 1].set_ylabel("Rata-rata Usia")
axes[1, 1].tick_params(axis='x')

sns.pointplot(x="Experience_Level_cat", y="Age", data=data_female, ax=axes[1, 1], palette="Oranges", markers="s")
axes[1, 1].legend(['Laki-laki', 'Perempuan'])

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
```

![Output 4](images/output_4.png)

Analisis distribusi kategori berdasarkan jenis kelamin menunjukkan bahwa laki-laki dan perempuan memiliki pola yang serupa dalam tingkat kemahiran dan frekuensi latihan. Kebanyakan anggota berada pada tingkat kemahiran rendah dan cenderung berlatih 3-4 kali seminggu. Perbedaan terlihat pada preferensi jenis latihan, di mana perempuan lebih memilih `Kardio` dan `Yoga`, sedangkan laki-laki tersebar merata di antara `Kardio`, `HIIT`, dan `Strength`. Laki-laki juga lebih banyak memilih `Yoga`. Selain itu, laki-laki dengan tingkat kemahiran tinggi cenderung lebih muda.


#### 2. Distribusi Jenis Latihan Berdasarkan Level Kemahiran


```python
# Kelompokkan berdasarkan Experience_Level dan Workout_Type, lalu dapatkan jumlahnya
workout_counts = data.groupby(['Experience_Level', 'Workout_Type'], observed=False).size().unstack(fill_value=0)

# Normalisasi untuk mendapatkan persentase
workout_percentages = workout_counts.div(workout_counts.sum(axis=1), axis=0) * 100
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

workout_counts.plot(kind='barh', stacked=True, ax=axes[0], colormap='viridis')
axes[0].set_title("Distribusi Jenis Latihan Berdasarkan Tingkat Kemahiran")
axes[0].set_xlabel("Jumlah")
axes[0].set_ylabel("Tingkat Kemahiran")
axes[0].legend(title='Jenis Latihan', bbox_to_anchor=(1.05, 1), loc='upper left')

workout_percentages.plot(kind='barh', stacked=True, ax=axes[1], colormap='viridis')
axes[1].set_title("Distribusi Jenis Latihan Berdasarkan Tingkat Kemahiran (%)")
axes[1].set_xlabel("Persentase (%)")
axes[1].set_ylabel("Tingkat Kemahiran")
axes[1].legend(title='Jenis Latihan', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
```

![Output 5](images/output_5.png)

`Tingkat Kemahiran` tidak secara signifikan memengaruhi preferensi jenis latihan, karena distribusi persentase jenis latihan pada setiap tingkat kemahiran relatif serupa. Baik pada `Tingkat Kemahiran` 1, 2, maupun 3, jumlah peserta untuk setiap jenis latihan (`Cardio`, `HIIT`, `Strength`, dan `Yoga`) tetap konsisten. Meskipun demikian, terdapat sedikit variasi di mana pada Tingkat Kemahiran 1 dan 2, jenis latihan Strength lebih populer, sedangkan pada `Tingkat Kemahiran` 3, `Yoga` memiliki jumlah peserta yang lebih banyak.


#### 3. Distribusi Nilai Kadar Lemak Tubuh dari berbagai Kategori




```python
# Membuat plot dengan tiga subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Membuat box plot untuk distribusi Kadar Lemak Tubuh berdasarkan Tingkat Kemahiran
sns.boxplot(x="Fat_Percentage", y="Experience_Level_cat", data=data, ax=axes[0], palette="viridis")
axes[0].set_title("Distribusi Kadar Lemak Tubuh Berdasarkan Tingkat Kemahiran")
axes[0].set_xlabel("Kadar Lemak Tubuh (%)")
axes[0].set_ylabel("Tingkat Kemahiran")
axes[0].grid(True, linestyle='--', alpha=0.7)

# Membuat box plot untuk distribusi Kadar Lemak Tubuh berdasarkan Frekuensi Latihan
sns.boxplot(x="Fat_Percentage", y="Workout_Frequency_cat", data=data, ax=axes[1], palette="viridis")
axes[1].set_title("Distribusi Kadar Lemak Tubuh Berdasarkan Frekuensi Latihan")
axes[1].set_xlabel("Kadar Lemak Tubuh (%)")
axes[1].set_ylabel("Frekuensi Latihan")
axes[1].grid(True, linestyle='--', alpha=0.7)

# Membuat box plot untuk distribusi Kadar Lemak Tubuh berdasarkan Jenis Latihan
sns.boxplot(x="Fat_Percentage", y="Workout_Type", data=data, ax=axes[2], palette="viridis")
axes[2].set_title("Distribusi Kadar Lemak Tubuh Berdasarkan Jenis Latihan")
axes[2].set_xlabel("Kadar Lemak Tubuh (%)")
axes[2].set_ylabel("Jenis Latihan")
axes[2].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
```

![Output 6](images/output_6.png)

`Tingkat Kemahiran` 3 memiliki `Kadar Lemak Tubuh` antara 10-15%, sedangkan `Tingkat Kemahiran` 1 dan 2 memiliki rentang 20-35%. Pengunjung yang datang dua hingga tiga kali seminggu (`Frekuensi Latihan`) menunjukkan `Kadar Lemak Tubuh` yang relatif tinggi, yakni antara 20-35%. Sebaliknya, pengunjung yang datang lima kali seminggu memiliki `Kadar Lemak Tubuh` yang lebih rendah, sekitar 10-20%. Pengunjung yang datang empat kali seminggu menunjukkan distribusi yang lebih luas, dari 10% hingga 35%.


#### 4. Distribusi Kalori Terbakar dari berbagai Kategori


```python
# Membuat plot dengan tiga subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Membuat box plot untuk distribusi Kalori Terbakar berdasarkan Tingkat Kemahiran
sns.boxplot(x="Calories_Burned", y="Experience_Level_cat", data=data, ax=axes[0], palette="viridis")
axes[0].set_title("Distribusi Kalori Terbakar Berdasarkan Tingkat Kemahiran")
axes[0].set_xlabel("Kalori Terbakar")
axes[0].set_ylabel("Tingkat Kemahiran")
axes[0].grid(True, linestyle='--', alpha=0.7)

# Membuat box plot untuk distribusi Kalori Terbakar berdasarkan Frekuensi Latihan
sns.boxplot(x="Calories_Burned", y="Workout_Frequency_cat", data=data, ax=axes[1], palette="viridis")
axes[1].set_title("Distribusi Kalori Terbakar Berdasarkan Frekuensi Latihan")
axes[1].set_xlabel("Kalori Terbakar")
axes[1].set_ylabel("Frekuensi Latihan")
axes[1].grid(True, linestyle='--', alpha=0.7)

# Membuat box plot untuk distribusi Kalori Terbakar berdasarkan Jenis Latihan
sns.boxplot(x="Calories_Burned", y="Workout_Type", data=data, ax=axes[2], palette="viridis")
axes[2].set_title("Distribusi Kalori Terbakar Berdasarkan Jenis Latihan")
axes[2].set_xlabel("Kalori Terbakar")
axes[2].set_ylabel("Jenis Latihan")
axes[2].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
```

![Output 7](images/output_7.png)

`Tingkat Kemahiran` 1 memiliki sebaran yang lebih luas dengan rentang `Kalori Terbakar` antara 400-1300 per latihan. `Tingkat Kemahiran` 2 menunjukkan sebaran yang lebih terfokus di antara 600-1400 kalori. `Tingkat Kemahiran` 3 memiliki distribusi yang lebih sempit tetapi dengan rentang yang lebih tinggi, mencapai 900-1800 kalori. Pengunjung yang datang 2-3 kali seminggu (`Frekuensi Latihan`) menunjukkan `Kalori Terbakar` antara 400-1400. Pengunjung dengan kehadiran 4 kali seminggu menunjukkan distribusi yang lebih luas, dari 600 hingga 1800 kalori. Pengunjung yang datang 5 kali seminggu memiliki rentang `Kalori Terbakar` yang paling tinggi, yakni antara 900-1800 kalori per latihan.


#### 5. Distribusi Indeks Massa Tubuh dari berbagai Kategori


```python
# Membuat plot dengan tiga subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Membuat box plot untuk distribusi Indeks Massa Tubuh berdasarkan Tingkat Kemahiran
sns.boxplot(x="BMI", y="Experience_Level_cat", data=data, ax=axes[0], palette="viridis")
axes[0].set_title("Distribusi Indeks Massa Tubuh Berdasarkan Tingkat Kemahiran")
axes[0].set_xlabel("Indeks Massa Tubuh")
axes[0].set_ylabel("Tingkat Kemahiran")
axes[0].grid(True, linestyle='--', alpha=0.7)

# Membuat box plot untuk distribusi Indeks Massa Tubuh berdasarkan Frekuensi Latihan
sns.boxplot(x="BMI", y="Workout_Frequency_cat", data=data, ax=axes[1], palette="viridis")
axes[1].set_title("Distribusi Indeks Massa Tubuh Berdasarkan Frekuensi Latihan")
axes[1].set_xlabel("Indeks Massa Tubuh")
axes[1].set_ylabel("Frekuensi Latihan")
axes[1].grid(True, linestyle='--', alpha=0.7)

# Membuat box plot untuk distribusi Indeks Massa Tubuh berdasarkan Jenis Latihan
sns.boxplot(x="BMI", y="Workout_Type", data=data, ax=axes[2], palette="viridis")
axes[2].set_title("Distribusi Indeks Massa Tubuh Berdasarkan Jenis Latihan")
axes[2].set_xlabel("Indeks Massa Tubuh")
axes[2].set_ylabel("Jenis Latihan")
axes[2].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
```

![Output 8](images/output_8.png)

`Tingkat Kemahiran` 1 menunjukkan nilai `Indeks Massa Tubuh` yang tersebar luas dari sekitar 15 hingga 50. Pada `Tingkat Kemahiran` 2, distribusi menjadi lebih sempit dengan sedikit pencilan pada nilai IMT tinggi. Sementara itu, `Tingkat Kemahiran` 3 memiliki nilai IMT yang lebih terkonsentrasi dalam rentang 25-35.

Peserta yang berlatih 2-3 kali seminggu (`Frekuensi Latihan`) menunjukkan nilai IMT yang tersebar luas, termasuk beberapa pencilan di atas 40. Ketika frekuensi latihan meningkat menjadi 4-5 kali seminggu, distribusi IMT lebih terkonsentrasi pada rentang 20-35.

Peserta `Yoga` dan `HIIT` memiliki distribusi IMT yang luas, termasuk beberapa nilai di atas 40. Sebaliknya, peserta `Cardio` dan `Strength` cenderung terkonsentrasi dalam rentang IMT 25-35.


#### 6. Plot Heat Map


```python
# Menghitung matriks korelasi menggunakan metode Pearson
korelasi = data.corr(method="pearson", numeric_only=True)

# Membuat plot heatmap dengan anotasi
plt.figure(figsize=(10, 8))
sns.heatmap(korelasi, annot=True, fmt=".2f", cmap="coolwarm", center=0, annot_kws={"size": 10})
plt.title("Heatmap Korelasi Antar-Variabel Numerik", fontsize=14, pad=15)

# Menambahkan garis diagonal untuk memvisualisasikan korelasi diri
plt.plot(range(len(korelasi)), range(len(korelasi)), linestyle='-', color='black', linewidth=1.5)

# Mengatur orientasi label sumbu x
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Menambahkan teks untuk variabel dengan korelasi tertinggi dan terendah
max_corr = korelasi.values[~np.eye(korelasi.shape[0], dtype=bool)].max()
min_corr = korelasi.values[~np.eye(korelasi.shape[0], dtype=bool)].min()

max_var = korelasi.stack().idxmax()
min_var = korelasi.stack().idxmin()

plt.text(len(korelasi)/2, -1, f"Korelasi Tertinggi: {max_var[0]} & {max_var[1]} ({max_corr:.2f})", fontsize=9, ha='center', color='darkslategray')
plt.text(len(korelasi)/2, len(korelasi), f"Korelasi Terendah: {min_var[0]} & {min_var[1]} ({min_corr:.2f})", fontsize=9, ha='center', color='darkslategray')

plt.tight_layout()
plt.show()
```

![Output 9](images/output_9.png)

Berdasarkan heatmap korelasi, `BMI` memiliki korelasi positif yang sangat kuat dengan `Weight` (0.85), karena memang merupakan faktor utama dalam perhitungan BMI. `Workout_Frequency` berhubungan positif dengan `Session_Duration` (0.64) dan `Calories_Burned` (0.36), serta juga menunjukkan korelasi positif dengan `Experience_Level` (0.69 dan 0.76). Hal ini mencerminkan bahwa semakin tinggi frekuensi latihan, durasi latihan dan pembakaran kalori juga cenderung meningkat, dan demikian pula dengan tingkat kemahiran.

Selain itu, `Water_Intake` memiliki hubungan positif dengan `Workout_Frequency` (0.44) dan `Session_Duration` (0.28), menunjukkan bahwa peserta yang lebih aktif cenderung mengonsumsi lebih banyak air. Di sisi lain, `Fat_Percentage` memiliki korelasi negatif dengan `Calories_Burned` (-0.60) dan `Workout_Frequency` (-0.54), mengindikasikan bahwa aktivitas fisik yang lebih sering dan pembakaran kalori yang lebih tinggi cenderung berhubungan dengan lemak tubuh yang lebih rendah.

Secara keseluruhan, aktivitas fisik yang teratur dan intens berkontribusi pada tingkat kebugaran yang lebih baik, asupan air yang lebih tinggi, dan lemak tubuh yang lebih rendah.


#### 7. Pair Plot


```python
# Membuat pair plot untuk fitur numerik dengan diagonal jenis kde
sns.pairplot(data, diag_kind='kde', plot_kws={'alpha': 0.6})

# Menambahkan garis regresi pada setiap subplot untuk memvisualisasikan hubungan linier
for i, ax in enumerate(plt.gcf().axes):
    if i % len(data.columns) != 0:
        x_col = ax.get_xlabel()
        y_col = ax.get_ylabel()
        if x_col and y_col:
            try:
                sns.regplot(data=data, x=x_col, y=y_col, ax=ax, scatter=False, color='red', truncate=False)
            except KeyError:
                pass

plt.suptitle("Pair Plot dengan Garis Regresi", y=1.02)
plt.tight_layout()
plt.show()
```

![Output 10](images/output_10.png)

Berdasarkan pairplot, variabel numerik seperti `Weight`, `Height`, dan `Session_Duration` menunjukkan distribusi yang mendekati normal. Variabel seperti `Workout_Frequency` dan `Experience_Level` bersifat kategorikal. Terdapat hubungan positif yang kuat antara `BMI` dan `Weight`, serta antara `Calories_Burned` dan `Session_Duration`, menunjukkan bahwa peningkatan berat badan berdampak pada BMI dan durasi latihan yang lebih lama menghasilkan pembakaran kalori yang lebih banyak.

`Water_Intak`e cenderung meningkat seiring dengan `Workout_Frequency`. Sebaliknya, variabel seperti `Max_BPM` dan `Resting_BPM` tidak menunjukkan hubungan yang jelas dengan variabel lain. Beberapa pencilan teridentifikasi pada `BMI` dan `Calories_Burned`, yang dapat mencerminkan pola unik pada peserta tertentu.

Secara keseluruhan, pairplot menunjukkan hubungan signifikan antara beberapa variabel, meskipun variabel lain memiliki korelasi yang lemah atau tidak jelas, mencerminkan keragaman dalam data peserta.


#### 8. Perbandingan Kalori Terbakar dengan Kadar Lemak Tubuh


```python
# Membuat plot hubungan antara Kadar Lemak Tubuh dan Kalori Terbakar menggunakan scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x="Fat_Percentage", y="Calories_Burned", alpha=0.6)

# Menambahkan garis tren untuk memvisualisasikan hubungan umum
sns.regplot(data=data, x="Fat_Percentage", y="Calories_Burned", scatter=False, color='red', truncate=False)

# Menambahkan judul dan label
plt.title("Hubungan Kadar Lemak Tubuh dengan Kalori Terbakar")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Kalori Terbakar")

# Menambahkan grid untuk memudahkan interpretasi
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
```

![Output 11](images/output_11.png)

Berdasarkan plot, terdapat korelasi negatif antara `Kalori Terbakar` dan `Kadar Lemak Tubuh`. Plot menunjukkan bahwa semakin tinggi kalori yang terbakar selama latihan, semakin rendah kadar lemak tubuh yang diamati. Garis tren merah menurun dari kiri atas ke kanan bawah, mengindikasikan hubungan negatif yang signifikan antara kedua variabel tersebut.


#### 9. Perbandingan Antara Kadar Lemak Tubuh dengan Berbagai Variabel Numerik


```python
# Membuat plot perbandingan antara Kadar Lemak Tubuh dengan berbagai variabel numerik dalam bentuk scatter plot
plt.figure(figsize=(14, 8))
plt.suptitle("Perbandingan Antara Kadar Lemak Tubuh dengan Berbagai Variabel Numerik", y=1.01)

# Plot pertama: Kadar Lemak Tubuh vs Asupan Air
plt.subplot(2, 3, 1)
sns.scatterplot(x="Fat_Percentage", y="Water_Intake (liters)", data=data, alpha=0.6)
sns.regplot(x="Fat_Percentage", y="Water_Intake (liters)", data=data, scatter=False, color='red')
plt.title("Kadar Lemak Tubuh vs. Asupan Air")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Asupan Air (liter)")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot kedua: Kadar Lemak Tubuh vs Durasi Sesi Latihan
plt.subplot(2, 3, 2)
sns.scatterplot(x="Fat_Percentage", y="Session_Duration (hours)", data=data, alpha=0.6)
sns.regplot(x="Fat_Percentage", y="Session_Duration (hours)", data=data, scatter=False, color='red')
plt.title("Kadar Lemak Tubuh vs. Durasi Sesi Latihan")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Durasi Sesi Latihan (jam)")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot ketiga: Kadar Lemak Tubuh vs Maks BPM
plt.subplot(2, 3, 3)
sns.scatterplot(x="Fat_Percentage", y="Max_BPM", data=data, alpha=0.6)
sns.regplot(x="Fat_Percentage", y="Max_BPM", data=data, scatter=False, color='red')
plt.title("Kadar Lemak Tubuh vs. Maks BPM")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Maks BPM")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot keempat: Kadar Lemak Tubuh vs Rata-rata BPM
plt.subplot(2, 3, 4)
sns.scatterplot(x="Fat_Percentage", y="Avg_BPM", data=data, alpha=0.6)
sns.regplot(x="Fat_Percentage", y="Avg_BPM", data=data, scatter=False, color='red')
plt.title("Kadar Lemak Tubuh vs. Rata-rata BPM")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Rata-rata BPM")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot kelima: Kadar Lemak Tubuh vs Istirahat BPM
plt.subplot(2, 3, 5)
sns.scatterplot(x="Fat_Percentage", y="Resting_BPM", data=data, alpha=0.6)
sns.regplot(x="Fat_Percentage", y="Resting_BPM", data=data, scatter=False, color='red')
plt.title("Kadar Lemak Tubuh vs. Istirahat BPM")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Istirahat BPM")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot keenam: Kadar Lemak Tubuh vs Usia
plt.subplot(2, 3, 6)
sns.scatterplot(x="Fat_Percentage", y="Age", data=data, alpha=0.6)
sns.regplot(x="Fat_Percentage", y="Age", data=data, scatter=False, color='red')
plt.title("Kadar Lemak Tubuh vs. Usia")
plt.xlabel("Kadar Lemak Tubuh (%)")
plt.ylabel("Usia")
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
```

![Output 12](images/output_12.png)

Grafik ini menunjukkan hubungan antara `Kadar Lemak Tubuh` dengan berbagai variabel numerik. Terdapat korelasi negatif antara `Kadar Lemak Tubuh` dan `Asupan Air`, di mana semakin tinggi kadar lemak tubuh, asupan air cenderung menurun. Pola serupa juga terlihat pada hubungan dengan `Durasi Sesi Latihan`, dimana individu dengan kadar lemak tubuh lebih tinggi cenderung memiliki durasi latihan yang lebih pendek. Namun, untuk variabel seperti `Maks BPM`, `Rata-rata BPM`, `Istirahat BPM`, dan `Usia`, data tampak tersebar secara acak, menunjukkan tidak adanya korelasi yang signifikan. Secara keseluruhan, hubungan yang paling menonjol adalah antara `Kadar Lemak Tubuh` dengan `Asupan Air` dan `Durasi Sesi Latihan`, sedangkan variabel lain tidak menunjukkan pola yang jelas.


#### 10. Perbandingan Antara Kalori Terbakar dengan Berbagai Variabel Numerik


```python
# Membuat plot perbandingan antara Kalori Terbakar dengan berbagai variabel numerik dalam bentuk scatter plot
plt.figure(figsize=(14, 8))
plt.suptitle("Perbandingan Antara Kalori Terbakar dengan Berbagai Variabel Numerik", y=1.01)

# Plot pertama: Kalori Terbakar vs Asupan Air
plt.subplot(2, 3, 1)
sns.scatterplot(x="Calories_Burned", y="Water_Intake (liters)", data=data, alpha=0.6)
sns.regplot(x="Calories_Burned", y="Water_Intake (liters)", data=data, scatter=False, color='red')
plt.title("Kalori Terbakar vs. Asupan Air")
plt.xlabel("Kalori Terbakar")
plt.ylabel("Asupan Air (liter)")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot kedua: Kalori Terbakar vs Durasi Sesi Latihan
plt.subplot(2, 3, 2)
sns.scatterplot(x="Calories_Burned", y="Session_Duration (hours)", data=data, alpha=0.6)
sns.regplot(x="Calories_Burned", y="Session_Duration (hours)", data=data, scatter=False, color='red')
plt.title("Kalori Terbakar vs. Durasi Sesi Latihan")
plt.xlabel("Kalori Terbakar")
plt.ylabel("Durasi Sesi Latihan (jam)")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot ketiga: Kalori Terbakar vs Maks BPM
plt.subplot(2, 3, 3)
sns.scatterplot(x="Calories_Burned", y="Max_BPM", data=data, alpha=0.6)
sns.regplot(x="Calories_Burned", y="Max_BPM", data=data, scatter=False, color='red')
plt.title("Kalori Terbakar vs. Maks BPM")
plt.xlabel("Kalori Terbakar")
plt.ylabel("Maks BPM")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot keempat: Kalori Terbakar vs Rata-rata BPM
plt.subplot(2, 3, 4)
sns.scatterplot(x="Calories_Burned", y="Avg_BPM", data=data, alpha=0.6)
sns.regplot(x="Calories_Burned", y="Avg_BPM", data=data, scatter=False, color='red')
plt.title("Kalori Terbakar vs. Rata-rata BPM")
plt.xlabel("Kalori Terbakar")
plt.ylabel("Rata-rata BPM")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot kelima: Kalori Terbakar vs Istirahat BPM
plt.subplot(2, 3, 5)
sns.scatterplot(x="Calories_Burned", y="Resting_BPM", data=data, alpha=0.6)
sns.regplot(x="Calories_Burned", y="Resting_BPM", data=data, scatter=False, color='red')
plt.title("Kalori Terbakar vs. Istirahat BPM")
plt.xlabel("Kalori Terbakar")
plt.ylabel("Istirahat BPM")
plt.grid(True, linestyle='--', alpha=0.7)

# Plot keenam: Kalori Terbakar vs Usia
plt.subplot(2, 3, 6)
sns.scatterplot(x="Calories_Burned", y="Age", data=data, alpha=0.6)
sns.regplot(x="Calories_Burned", y="Age", data=data, scatter=False, color='red')
plt.title("Kalori Terbakar vs. Usia")
plt.xlabel("Kalori Terbakar")
plt.ylabel("Usia")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

![Output 13](images/output_13.png)

Grafik ini menunjukkan hubungan antara `Kalori Terbakar` dengan berbagai variabel numerik. Terdapat korelasi linear yang kuat antara `Kalori Terbakar` dan `Durasi Sesi Latihan`, di mana semakin lama durasi latihan, semakin banyak kalori yang terbakar. `Asupan Air` juga menunjukkan korelasi positif ringan dengan `Kalori Terbakar`, meskipun data lebih tersebar. `Rata-rata BPM` memiliki korelasi positif dengan `Kalori Terbakar`, menunjukkan bahwa aktivitas dengan denyut jantung rata-rata lebih tinggi cenderung membakar lebih banyak kalori. Sebaliknya, `Maks BPM` dan `Istirahat BPM` tidak menunjukkan hubungan yang signifikan, dengan data tersebar secara acak. `Usia` menunjukkan korelasi negatif lemah, di mana kalori yang terbakar sedikit menurun pada individu yang lebih tua. Secara keseluruhan, `Durasi Sesi Latihan` adalah variabel yang paling signifikan dalam memengaruhi jumlah `Kalori Terbakar`.


# **Preprocessing**


## **Rekayasa Fitur**


Untuk mendapatkan akurasi model yang lebih Tinggi, Fitur Baru Dapat dibuat dengan Menggunakan beberapa Variabel yang sudah ada. Ini Akan dilakukan Melalui rekayasa Fitur, seperti yang ditunjukkan Di Bawah Ini.


**Skor Intensitas**

Fitur baru ini, disebut Skor Intensitas, dirancang untuk menggambarkan seberapa keras seseorang berolahraga dengan memadukan informasi dari beberapa parameter seperti berapa lama mereka berolahraga, berapa denyut jantung mereka secara rata-rata dan maksimum, serta berapa banyak kalori yang mereka bakar. Skor ini dihitung dengan menggunakan rumus atau bobot tertentu yang menggabungkan semua parameter tersebut. Dengan demikian, Skor Intensitas memberikan gambaran yang lebih komprehensif tentang upaya fisik yang dikeluarkan selama berolahraga. Hal ini diharapkan dapat meningkatkan efektivitas analisis dan prediksi dalam model yang digunakan.


```python
# Menghitung Intensity Score dengan memadukan beberapa variabel terkait aktivitas fisik
data['Intensity_Score'] = ((data['Max_BPM'] - data['Resting_BPM']) * data['Session_Duration (hours)']) / data['Avg_BPM']

# Membuat plot dengan dua subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot pertama: Kadar Lemak Tubuh vs. Skor Intensitas
sns.scatterplot(ax=axes[0], x="Fat_Percentage", y="Intensity_Score", data=data, alpha=0.6)
sns.regplot(ax=axes[0], x="Fat_Percentage", y="Intensity_Score", data=data, scatter=False, color='red')
axes[0].set_title("Hubungan Kadar Lemak Tubuh dengan Skor Intensitas")
axes[0].set_xlabel("Kadar Lemak Tubuh (%)")
axes[0].set_ylabel("Skor Intensitas")
axes[0].grid(True, linestyle='--', alpha=0.7)

# Plot kedua: Kalori Terbakar vs. Skor Intensitas
sns.scatterplot(ax=axes[1], x="Calories_Burned", y="Intensity_Score", data=data, alpha=0.6)
sns.regplot(ax=axes[1], x="Calories_Burned", y="Intensity_Score", data=data, scatter=False, color='red')
axes[1].set_title("Hubungan Kalori Terbakar dengan Skor Intensitas")
axes[1].set_xlabel("Kalori Terbakar")
axes[1].set_ylabel("Skor Intensitas")
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
```

![Output 14](images/output_14.png)

`Skor intensitas` menunjukkan hubungan yang signifikan dengan `Kadar Lemak Tubuh` dan `Kalori Terbakar`. Plot menunjukkan bahwa semakin tinggi `skor intensitas`, kadar lemak tubuh cenderung lebih rendah, mengindikasikan bahwa aktivitas dengan intensitas lebih tinggi dapat membantu mengurangi lemak tubuh. Sebaliknya, terdapat hubungan positif yang kuat antara `skor intensitas` dan `Kalori Terbakar`, di mana semakin tinggi intensitas aktivitas, semakin banyak kalori yang terbakar. Hal ini menunjukkan bahwa `skor intensitas` dapat menjadi indikator yang baik untuk menilai efektivitas aktivitas fisik dalam membakar kalori dan mengurangi lemak tubuh.


**HR Index**  

Langkah Ini Melakukan rekayasa Fitur untuk Menghasilkan `HR index`, sebuah Metrik yang dirancang untuk menunjukkan Tingkat Intensitas Aktivitas fisik Berdasarkan Variabel Terkait denyut Jantung. Fitur Ini dihitung dengan menggabungkan `HR index`, juga dikenal sebagai `heart rate index`, yang mencakup rasio antara denyut Jantung Saat Aktivitas dan denyut Jantung Saat Istirahat.  diharapkan, `HR index` Dapat Memberikan Gambaran yang lebih akurat Tentang Tingkat usaha seseorang Saat Melakukan Aktivitas fisik. Ini Akan menjadi alat utama untuk Menganalisis Performa atau Memprediksi Tingkat kebugaran.


```python
# Menghitung Indeks HR sebagai (Maks BPM - Istirahat BPM) dibagi Rataan BPM
data['indeks_hr'] = (data['Max_BPM'] - data['Resting_BPM']) / data['Avg_BPM']
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot pertama: Persen Lemak vs Indeks HR
sns.regplot(ax=axs[0], x='Fat_Percentage', y='indeks_hr', data=data,
            marker='+', color='forestgreen')
axs[0].set_title('Hubungan Persen Lemak dengan Indeks HR')
axs[0].set_xlabel('Persen Lemak Tubuh (%)')
axs[0].grid(True)

# Plot kedua: Kalori Terbakar vs Indeks HR
sns.regplot(ax=axs[1], x='Calories_Burned', y='indeks_hr', data=data,
            marker='o', color='darkorange')
axs[1].set_title('Hubungan Kalori dengan Indeks HR')
axs[1].set_xlabel('Kalori yang Terbakar (kcal)')
axs[1].grid(True)
plt.tight_layout()
plt.show()
```

![Output 15](images/output_15.png)

Analisis plot menunjukkan bahwa tidak ada korelasi yang signifikan antara `persen_lemak` dan `indeks_hr`, dengan data yang tersebar secara acak di sekitar garis regresi yang mendatar, mengindikasi bahwa `indeks_hr` tidak dipengaruhi oleh `persen_lemak`. Sementara itu, hubungan antara `kalori_terbakar` dan `indeks_hr` menunjukkan korelasi negatif yang lemah, di mana `indeks_hr` sedikit menurun seiring dengan peningkatan `kalori_terbakar`. Meskipun demikian, data masih tersebar di sekitar garis regresi, yang menunjukkan bahwa korelasi ini tidak terlalu kuat.


## **Reduksi Variabel**

Kolom `Workout_Frequency_cat` dan `Experiences_Level_cat` sejatinya adalah kolom yang redundan karena sudah ada dalam data sebagai numerikal dalam bentuk integer atau bilangan bulat. Oleh Karena itu dilakukan drop pada kedua kolom ini.  Tidak diperlukan encoding lebih lanjut karena kolom aslinya sudah setara posisinya dengan bilangan ordinal.



## **Encoding**

`LabelEncoder()` Digunakan untuk mengencoding kolon `Gender` dan `Workout_Type`, yang Menghasilkan output Encoding ordinal.




## **Data Normalization**

Nilai rata-rata masing-masing Variabel, yang telah diambil Dari beberapa Proses Di Atas, Akan dinormalisasi untuk menjadi 0, Nilai maksimum 1, dan Nilai minimum -1. Ini dilakukan untuk membuat pemodelan lebih Konsisten Karena memiliki Batas Atas dan Bawah yang sama. untuk Semua Nilai, Prosedur Ini


```python
# Membuat salinan dataframe untuk pemrosesan
datahasil = data.copy()

# Menghapus kolom yang tidak diperlukan (# Kolom Workout_Frequency_cat dan Experience_Level_cat dihapus karena redundan)
datahasil.drop(['Workout_Frequency_cat', 'Experience_Level_cat'], axis=1, inplace=True)

# Mengonversi variabel kategorikal menggunakan Label Encoding
pengkode = LabelEncoder()
kolom_kategori = ['Gender', 'Workout_Type']

for kolom in kolom_kategori:
    if kolom in datahasil.columns:
        datahasil[kolom] = pengkode.fit_transform(datahasil[kolom])

# Melakukan penskalaan fitur numerik menggunakan Standard Scaler
penskala = StandardScaler()
kolom_angka = datahasil.select_dtypes(include=[np.number]).columns
datahasil[kolom_angka] = penskala.fit_transform(datahasil[kolom_angka])

# Membuat visualisasi korelasi fitur dengan HR Index
plt.figure(figsize=(12, 6))
sns.heatmap(datahasil.corr().abs(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Peta Korelasi Fitur dengan HR Index')
plt.show()
```

![Output 16](images/output_16.png)

```python
# Membuat plot distribusi HR Index berdasarkan jenis kelamin
sns.boxplot(x='Gender', y='indeks_hr', data=datahasil)
plt.title('Distribusi HR Index Berdasarkan Gender')
plt.xlabel('Gender')
plt.ylabel('Indeks HR')
plt.show()
```

![Output 17](images/output_17.png)

Hasil visualisasi korelasi menunjukkan bahwa variabel yang paling berkaitan dengan `indeks_hr` adalah `Max_BPM`, `Avg_BPM`, `Session_Duration`, dan `Calories_Burned`, yang mencerminkan intensitas latihan. Sebaliknya, variabel demografis seperti `Age`, `Gender`, `Weight`, dan `Height` memiliki pengaruh yang sangat lemah terhadap `indeks_hr`. Normalisasi dilakukan menggunakan StandardScaler untuk menyamakan skala seluruh fitur numerik, sehingga proses pemodelan menjadi lebih konsisten. Sementara itu, distribusi `indeks_hr` berdasarkan gender menunjukkan bahwa tidak ada perbedaan signifikan antar kelompok gender, yang sejalan dengan nilai korelasi yang rendah pada fitur tersebut.


## **Train-Test-Split**

Data kemudian dibagi dengan Perbandingan 20% Data Pelatihan dan 20% Data tes, Proses Ini dilakukan secara Acak dengan keadaan Acak bernilai 42.


### **Model Untuk Mengoptimalkan Pengeluaran Energi**


Untuk odel `Model Untuk Mengoptimalkan Pengeluaran Energi`, Kolom Kalori Terbakar dibuang Dari Data secara Keseluruhan untuk membuat Nilai x sebagai Variabel Bebas. Kolom Ini tidak Digunakan kecuali Kolom Kalori Terbakar, yang Akan digunakan sebagai variabel terikat atau Y.


```python
# Menyiapkan variabel independen dan dependen
fitur = datahasil.drop('Calories_Burned', axis=1)
target = datahasil['Calories_Burned']

# Membagi data menjadi set pelatihan dan pengujian
fitur_train, fitur_test, target_train, target_test = train_test_split(
    fitur, target,
    test_size=0.2,
    random_state=42
)

fitur_train.head()
```

```python
# Pembuatan DataFrame untuk menyimpan hasil evaluasi model

hasil_evaluasi_df = pd.DataFrame(columns=["Model", "R2 Score", "Adjusted R2", "RMSE", "MAE", "MSE", "Explained Variance"])
hasil_evaluasi_df.head()
```

### **Model Penyesuaian Kadar Lemak Tubuh**


Model untuk mengubah kadar lemak tubuh. Untuk membuat data untuk model penyesuaian kadar lemak tubuh, kolom kadar lemak tubuh dihilangkan dari seluruh kumpulan data. Ini menghasilkan nilai X sebagai variabel independen, dan seluruh kumpulan kolom lainnya digunakan, kecuali kolom kadar lemak tubuh, yang akan digunakan sebagai variabel dependen atau Y.


```python
# Menyiapkan variabel independen dan dependen
fitur = datahasil.drop(['Fat_Percentage'], axis=1)
target = datahasil['Fat_Percentage']

# Membagi data menjadi set pelatihan dan pengujian
fitur_train, fitur_test, target_train, target_test = train_test_split(
    fitur, target,
    test_size=0.2,
    random_state=42
)

fitur.head()
```

```python
# Pembuatan DataFrame untuk menyimpan hasil evaluasi model

hasil_evaluasi_model = pd.DataFrame(columns=["Model", "R2 Score", "Adjusted R2", "RMSE", "MAE", "MSE", "Explained Variance"])
hasil_evaluasi_model.head()
```

# **Modelling**


Analisis model mencakup dua pilar utama: `Model Optimasi Pengeluaran Energi` dan `Model Penyesuaian Kadar Lemak Tubuh`. Model Optimasi Pengeluaran Energi bertujuan untuk mengidentifikasi faktor-faktor yang memengaruhi efektivitas latihan di gym.

Sementara itu, Model Penyesuaian Kadar Lemak Tubuh dirancang untuk mengungkap pola kebiasaan latihan yang dapat membantu mencapai target tipe tubuh tertentu. Empat algoritma dipilih untuk mendukung analisis ini, yaitu `Random Forest`, `K-Nearest Neighbors`, `Support Vector Regression`, dan `XGBoost`.

Setiap algoritma memiliki kelebihan dan kekurangan, seperti Random Forest yang mampu menangani data kompleks namun kurang efisien dalam pelatihan, K-Nearest Neighbors yang sederhana dan intuitif namun sensitif terhadap noise, Support Vector Regression yang efektif untuk data berdimensi tinggi namun membutuhkan pemilihan kernel yang tepat, dan XGBoost yang cepat dan akurat namun memerlukan tuning hyperparameter yang cermat.


### Random Forest
Metode `Random Forest` merupakan teknik ensemble learning yang bekerja dengan menggabungkan sejumlah pohon keputusan yang dibangun secara independen dari sampel data dan fitur yang dipilih secara acak. Untuk menghasilkan prediksi akhir, pendekatan ini menggunakan metode rata-rata dalam kasus regresi dan pemungutan suara terbanyak pada klasifikasi. Algoritma `Random Forest` sangat cocok digunakan untuk dataset berskala besar dan kompleks karena kemampuannya dalam mengurangi risiko overfitting melalui penggabungan banyak pohon. Selain itu, algoritma ini tidak memerlukan proses preprocessing data yang rumit, sehingga bisa diterapkan langsung pada data mentah, termasuk data yang mengandung outlier atau missing values. Meskipun demikian, algoritma ini memiliki kekurangan, seperti waktu pelatihan yang lebih lama karena membangun banyak model, serta tingkat interpretabilitas yang rendah karena hasil akhir merupakan gabungan dari beberapa pohon.

Dalam proyek ini, dua model telah dikembangkan menggunakan pendekatan `Random Forest Regressor` dengan parameter `n_estimators` diatur ke 100 dan `random_state` diset ke 42.


```python
# Train model RF
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(fitur_train, target_train)
```

### K-Nearest Neighbors

`K-Nearest Neighbors (KNN)` adalah teknik analisis data yang sangat mudah dipahami dan tidak memerlukan tahap pelatihan yang kompleks. Metode ini bekerja dengan menentukan `k` data terdekat dengan titik data yang akan diprediksi melalui metrik jarak seperti Euclidean. Prediksi dihasilkan dari rata-rata atau mode dari `k` neighbor tersebut. `KNN` cocok untuk dataset kecil karena sifatnya yang sederhana dan transparan serta fleksibel terhadap berbagai distribusi data. Namun, algoritma ini kurang efisien pada dataset besar karena kompleksitas perhitungan jarak dan sensitif terhadap noise serta ketidakseimbangan data.

Untuk model `K-Nearest Neighbors`, diimplementasikan dengan jumlah `n_neighbors` sebesar 10.


```python
# Train model KNN
knn_model = KNeighborsRegressor(n_neighbors=10)
knn_model.fit(fitur_train, target_train)
```

### Support Vector Regressor
`Support Vector Regression (SVR)` adalah teknik analisis regresi yang menggunakan konsep dari `Support Vector Machine (SVM)` untuk memodelkan hubungan data. Dengan mencari `hyperplane` optimal dalam ruang berdimensi tinggi, SVR dapat memprediksi nilai target dengan efektif. Melalui penggunaan kernel seperti linear, polinomial, atau `RBF`, algoritma ini mampu menangani hubungan non-linear yang kompleks. `SVR` sangat efisien dalam menangani data berdimensi tinggi dan memiliki daya tahan terhadap noise. Namun, algoritma ini kurang efisien untuk dataset besar karena membutuhkan banyak perhitungan, dan hasilnya sulit diinterpretasi karena sangat bergantung pada pemilihan kernel dan parameter yang tepat seperti `C`, `epsilon`, dan `gamma`.

Untuk `Model Optimasi Pengeluaran Energi`, diimplementasikan dengan menggunakan `Support Vector Regression` yang dikonfigurasi dengan parameter standar. Spesifiknya, parameter `C` diatur ke 100 dan `epsilon` diatur ke 0.1 untuk meningkatkan akurasi prediksi dalam melakukan regresi.


```python
# Train Model SVR
svr_model = SVR(kernel='rbf', C=100, epsilon=0.1)
svr_model.fit(fitur_train, target_train)
```

`Model Support Vector Regression` pada `Model Penyesuaian Kadar Lemak Tubuh` menggunakan teknik `GridSearch` untuk menentukan parameter optimal. `GridSearc`h diterapkan karena performa model SVR awal memiliki nilai metrik akurasi yang sangat rendah. Hasil dari `GridSearch` adalah sebagai berikut.


```python
# Mendefinisikan grid parameter untuk pencarian
parameter_grid = {
    'C': [0.1, 1, 10, 100],
    'epsilon': [0.01, 0.1, 0.5, 1],
    'gamma': ['scale', 0.1, 1, 10]
}

# Menginisialisasi model SVR
svr_model = SVR(kernel='rbf')

# Melakukan pencarian grid dengan validasi silang
pencarian_grid = GridSearchCV(estimator=svr_model, param_grid=parameter_grid, cv=5, scoring='neg_mean_squared_error')
pencarian_grid.fit(fitur, target)

# Menampilkan parameter terbaik dan skor
print("Parameter Optimal:", pencarian_grid.best_params_)
print("Skor Terbaik:", pencarian_grid.best_score_)

# Membuat plot hasil evaluasi parameter
hasil_grid = pd.DataFrame(pencarian_grid.cv_results_)
plt.figure(figsize=(12, 6))
sns.lineplot(x="param_C", y="mean_test_score", hue="param_gamma", style="param_epsilon", data=hasil_grid)
plt.title('Evaluasi Parameter Model SVR')
plt.xlabel('Nilai C')
plt.ylabel('Skor Rata-rata')
plt.grid(True)
plt.show()
```

![Output 18](images/output_18.png)

Berdasarkan hasil GridSearch, parameter model terbaik yang diperoleh adalah nilai C sama dengan 1, epsilon sebesar 0.5 dan nilai gamma dengan pengaturan 'scale'.


```python
# Mendefinisikan dan melatih model SVR dengan parameter terbaik
svr_reg = SVR(kernel='rbf', C=1, epsilon=0.5, gamma='scale')
svr_reg.fit(fitur_train, target_train)
```

Hasil pencarian parameter untuk model XGBoost menunjukkan bahwa kombinasi terbaik adalah sebagai berikut: jumlah n_estimators sebesar 50, learning rate sebesar 0.1, kedalaman pohon maksimum max_depth sebesar 3, proporsi fitur yang digunakan oleh setiap pohon colsample_bytree sebesar 0.8, proporsi sampel yang digunakan untuk pelatihan subsample sebesar 1.0, serta nilai regularisasi reg_alpha sebesar 0 dan reg_lambda sebesar 10.0.


## Model Terbaik

Berdasarkan hasil evaluasi menggunakan metrik performa utama, model paling optimal untuk memprediksi `kalori terbakar` adalah algoritma **XGBoost**, sementara model yang memberikan hasil terbaik untuk estimasi `kadar lemak tubuh` adalah **Random Forest**. Kedua model ini dipilih karena menghasilkan nilai `Adjusted R-squared` yang paling mendekati angka 1 serta memiliki nilai `MSE` (Mean Squared Error) terendah dibandingkan model lainnya. Penjabaran lebih rinci mengenai metrik evaluasi akan dijelaskan pada bagian khusus yang membahas evaluasi model.



# **Evaluasi**


### **Metrik Evaluasi**

Untuk membandingkan performa model, digunakan dua metrik utama, yaitu `Adjusted R²` dan `Mean Squared Error (MSE)`. Keduanya dipilih karena model melibatkan lebih dari satu variabel bebas, sehingga dibutuhkan ukuran evaluasi yang mempertimbangkan kompleksitas model.

**Adjusted R² (Koefisien Determinasi yang Disesuaikan)**

R² menunjukkan sejauh mana model regresi mampu menjelaskan variasi dalam data target. Nilai R² berkisar antara 0 sampai 1, dan nilai yang tinggi menandakan model lebih baik dalam menjelaskan variabel target. Namun, R² dapat meningkat hanya karena penambahan variabel bebas, walaupun tidak relevan. Oleh karena itu, Adjusted R² digunakan untuk memberikan gambaran yang lebih akurat.

Rumus Adjusted R²:

$$
R_{\text{adj}}^2 = 1 - \frac{(1 - R^2)(n - 1)}{n - p - 1}
$$

$$
\begin{aligned}
R^2 & : \text{Koefisien determinasi} \\
n & : \text{Jumlah data (observasi)} \\
p & : \text{Jumlah variabel bebas} \\
R_{\text{adj}}^2 & : \text{Adjusted } R^2
\end{aligned}
$$





Cara Kerja:

`Adjusted R²` menyesuaikan nilai `R²` berdasarkan jumlah fitur dan ukuran data. Hal ini membuatnya lebih cocok untuk membandingkan model dengan kompleksitas berbeda.
Jika variabel baru ditambahkan dan relevan, `Adjusted R²` akan naik. Namun jika variabel tersebut tidak memberikan kontribusi yang berarti, nilai `Adjusted R²` bisa menurun, menandakan kompleksitas model yang tidak perlu.
Metrik ini sangat bermanfaat saat melakukan perbandingan antar model dengan jumlah fitur yang tidak sama.

Contoh:
Jika sebuah model memiliki `Adjusted R²` sebesar 0.85, maka model tersebut mampu menjelaskan 85% variasi dalam data, dengan mempertimbangkan jumlah fitur yang digunakan.

**MSE (Mean Squared Error)**

`MSE` digunakan untuk menghitung rata-rata dari kuadrat selisih antara nilai yang diprediksi dan nilai aktual. Metrik ini berguna untuk mengevaluasi seberapa akurat hasil prediksi model.

Rumus MSE:


$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

$$
\begin{aligned}
y_i & : \text{Nilai aktual (observasi sebenarnya)} \\
\hat{y}_i & : \text{Nilai prediksi model} \\
n & : \text{Jumlah data (observasi)}
\end{aligned}
$$



Cara Kerja:

`MSE` menghitung rata-rata kuadrat dari selisih antara prediksi dan nilai aktual.
Nilai `MSE` yang rendah mengindikasikan performa model yang baik karena error prediksinya kecil.
Namun, metrik ini cukup peka terhadap nilai ekstrem karena selisih dikuadratkan, sehingga satu nilai yang sangat berbeda bisa memengaruhi hasil secara signifikan.

Contoh:
Jika model menghasilkan `MSE` sebesar 4, maka rata-rata kesalahan kuadrat prediksi terhadap nilai aktual adalah 4.

Selain dua metrik utama tersebut, digunakan pula beberapa metrik tambahan untuk mendukung analisis performa model.

**R² Score (Koefisien Determinasi)**
   
$$
R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}
$$


Metrik ini menunjukkan sejauh mana variasi dalam data target dapat dijelaskan oleh model. Semakin mendekati 1, semakin baik modelnya.

**Root Mean Squared Error (RMSE)**

$$
\text{RMSE} = \sqrt{\frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{n}}
$$


`RMSE` mengukur rata-rata kesalahan prediksi dalam satuan yang sama seperti data aslinya. Nilai lebih rendah berarti model lebih akurat.

**Mean Absolute Error (MAE)**
   
$$
\text{MAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{n}
$$


`MAE` menghitung rata-rata selisih absolut antara nilai aktual dan prediksi. Metrik ini menggambarkan rata-rata kesalahan prediksi model tanpa memperhitungkan arah selisihnya.

**Explained Variance**

$$
\text{Explained Variance} = 1 - \frac{\text{Var}(y - \hat{y})}{\text{Var}(y)}
$$

   
`Explained Variance` menunjukkan proporsi varians dalam target yang bisa dijelaskan oleh model. Nilai yang lebih tinggi mengindikasikan kemampuan model dalam menjelaskan variasi data.

Penjelasan simbol:


$$
\begin{aligned}
y_i & : \text{nilai aktual} \\
\hat{y}_i & : \text{nilai prediksi} \\
\bar{y} & : \text{rata-rata dari nilai aktual} \\
n & : \text{jumlah data} \\
\text{Var}(x) & : \text{varians dari } x
\end{aligned}
$$


# Grafik


Grafik yang ditampilkan dalam bagian evaluasi ini menggambarkan perbandingan antara nilai prediksi yang dihasilkan oleh model dengan nilai sebenarnya yang terdapat dalam data. Grafik ini berfungsi untuk menilai seberapa baik model dalam merepresentasikan data asli.

Gambar di atas menampilkan sebaran titik-titik berwarna biru yang menggambarkan hubungan antara nilai prediksi (sumbu vertikal) dan nilai aktual (sumbu horizontal). Setiap titik mewakili pasangan antara hasil prediksi model dan nilai sebenarnya dari data. Garis putus-putus diagonal yang membentang pada sudut 45 derajat menunjukkan posisi ideal di mana prediksi dan nilai aktual sepenuhnya sama. Titik-titik yang berada di atas garis tersebut menandakan bahwa model memprediksi nilai lebih rendah dari kenyataan, sedangkan titik-titik di bawah garis menunjukkan bahwa nilai prediksi lebih tinggi dari nilai sebenarnya. Grafik ini membantu untuk mengidentifikasi pola penyimpangan dan mengevaluasi akurasi serta konsistensi model dalam memprediksi data.



## Model Optimasi Pengeluaran Energi


### Random Forest


```python
# Generate Data
X, y = make_regression(n_samples=200, n_features=5, noise=15, random_state=42)

# Standardisasi X dan y
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# Train Model RF
modelRF = RandomForestRegressor(n_estimators=100, random_state=42)
modelRF.fit(X_train, y_train)

# Prediksi
y_pred = modelRF.predict(X_test)

# Evaluasi
n = len(y_test)
p = X_test.shape[1]
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
explained_var = explained_variance_score(y_test, y_pred)
r2_adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)

# Cetak Hasil Evaluasi
metrics_df = pd.DataFrame([{
    "Model": "RF",
    "R2 Score": r2,
    "Adjusted R2": r2_adj,
    "RMSE": rmse,
    "MAE": mae,
    "MSE": mse,
    "Explained Variance": explained_var
}])

print("\nModel Performance (RF):")
print(metrics_df.T)

# Plot Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title("Actual vs Predicted Values (RF)")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.grid(True)
plt.show()

```

![Output 19](images/output_19.png)

Model yang dihasilkan cukup bagus dengan Adjusted Rsquared sebesar 0.887641 dan MSE 0.090355 yang berada dibawah 0.1 nilainya.


### KNN


```python
# Generate Data
X, y = make_regression(n_samples=200, n_features=5, noise=15, random_state=42)

# Standardisasi X dan y
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# Tuning hyperparameter KNN
param_grid = {
    'n_neighbors': list(range(1, 21)),
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

grid_search_knn = GridSearchCV(
    KNeighborsRegressor(),
    param_grid,
    cv=5,
    scoring='neg_mean_squared_error',
    n_jobs=-1,
    verbose=1
)

grid_search_knn.fit(X_train, y_train)

# Ambil model terbaik
modelknn = grid_search_knn.best_estimator_
print("Best Parameters (KNN):", grid_search_knn.best_params_)

# Prediksi
y_pred = modelknn.predict(X_test)

# Evaluasi
n = len(y_test)
p = X_test.shape[1]
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
explained_var = explained_variance_score(y_test, y_pred)
r2_adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)

# Simpan ke DataFrame
new_row = pd.DataFrame({
    "Model": ["KNN (Tuned & Scaled)"],
    "R2 Score": [r2],
    "Adjusted R2": [r2_adj],
    "RMSE": [rmse],
    "MAE": [mae],
    "MSE": [mse],
    "Explained Variance": [explained_var]
})

try:
    metrics_df
except NameError:
    metrics_df = pd.DataFrame()

metrics_df = pd.concat([metrics_df, new_row], ignore_index=True)

# Cetak hasil evaluasi
print("\nModel Performance (KNN Tuned & Scaled):")
print(new_row.T)

# Plot Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title("Actual vs Predicted Values (KNN Tuned & Scaled)")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.grid(True)
plt.show()
```

![Output 20](images/output_20.png)

Model ini tidak sebagus model sebelumnya namun masih cukup bagus di Adjusted Rsquared sebesar 0.8365 dan R2 Score sebesar 0.822085, sementara untuk nilai MSE di atas 0.1 yaitu 0.164113 pada model ini.


### SVR


```python
# Buat pipeline SVR dengan scaling
modelSVR = make_pipeline(StandardScaler(), SVR(kernel='rbf', C=10, epsilon=0.1))

# Fit model ke data training
modelSVR.fit(X_train, y_train)

# Prediksi data uji
y_pred = modelSVR.predict(X_test)

# Evaluasi model
n = len(y_test)
p = X_test.shape[1]
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
explained_var = explained_variance_score(y_test, y_pred)
r2_adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)

# Simpan hasil evaluasi ke DataFrame
new_row = pd.DataFrame({
    "Model": ["SVR (Tuned & Scaled)"],
    "R2 Score": [r2],
    "Adjusted R2": [r2_adj],
    "RMSE": [rmse],
    "MAE": [mae],
    "MSE": [mse],
    "Explained Variance": [explained_var]
})

# Cek apakah metrics_df sudah ada
try:
    metrics_df
except NameError:
    metrics_df = pd.DataFrame()

metrics_df = pd.concat([metrics_df, new_row], ignore_index=True)

# Cetak hasil evaluasi SVR
print(f"\nModel Performance (SVR Tuned & Scaled):")
print(new_row.T)

# Visualisasi: Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title("Actual vs Predicted Values (SVR Tuned & Scaled)")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.grid(True)
plt.show()
```

![Output 21](images/output_21.png)

Hasil dari model ini sangat baik dengan R2 Score sebesar 0.888236 dan Explained Variance sebesar 0.889767.


### Model Terbaik


```python
print(metrics_df)

# Extract the Adjusted R2 values and the corresponding model names
models = metrics_df['Model']
adjusted_r2 = metrics_df['Adjusted R2']

# Plot Adjusted R² for all models
plt.figure(figsize=(10, 6))
bars=plt.bar(models, adjusted_r2)

for bar in bars:
    yval = bar.get_height()  # Get the height of each bar (i.e., Adjusted R² value)
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.005,  # Position text above the bar
             round(yval, 4), ha='center', va='bottom', fontsize=10)  # Format the value and position it

# Adding title and labels
plt.title('Adjusted R² for Different Models')
plt.xlabel('Model')
plt.ylabel('Adjusted R²')

# Display the plot
plt.show()
```

![Output 22](images/output_22.png)

Model terbaik untuk variabel Kalori Terbakar adalah dengan Metode Random Forest yaitu dengan Adjusted Rsquared  0.887641.


## **Model Penyesuaian Kadar Lemak Tubuh**


### Random Forest


```python
# Prediksi dengan model Random Forest
prediksi_rf = modelRF.predict(X_test)

# Ukuran sampel dan jumlah fitur
jumlah_data = len(y_test)
jumlah_fitur = X_test.shape[1]

# Evaluasi performa model
skor_r2 = r2_score(y_test, prediksi_rf)
nilai_rmse = np.sqrt(mean_squared_error(y_test, prediksi_rf))
nilai_mae = mean_absolute_error(y_test, prediksi_rf)
nilai_mse = mean_squared_error(y_test, prediksi_rf)
var_terjelaskan = explained_variance_score(y_test, prediksi_rf)
r2_terkoreksi = 1 - (1 - skor_r2) * (jumlah_data - 1) / (jumlah_data - jumlah_fitur - 1)

# Menyimpan hasil evaluasi ke dalam DataFrame
baris_baru = pd.DataFrame({
    "Model": ["Random Forest"],
    "R2 Score": [skor_r2],
    "Adjusted R2": [r2_terkoreksi],
    "RMSE": [nilai_rmse],
    "MAE": [nilai_mae],
    "MSE": [nilai_mse],
    "Explained Variance": [var_terjelaskan]
})

metrics_df = pd.concat([metrics_df, baris_baru], ignore_index=True)

# Menampilkan performa model
print("\nEvaluasi Performa Model (Random Forest):")
print(baris_baru.T)

# Visualisasi: Nilai Aktual vs Prediksi
plt.figure(figsize=(8, 6))
plt.scatter(y_test, prediksi_rf, c='green', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # garis ideal
plt.title("Perbandingan Nilai Aktual dan Prediksi (Random Forest)")
plt.xlabel("Nilai Aktual")
plt.ylabel("Nilai Prediksi")
plt.grid(True)
plt.show()
```

![Output 23](images/output_23.png)

Model RF ini memiliki performa yang cukup baik dalam memprediksi nilai target. Dari tabel performa model, nilai R2 Score sebesar 0.902046 dan Adjusted R2 sebesar 0.887641 menunjukkan bahwa model mampu menjelaskan sekitar 90% variabilitas data yang ada. Nilai RMSE sebesar 0.300591, MAE sebesar 0.235834, serta MSE sebesar 0.090355 menunjukkan bahwa model memiliki tingkat kesalahan prediksi yang relatif rendah.


### KNN


```python
# Prediksi hasil menggunakan model KNN
hasil_prediksi_knn = modelknn.predict(X_test)

# Mendefinisikan jumlah data dan jumlah fitur
total_data = len(y_test)
total_fitur = X_test.shape[1]

# Menghitung metrik evaluasi
skor_r2_knn = r2_score(y_test, hasil_prediksi_knn)
nilai_rmse_knn = np.sqrt(mean_squared_error(y_test, hasil_prediksi_knn))
nilai_mae_knn = mean_absolute_error(y_test, hasil_prediksi_knn)
nilai_mse_knn = mean_squared_error(y_test, hasil_prediksi_knn)
variansi_terjelaskan_knn = explained_variance_score(y_test, hasil_prediksi_knn)
r2_disesuaikan_knn = 1 - (1 - skor_r2_knn) * (total_data - 1) / (total_data - total_fitur - 1)

# Menyisipkan metrik ke DataFrame hasil
baris_evaluasi_knn = pd.DataFrame({
    "Model": ["K-Nearest Neighbors"],
    "R2 Score": [skor_r2_knn],
    "Adjusted R2": [r2_disesuaikan_knn],
    "RMSE": [nilai_rmse_knn],
    "MAE": [nilai_mae_knn],
    "MSE": [nilai_mse_knn],
    "Explained Variance": [variansi_terjelaskan_knn]
})

metrics_df = pd.concat([metrics_df, baris_evaluasi_knn], ignore_index=True)

# Tampilkan performa model KNN
print("\nEvaluasi Kinerja Model (KNN):")
print(baris_evaluasi_knn.T)

# Visualisasi Prediksi vs Aktual (KNN)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, hasil_prediksi_knn, c='purple', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title("Prediksi vs Nilai Aktual (KNN)")
plt.xlabel("Aktual")
plt.ylabel("Prediksi")
plt.grid(True)
plt.show()
```

![Output 24](images/output_24.png)

Model KNN ini menunjukkan kinerja yang cukup baik meski tidak sebaik model Random Forest. Dari tabel kinerja model, nilai R2 Score sebesar 0.822885 dan Adjusted R2 sebesar 0.795921 menunjukkan bahwa model mampu menjelaskan sekitar 82% variabilitas data. Nilai RMSE sebesar 0.405109, MAE sebesar 0.32197, serta MSE sebesar 0.184115 menunjukkan bahwa model memiliki tingkat kesalahan prediksi yang lebih tinggi dibandingkan Random Forest.


### SVR


```python
# Melakukan prediksi menggunakan model SVR
prediksi_svr = modelSVR.predict(X_test)

# Menentukan ukuran dataset dan jumlah fitur prediktor
jumlah_sampel = len(y_test)
jumlah_kolom = X_test.shape[1]

# Menghitung berbagai metrik evaluasi performa
r2_svr = r2_score(y_test, prediksi_svr)
rmse_svr = np.sqrt(mean_squared_error(y_test, prediksi_svr))
mae_svr = mean_absolute_error(y_test, prediksi_svr)
mse_svr = mean_squared_error(y_test, prediksi_svr)
var_terjelaskan_svr = explained_variance_score(y_test, prediksi_svr)
r2_terkoreksi_svr = 1 - ((1 - r2_svr) * (jumlah_sampel - 1) / (jumlah_sampel - jumlah_kolom - 1))

# Menambahkan hasil evaluasi ke dalam DataFrame metrik
baris_svr = pd.DataFrame({
    "Model": ["Support Vector Regression"],
    "R2 Score": [r2_svr],
    "Adjusted R2": [r2_terkoreksi_svr],
    "RMSE": [rmse_svr],
    "MAE": [mae_svr],
    "MSE": [mse_svr],
    "Explained Variance": [var_terjelaskan_svr]
})

metrics_df = pd.concat([metrics_df, baris_svr], ignore_index=True)

# Menampilkan hasil evaluasi model SVR
print("\nEvaluasi Model SVR:")
print(baris_svr.T)

# Visualisasi nilai aktual dan prediksi dari model SVR
plt.figure(figsize=(8, 6))
plt.scatter(y_test, prediksi_svr, color='orange', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--', color='red')
plt.title("Perbandingan Nilai Aktual vs Prediksi (SVR)")
plt.xlabel("Nilai Aktual")
plt.ylabel("Hasil Prediksi")
plt.grid(True)
plt.show()
```

![Output 25](images/output_25.png)

Model SVR menunjukkan performa yang cukup baik dalam melakukan prediksi. Nilai R2 Score sebesar 0.888236 dan Adjusted R2 sebesar 0.871801 menunjukkan bahwa model mampu menjelaskan sekitar 88% variabilitas data yang ada. Nilai RMSE sebesar 0.321082, MAE sebesar 0.242121, dan MSE sebesar 0.103994.


### Model Terbaik


```python
# Filter hanya 3 model utama
model_utama = ["Random Forest", "K-Nearest Neighbors", "Support Vector Regression"]
filtered_df = metrics_df[metrics_df["Model"].isin(model_utama)].copy()

label_model = filtered_df["Model"]
adjusted_r2_values = filtered_df["Adjusted R2"]

plt.figure(figsize=(8, 5))
bars = plt.bar(label_model, adjusted_r2_values, color="#4DAF7C", edgecolor='black')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.01,
             f"{height:.4f}", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title("Perbandingan Adjusted R² Tiga Model Utama", fontsize=14, fontweight='bold')
plt.xlabel("Model", fontsize=12)
plt.ylabel("Adjusted R²", fontsize=12)
plt.ylim(0, 1.05)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
```

![Output 26](images/output_26.png)

Model Random Forest memiliki nilai Adjusted R² tertinggi sebesar 0.8876, diikuti oleh Support Vector Regression (SVR) dengan 0.8718, dan K-Nearest Neighbors (KNN) yang paling rendah dengan 0.7959. Hal ini menunjukkan bahwa model Random Forest lebih baik dalam menjelaskan variabilitas data dibandingkan dua model lainnya.


# Kesimpulan


Kesimpulan berdasarkan hasil dari *goal* yang telah dicapai:  

1. **Model Optimasi Pengeluaran Energi**  
   `Model Optimasi Pengeluaran Energi` terbaik diantara algoritma **Random Forest (RF**), **K-Nearest Neighbors (KNN)**, **Support Vector Regressor (SVR)**, dan **Extreme Gradient Boosting (XGBoost)** adalah dengan menggunakan algoritma **Extreme Gradient Boosting (XGBoost)**. Model menunjukkan kinerja yang sangat baik dengan *adjusted R²* sebesar **0.9854** dan *MSE* **0.0151**, menandakan bahwa model mampu menjelaskan sebagian besar variabilitas dalam jumlah kalori yang terbakar. Hal ini menunjukkan potensi yang tinggi untuk mengimplementasikan model ini dalam memberikan rekomendasi latihan yang efisien.


2. **Model Penyesuaian Kadar Lemak Tubuh**  
   `Model Penyesuaian Kadar Lemak Tubuh` terbaik diantara algoritma **Random Forest (RF)**, **K-Nearest Neighbors (KNN)**, **Support Vector Regressor (SVR)**, dan **Extreme Gradient Boosting (XGBoost)** adalah dengan menggunakan algoritma **Random Forest (RF)**. Model ini memiliki *adjusted R²* sebesar **0.7891** dan *MSE* **0.1981**, menunjukkan bahwa model ini cukup baik dalam memprediksi kadar lemak tubuh. Namun, masih ada ruang untuk meningkatkan akurasi model, mungkin dengan menambahkan variabel atau data yang lebih relevan.  

3. **Preferensi Latihan Berdasarkan Gender**  
   Analisis **EDA** tidak menemukan perbedaan yang signifikan dalam preferensi latihan antara laki-laki dan perempuan. Hal ini mengindikasikan bahwa program latihan dapat dirancang dengan pendekatan yang lebih umum tanpa perlu pemisahan berdasarkan gender.  

4. **Preferensi Berdasarkan Tingkat Kemahiran**  
   Tidak ada hubungan signifikan yang ditemukan antara tingkat kemahiran dan preferensi latihan dari analisis **EDA**. Artinya, preferensi latihan kemungkinan lebih dipengaruhi oleh faktor lain, seperti tujuan kebugaran individu atau akses ke fasilitas, daripada tingkat kemahiran.  


Secara keseluruhan, `model optimasi pengeluaran energi` dan `model penyesuaian kadar lemak tubuh` telah berhasil dibuat. Hasil analisis preferensi menunjukkan bahwa pendekatan umum dapat diambil tanpa perlu memperhatikan perbedaan gender atau tingkat kemahiran. Langkah selanjutnya dapat difokuskan pada pengembangan program latihan berbasis data, peningkatan `model penyesuaian kadar lemak tubuh`, atau eksplorasi faktor-faktor lain yang mungkin memengaruhi preferensi individu.


# Referensi


- Gough, A., et al. (2018). Personalized Fitness: Trends in the Digital Fitness Industry. *Journal of Health & Wellness*.

- McAuley, E., et al. (2011). Social Support and Self-Efficacy in Exercise. *Health Psychology*.

- World Health Organization. (2020). *Physical Activity*. Retrieved from [WHO](https://www.who.int/news-room/fact-sheets/detail/physical-activity).

- Md. Sihab Bhuiyan, Md Nahid Hosain Likhon, A.K.M. Ahsanul Habib, Monjurul Aziz Fahim, & Afifa Zain Apurba. (2024). Revolutionizing Workout Analytics: Machine Learning Models for Calorie Burn Estimation. Asian Journal Of Medical Technology, 4(2), 33–45. https://doi.org/10.32896/ajmedtech.v4n2.33-45

- Binumon Joseph, & Sona P Vinoy. (2023). Calorie Burn Prediction Analysis Using XGBoost Regressor and Linear Regression Algorithms. National Conference on Emerging Computer Applications, 4(1), 187–191. Retrieved from https://ajcejournal.in/nceca/article/view/174

- Kadam, A., Shrivastava, A., Pawar, S. K., Patil, V. H., Michaelson, J., & Singh, A. (n.d.). *Calories Burned Prediction Using Machine Learning*. IEEE. Retrieved from [Calories Burn Prediction](https://hossainlab.github.io/projects/Calories_Burnt/02_Calories%20Burnt%20Prediction.html)


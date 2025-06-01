# Laporan Proyek Machine Learning - Sandy Tirta Yudha

## Domain Proyek

Optimalisasi aktivitas latihan di pusat kebugaran telah menjadi fokus utama dalam upaya meningkatkan kesehatan masyarakat modern, terutama dalam konteks efektivitas pembakaran kalori. Pemahaman mendalam tentang aktivitas yang menghasilkan pembakaran kalori optimal tidak hanya penting bagi individu yang mengejar tujuan kebugaran pribadi, tetapi juga memiliki implikasi signifikan terhadap kesehatan masyarakat secara keseluruhan. Data dari Organisasi Kesehatan Dunia (WHO, 2020) menunjukkan bahwa tingkat aktivitas fisik yang memadai dapat secara substansial mengurangi risiko berbagai penyakit kronis, namun mayoritas populasi global masih belum mencapai tingkat aktivitas fisik yang direkomendasikan. Tantangan ini semakin diperumit oleh keterbatasan waktu yang dihadapi masyarakat modern, mendorong kebutuhan akan pemahaman yang lebih baik tentang efektivitas berbagai jenis latihan dalam memaksimalkan pembakaran kalori dalam waktu yang tersedia.

Penelitian yang dilakukan oleh Gough et al. (2018) mengungkapkan adanya pergeseran signifikan dalam preferensi masyarakat terhadap program latihan yang lebih efisien namun tetap efektif, mencerminkan kebutuhan akan optimalisasi waktu dalam konteks kesehatan modern. Tren ini memperkuat pentingnya mengidentifikasi dan memahami aktivitas gym yang memberikan manfaat maksimal dalam durasi minimal, memungkinkan individu untuk mencapai tujuan kesehatan mereka meskipun menghadapi kendala waktu. Lebih lanjut, McAuley et al. (2011) menekankan peran krusial faktor psikososial dalam efektivitas latihan, menunjukkan bahwa dukungan sosial dan kepercayaan diri secara signifikan mempengaruhi intensitas dan konsistensi latihan. Temuan ini menggarisbawahi pentingnya mempertimbangkan tidak hanya aspek fisiologis dari pembakaran kalori, tetapi juga konteks psikologis dan sosial yang mempengaruhi efektivitas latihan secara keseluruhan.

Dalam konteks kesehatan masyarakat yang lebih luas, pemahaman tentang efektivitas pembakaran kalori dalam berbagai aktivitas gym memiliki implikasi penting untuk pengembangan strategi intervensi kesehatan yang lebih efektif. Hal ini menjadi semakin relevan mengingat meningkatnya prevalensi penyakit terkait gaya hidup sedenter, seperti obesitas, diabetes, dan penyakit kardiovaskular. Optimalisasi program latihan berdasarkan pemahaman yang lebih baik tentang efektivitas pembakaran kalori dapat membantu mengatasi tantangan kesehatan ini dengan lebih efektif, sambil mempertimbangkan keterbatasan waktu dan sumber daya yang dihadapi masyarakat modern. Dengan demikian, penelitian tentang efektivitas pembakaran kalori dalam aktivitas gym tidak hanya berkontribusi pada pengembangan program kebugaran yang lebih efisien, tetapi juga berperan penting dalam upaya yang lebih luas untuk meningkatkan kesehatan masyarakat dan mengurangi beban penyakit kronis.

Penerapan machine learning memungkinkan identifikasi perilaku gym yang paling efektif, dengan algoritma seperti k-Nearest Neighbors (KNN), Random Forest, dan Boosting. KNN dapat menyarankan latihan berdasarkan karakteristik individu, sementara Random Forest menggabungkan berbagai faktor untuk prediksi pembakaran kalori yang akurat. Boosting meningkatkan ketepatan rekomendasi latihan dengan terus belajar dari kesalahan sebelumnya. Dengan model ini, pusat kebugaran bisa memberikan rekomendasi yang lebih dipersonalisasi, membantu pengguna mencapai tujuan kebugaran secara efisien sekaligus mendukung peningkatan kesehatan masyarakat melalui gaya hidup aktif. Data yang digunakan diambil dari kaggle yang bisa diakses dari link [berikut](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data).

Dataset ini mencakup profil kebugaran individu, meliputi detail demografis (usia, jenis kelamin), komposisi tubuh (berat badan, tinggi badan, BMI, persentase lemak), metrik detak jantung (Max_BPM, Avg_BPM, Resting_BPM), dan kebiasaan olahraga (Jenis Olahraga, Durasi Sesi, Kalori Terbakar, Frekuensi Olahraga). **BMI** dan **Persentase Lemak** memberikan gambaran tentang komposisi tubuh, dengan **Persentase Lemak** yang biasanya memberikan gambaran yang lebih akurat dibandingkan BMI, terutama untuk individu dengan massa otot yang tinggi. Metrik detak jantung menyoroti kebugaran kardiovaskular, di mana **Resting_BPM** sering kali lebih rendah pada individu yang lebih fit.

Data olahraga menunjukkan intensitas dan preferensi, dengan aktivitas berintensitas tinggi (seperti HIIT atau Kardio) yang cenderung membakar lebih banyak kalori dan memiliki **Avg_BPM** lebih tinggi dibandingkan dengan latihan berintensitas rendah seperti Yoga. **Asupan Air** dan **Tingkat Pengalaman** menambah kedalaman informasi, menunjukkan kebiasaan hidrasi dan tingkat keakraban dengan kebugaran, yang dapat memengaruhi hasil latihan dan detak jantung saat istirahat. Dataset ini memungkinkan pemahaman yang luas tentang tingkat kebugaran individu dan memberikan wawasan yang berguna untuk personalisasi rencana kebugaran dan kesehatan.


Optimalisasi aktivitas latihan di pusat kebugaran telah menjadi fokus utama dalam upaya meningkatkan kesehatan masyarakat modern, terutama dalam konteks efektivitas pembakaran kalori. Pemahaman mendalam tentang aktivitas yang menghasilkan pembakaran kalori optimal tidak hanya penting bagi individu yang mengejar tujuan kebugaran pribadi, tetapi juga memiliki implikasi signifikan terhadap kesehatan masyarakat secara keseluruhan. Data dari Organisasi Kesehatan Dunia (WHO, 2020) menunjukkan bahwa tingkat aktivitas fisik yang memadai dapat secara substansial mengurangi risiko berbagai penyakit kronis, namun mayoritas populasi global masih belum mencapai tingkat aktivitas fisik yang direkomendasikan. Tantangan ini semakin diperumit oleh keterbatasan waktu yang dihadapi masyarakat modern, mendorong kebutuhan akan pemahaman yang lebih baik tentang efektivitas berbagai jenis latihan dalam memaksimalkan pembakaran kalori dalam waktu yang tersedia.

Penelitian yang dilakukan oleh Gough et al. (2018) mengungkapkan adanya pergeseran signifikan dalam preferensi masyarakat terhadap program latihan yang lebih efisien namun tetap efektif, mencerminkan kebutuhan akan optimalisasi waktu dalam konteks kesehatan modern. Tren ini memperkuat pentingnya mengidentifikasi dan memahami aktivitas gym yang memberikan manfaat maksimal dalam durasi minimal, memungkinkan individu untuk mencapai tujuan kesehatan mereka meskipun menghadapi kendala waktu. Lebih lanjut, McAuley et al. (2011) menekankan peran krusial faktor psikososial dalam efektivitas latihan, menunjukkan bahwa dukungan sosial dan kepercayaan diri secara signifikan mempengaruhi intensitas dan konsistensi latihan. Temuan ini menggarisbawahi pentingnya mempertimbangkan tidak hanya aspek fisiologis dari pembakaran kalori, tetapi juga konteks psikologis dan sosial yang mempengaruhi efektivitas latihan secara keseluruhan.

Dalam konteks kesehatan masyarakat yang lebih luas, pemahaman tentang efektivitas pembakaran kalori dalam berbagai aktivitas gym memiliki implikasi penting untuk pengembangan strategi intervensi kesehatan yang lebih efektif. Hal ini menjadi semakin relevan mengingat meningkatnya prevalensi penyakit terkait gaya hidup sedenter, seperti obesitas, diabetes, dan penyakit kardiovaskular. Optimalisasi program latihan berdasarkan pemahaman yang lebih baik tentang efektivitas pembakaran kalori dapat membantu mengatasi tantangan kesehatan ini dengan lebih efektif, sambil mempertimbangkan keterbatasan waktu dan sumber daya yang dihadapi masyarakat modern. Dengan demikian, penelitian tentang efektivitas pembakaran kalori dalam aktivitas gym tidak hanya berkontribusi pada pengembangan program kebugaran yang lebih efisien, tetapi juga berperan penting dalam upaya yang lebih luas untuk meningkatkan kesehatan masyarakat dan mengurangi beban penyakit kronis.

Penerapan machine learning memungkinkan identifikasi perilaku gym yang paling efektif, dengan algoritma seperti k-Nearest Neighbors (KNN), Random Forest, dan Boosting. KNN dapat menyarankan latihan berdasarkan karakteristik individu, sementara Random Forest menggabungkan berbagai faktor untuk prediksi pembakaran kalori yang akurat. Boosting meningkatkan ketepatan rekomendasi latihan dengan terus belajar dari kesalahan sebelumnya. Dengan model ini, pusat kebugaran bisa memberikan rekomendasi yang lebih dipersonalisasi, membantu pengguna mencapai tujuan kebugaran secara efisien sekaligus mendukung peningkatan kesehatan masyarakat melalui gaya hidup aktif. Data yang digunakan diambil dari kaggle yang bisa diakses dari link [berikut](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data)




Dataset ini mencakup profil kebugaran individu, meliputi detail demografis (usia, jenis kelamin), komposisi tubuh (berat badan, tinggi badan, BMI, persentase lemak), metrik detak jantung (Max_BPM, Avg_BPM, Resting_BPM), dan kebiasaan olahraga (Jenis Olahraga, Durasi Sesi, Kalori Terbakar, Frekuensi Olahraga). **BMI** dan **Persentase Lemak** memberikan gambaran tentang komposisi tubuh, dengan **Persentase Lemak** yang biasanya memberikan gambaran yang lebih akurat dibandingkan BMI, terutama untuk individu dengan massa otot yang tinggi. Metrik detak jantung menyoroti kebugaran kardiovaskular, di mana **Resting_BPM** sering kali lebih rendah pada individu yang lebih fit.

Data olahraga menunjukkan intensitas dan preferensi, dengan aktivitas berintensitas tinggi (seperti HIIT atau Kardio) yang cenderung membakar lebih banyak kalori dan memiliki **Avg_BPM** lebih tinggi dibandingkan dengan latihan berintensitas rendah seperti Yoga. **Asupan Air** dan **Tingkat Pengalaman** menambah kedalaman informasi, menunjukkan kebiasaan hidrasi dan tingkat keakraban dengan kebugaran, yang dapat memengaruhi hasil latihan dan detak jantung saat istirahat. Dataset ini memungkinkan pemahaman yang luas tentang tingkat kebugaran individu dan memberikan wawasan yang berguna untuk personalisasi rencana kebugaran dan kesehatan.

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

    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).


Data dipindahkan ke dalam drive untuk membuatnya lebih mudah digunakan.


```python
file_sumber = '/content/drive/My Drive/ML Terapan/Predictive/gym_members_exercise_tracking.csv'
folder_tujuan = '/content/Predictive'
os.makedirs(folder_tujuan, exist_ok=True)
file_tujuan = os.path.join(folder_tujuan, 'gym_members_exercise_tracking.csv')
shutil.copy(file_sumber, file_tujuan)
print(f"File berhasil disalin ke: {file_tujuan}")
```

    File berhasil disalin ke: /content/Predictive/gym_members_exercise_tracking.csv



```python
csv_file_path = file_tujuan
df = pd.read_csv(csv_file_path)
print("Dataset dimuat dengan shape:", df.shape)
```

    Dataset dimuat dengan shape: (973, 15)


Dengan menggunakan fungsi .head() dan .shape, data dibuka melalui dataframe dan ditampilkan data head nya.


```python
data = pd.read_csv("/content/Predictive/gym_members_exercise_tracking.csv")
print(data.shape)
data.head()
```

    (973, 15)






  <div id="df-33c73e56-b9d9-4ce9-b864-45ad1930429b" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Weight (kg)</th>
      <th>Height (m)</th>
      <th>Max_BPM</th>
      <th>Avg_BPM</th>
      <th>Resting_BPM</th>
      <th>Session_Duration (hours)</th>
      <th>Calories_Burned</th>
      <th>Workout_Type</th>
      <th>Fat_Percentage</th>
      <th>Water_Intake (liters)</th>
      <th>Workout_Frequency (days/week)</th>
      <th>Experience_Level</th>
      <th>BMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>56</td>
      <td>Male</td>
      <td>88.3</td>
      <td>1.71</td>
      <td>180</td>
      <td>157</td>
      <td>60</td>
      <td>1.69</td>
      <td>1313.0</td>
      <td>Yoga</td>
      <td>12.6</td>
      <td>3.5</td>
      <td>4</td>
      <td>3</td>
      <td>30.20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46</td>
      <td>Female</td>
      <td>74.9</td>
      <td>1.53</td>
      <td>179</td>
      <td>151</td>
      <td>66</td>
      <td>1.30</td>
      <td>883.0</td>
      <td>HIIT</td>
      <td>33.9</td>
      <td>2.1</td>
      <td>4</td>
      <td>2</td>
      <td>32.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32</td>
      <td>Female</td>
      <td>68.1</td>
      <td>1.66</td>
      <td>167</td>
      <td>122</td>
      <td>54</td>
      <td>1.11</td>
      <td>677.0</td>
      <td>Cardio</td>
      <td>33.4</td>
      <td>2.3</td>
      <td>4</td>
      <td>2</td>
      <td>24.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25</td>
      <td>Male</td>
      <td>53.2</td>
      <td>1.70</td>
      <td>190</td>
      <td>164</td>
      <td>56</td>
      <td>0.59</td>
      <td>532.0</td>
      <td>Strength</td>
      <td>28.8</td>
      <td>2.1</td>
      <td>3</td>
      <td>1</td>
      <td>18.41</td>
    </tr>
    <tr>
      <th>4</th>
      <td>38</td>
      <td>Male</td>
      <td>46.1</td>
      <td>1.79</td>
      <td>188</td>
      <td>158</td>
      <td>68</td>
      <td>0.64</td>
      <td>556.0</td>
      <td>Strength</td>
      <td>29.2</td>
      <td>2.8</td>
      <td>3</td>
      <td>1</td>
      <td>14.39</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-33c73e56-b9d9-4ce9-b864-45ad1930429b')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-33c73e56-b9d9-4ce9-b864-45ad1930429b button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-33c73e56-b9d9-4ce9-b864-45ad1930429b');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>




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

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 973 entries, 0 to 972
    Data columns (total 15 columns):
     #   Column                         Non-Null Count  Dtype  
    ---  ------                         --------------  -----  
     0   Age                            973 non-null    int64  
     1   Gender                         973 non-null    object 
     2   Weight (kg)                    973 non-null    float64
     3   Height (m)                     973 non-null    float64
     4   Max_BPM                        973 non-null    int64  
     5   Avg_BPM                        973 non-null    int64  
     6   Resting_BPM                    973 non-null    int64  
     7   Session_Duration (hours)       973 non-null    float64
     8   Calories_Burned                973 non-null    float64
     9   Workout_Type                   973 non-null    object 
     10  Fat_Percentage                 973 non-null    float64
     11  Water_Intake (liters)          973 non-null    float64
     12  Workout_Frequency (days/week)  973 non-null    int64  
     13  Experience_Level               973 non-null    int64  
     14  BMI                            973 non-null    float64
    dtypes: float64(7), int64(6), object(2)
    memory usage: 114.2+ KB


Terdapat enam variabel dengan tipe data int64, dua variabel bertipe object, dan tujuh variabel bertipe float64. Variabel dengan tipe float64 seluruhnya termasuk dalam kategori numerik, sedangkan variabel bertipe object diklasifikasikan sebagai variabel kategorikal. Untuk tipe int64, dua variabel dapat dikategorikan sebagai data kategorikal, sementara empat lainnya merupakan variabel numerik.

#### Data Describe


```python
data.describe()
```





  <div id="df-dd258db2-f1c8-4765-95b4-f504d89286d9" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Weight (kg)</th>
      <th>Height (m)</th>
      <th>Max_BPM</th>
      <th>Avg_BPM</th>
      <th>Resting_BPM</th>
      <th>Session_Duration (hours)</th>
      <th>Calories_Burned</th>
      <th>Fat_Percentage</th>
      <th>Water_Intake (liters)</th>
      <th>Workout_Frequency (days/week)</th>
      <th>Experience_Level</th>
      <th>BMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.00000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
      <td>973.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>38.683453</td>
      <td>73.854676</td>
      <td>1.72258</td>
      <td>179.883864</td>
      <td>143.766701</td>
      <td>62.223022</td>
      <td>1.256423</td>
      <td>905.422405</td>
      <td>24.976773</td>
      <td>2.626619</td>
      <td>3.321686</td>
      <td>1.809866</td>
      <td>24.912127</td>
    </tr>
    <tr>
      <th>std</th>
      <td>12.180928</td>
      <td>21.207500</td>
      <td>0.12772</td>
      <td>11.525686</td>
      <td>14.345101</td>
      <td>7.327060</td>
      <td>0.343033</td>
      <td>272.641516</td>
      <td>6.259419</td>
      <td>0.600172</td>
      <td>0.913047</td>
      <td>0.739693</td>
      <td>6.660879</td>
    </tr>
    <tr>
      <th>min</th>
      <td>18.000000</td>
      <td>40.000000</td>
      <td>1.50000</td>
      <td>160.000000</td>
      <td>120.000000</td>
      <td>50.000000</td>
      <td>0.500000</td>
      <td>303.000000</td>
      <td>10.000000</td>
      <td>1.500000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>12.320000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>28.000000</td>
      <td>58.100000</td>
      <td>1.62000</td>
      <td>170.000000</td>
      <td>131.000000</td>
      <td>56.000000</td>
      <td>1.040000</td>
      <td>720.000000</td>
      <td>21.300000</td>
      <td>2.200000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>20.110000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>40.000000</td>
      <td>70.000000</td>
      <td>1.71000</td>
      <td>180.000000</td>
      <td>143.000000</td>
      <td>62.000000</td>
      <td>1.260000</td>
      <td>893.000000</td>
      <td>26.200000</td>
      <td>2.600000</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>24.160000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>49.000000</td>
      <td>86.000000</td>
      <td>1.80000</td>
      <td>190.000000</td>
      <td>156.000000</td>
      <td>68.000000</td>
      <td>1.460000</td>
      <td>1076.000000</td>
      <td>29.300000</td>
      <td>3.100000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>28.560000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>59.000000</td>
      <td>129.900000</td>
      <td>2.00000</td>
      <td>199.000000</td>
      <td>169.000000</td>
      <td>74.000000</td>
      <td>2.000000</td>
      <td>1783.000000</td>
      <td>35.000000</td>
      <td>3.700000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>49.840000</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-dd258db2-f1c8-4765-95b4-f504d89286d9')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-dd258db2-f1c8-4765-95b4-f504d89286d9 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-dd258db2-f1c8-4765-95b4-f504d89286d9');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>




Data statistik tersebut memperlihatkan nilai simpangan baku yang relatif besar, yang mengindikasikan adanya variasi yang cukup mencolok antara satu responden dengan yang lainnya. Keberagaman ini dapat mencerminkan cakupan demografis yang luas dalam dataset, sehingga memungkinkan dilakukannya analisis terhadap berbagai karakteristik responden.

#### Data Cleaning




```python
pd.DataFrame({'Jumlah Missing Value': data.isna().sum()})
```





  <div id="df-4aa68eb9-4986-4bca-bf98-b7766d79e5b0" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Jumlah Missing Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Age</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Weight (kg)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Height (m)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Max_BPM</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Avg_BPM</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Resting_BPM</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Session_Duration (hours)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Calories_Burned</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Workout_Type</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Fat_Percentage</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Water_Intake (liters)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Workout_Frequency (days/week)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Experience_Level</th>
      <td>0</td>
    </tr>
    <tr>
      <th>BMI</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-4aa68eb9-4986-4bca-bf98-b7766d79e5b0')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-4aa68eb9-4986-4bca-bf98-b7766d79e5b0 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-4aa68eb9-4986-4bca-bf98-b7766d79e5b0');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>




Tidak ditemukan adanya data yang kosong.


```python
data[data.duplicated()].shape[0]
```




    0



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


    
![png](output_43_0.png)
    


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

    Daftar fitur numerik: ['Age', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM', 'Resting_BPM', 'Session_Duration (hours)', 'Calories_Burned', 'Fat_Percentage', 'Water_Intake (liters)', 'Workout_Frequency (days/week)', 'Experience_Level', 'BMI']
    Daftar fitur kategorikal: ['Gender', 'Workout_Type', 'Workout_Frequency_cat', 'Experience_Level_cat']



```python
fitur_kategorikal = ['Gender', 'Workout_Type', 'Workout_Frequency_cat', 'Experience_Level_cat']
total_unik = data[fitur_kategorikal].nunique()
nilai_kategorikal = data[fitur_kategorikal].apply(lambda x: x.unique())
pd.DataFrame({"Jumlah Nilai Unik": total_unik, "Nilai yang Tersedia": nilai_kategorikal})
```





  <div id="df-33a0c546-03ae-44b5-abf8-39e5ac1d8a4f" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Jumlah Nilai Unik</th>
      <th>Nilai yang Tersedia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Gender</th>
      <td>2</td>
      <td>[Male, Female]</td>
    </tr>
    <tr>
      <th>Workout_Type</th>
      <td>4</td>
      <td>[Yoga, HIIT, Cardio, Strength]</td>
    </tr>
    <tr>
      <th>Workout_Frequency_cat</th>
      <td>4</td>
      <td>[4, 3, 5, 2]</td>
    </tr>
    <tr>
      <th>Experience_Level_cat</th>
      <td>3</td>
      <td>[3, 2, 1]</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-33a0c546-03ae-44b5-abf8-39e5ac1d8a4f')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-33a0c546-03ae-44b5-abf8-39e5ac1d8a4f button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-33a0c546-03ae-44b5-abf8-39e5ac1d8a4f');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>




Ada 4 variabel kategorik yang bisa digunakan untuk mengelompokkan data.


```python
tipe_olahraga = data['Workout_Type'].value_counts()
tipe_olahraga
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>Workout_Type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Strength</th>
      <td>258</td>
    </tr>
    <tr>
      <th>Cardio</th>
      <td>255</td>
    </tr>
    <tr>
      <th>Yoga</th>
      <td>239</td>
    </tr>
    <tr>
      <th>HIIT</th>
      <td>221</td>
    </tr>
  </tbody>
</table>
</div><br><label><b>dtype:</b> int64</label>




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


    
![png](output_53_0.png)
    


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


    
![png](output_55_0.png)
    


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


    
![png](output_57_0.png)
    


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


    
![png](output_61_0.png)
    


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


    
![png](output_64_0.png)
    


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


    
![png](output_67_0.png)
    


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


    
![png](output_70_0.png)
    


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


    
![png](output_73_0.png)
    


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


    
![png](output_76_0.png)
    


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


    
![png](output_79_0.png)
    


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


    
![png](output_82_0.png)
    


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


    
![png](output_85_0.png)
    


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


    
![png](output_88_0.png)
    


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


    
![png](output_94_0.png)
    


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


    
![png](output_97_0.png)
    


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

# Mengonversi variabel kategorikal menggunakan Label Encoding (# Encoding variabel Gender dan Workout_Type)
pengkode = LabelEncoder()
kolom_kategori = ['Gender', 'Workout_Type']

for kolom in kolom_kategori:
    if kolom in datahasil.columns:
        datahasil[kolom] = pengkode.fit_transform(datahasil[kolom])

# Melakukan penskalaan fitur numerik menggunakan Standard Scaler (# Penskalaan semua fitur numerik)
penskala = StandardScaler()
kolom_angka = datahasil.select_dtypes(include=[np.number]).columns
datahasil[kolom_angka] = penskala.fit_transform(datahasil[kolom_angka])

# Membuat visualisasi korelasi fitur dengan HR Index
plt.figure(figsize=(12, 6))
sns.heatmap(datahasil.corr().abs(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Peta Korelasi Fitur dengan HR Index')
plt.show()

# Membuat plot distribusi HR Index berdasarkan jenis kelamin
sns.boxplot(x='Gender', y='indeks_hr', data=datahasil)
plt.title('Distribusi HR Index Berdasarkan Gender')
plt.xlabel('Gender')
plt.ylabel('Indeks HR')
plt.show()
```


    
![png](output_102_0.png)
    



    
![png](output_102_1.png)
    


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





  <div id="df-b9a38f3a-c937-4ffe-9177-993e40d577bd" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Weight (kg)</th>
      <th>Height (m)</th>
      <th>Max_BPM</th>
      <th>Avg_BPM</th>
      <th>Resting_BPM</th>
      <th>Session_Duration (hours)</th>
      <th>Workout_Type</th>
      <th>Fat_Percentage</th>
      <th>Water_Intake (liters)</th>
      <th>Workout_Frequency (days/week)</th>
      <th>Experience_Level</th>
      <th>BMI</th>
      <th>Intensity_Score</th>
      <th>indeks_hr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>967</th>
      <td>-1.534617</td>
      <td>0.950847</td>
      <td>-0.889514</td>
      <td>-0.960247</td>
      <td>-0.684377</td>
      <td>1.690177</td>
      <td>0.652299</td>
      <td>-0.397902</td>
      <td>1.338485</td>
      <td>-0.156129</td>
      <td>0.955853</td>
      <td>0.743295</td>
      <td>0.257176</td>
      <td>-0.515531</td>
      <td>-1.016628</td>
      <td>-1.563369</td>
    </tr>
    <tr>
      <th>365</th>
      <td>0.026000</td>
      <td>-1.051694</td>
      <td>-0.625321</td>
      <td>-0.568564</td>
      <td>-1.552451</td>
      <td>1.620431</td>
      <td>0.106097</td>
      <td>-0.981235</td>
      <td>-0.439462</td>
      <td>0.419300</td>
      <td>-1.544716</td>
      <td>-0.352502</td>
      <td>-1.095432</td>
      <td>-0.398370</td>
      <td>-1.479334</td>
      <td>-1.812168</td>
    </tr>
    <tr>
      <th>559</th>
      <td>1.258067</td>
      <td>-1.051694</td>
      <td>0.082340</td>
      <td>-0.020208</td>
      <td>1.225384</td>
      <td>0.713732</td>
      <td>-0.303555</td>
      <td>-0.835402</td>
      <td>-1.328435</td>
      <td>0.227491</td>
      <td>-1.211307</td>
      <td>-0.352502</td>
      <td>-1.095432</td>
      <td>0.095813</td>
      <td>-0.585599</td>
      <td>0.331517</td>
    </tr>
    <tr>
      <th>33</th>
      <td>-1.206066</td>
      <td>-1.051694</td>
      <td>-0.705522</td>
      <td>-1.665277</td>
      <td>0.617733</td>
      <td>0.922970</td>
      <td>0.788850</td>
      <td>-0.631235</td>
      <td>-1.328435</td>
      <td>1.074650</td>
      <td>-0.211079</td>
      <td>-1.448299</td>
      <td>-1.095432</td>
      <td>0.137871</td>
      <td>-0.752430</td>
      <td>-0.535557</td>
    </tr>
    <tr>
      <th>31</th>
      <td>-1.534617</td>
      <td>-1.051694</td>
      <td>-0.398869</td>
      <td>-1.586940</td>
      <td>0.444118</td>
      <td>-1.169411</td>
      <td>-1.669061</td>
      <td>-0.660402</td>
      <td>1.338485</td>
      <td>0.483237</td>
      <td>-0.711193</td>
      <td>0.743295</td>
      <td>0.257176</td>
      <td>0.510386</td>
      <td>0.165142</td>
      <td>1.822367</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-b9a38f3a-c937-4ffe-9177-993e40d577bd')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-b9a38f3a-c937-4ffe-9177-993e40d577bd button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-b9a38f3a-c937-4ffe-9177-993e40d577bd');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>





```python
# Pembuatan DataFrame untuk menyimpan hasil evaluasi model

hasil_evaluasi_df = pd.DataFrame(columns=["Model", "R2 Score", "Adjusted R2", "RMSE", "MAE", "MSE", "Explained Variance"])
hasil_evaluasi_df.head()
```





  <div id="df-b22fdb39-0e9a-4c32-b294-e9cceab466c8" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>R2 Score</th>
      <th>Adjusted R2</th>
      <th>RMSE</th>
      <th>MAE</th>
      <th>MSE</th>
      <th>Explained Variance</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-b22fdb39-0e9a-4c32-b294-e9cceab466c8')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-b22fdb39-0e9a-4c32-b294-e9cceab466c8 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-b22fdb39-0e9a-4c32-b294-e9cceab466c8');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>




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





  <div id="df-7951055c-15e8-4640-8565-3afba0cde354" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Weight (kg)</th>
      <th>Height (m)</th>
      <th>Max_BPM</th>
      <th>Avg_BPM</th>
      <th>Resting_BPM</th>
      <th>Session_Duration (hours)</th>
      <th>Calories_Burned</th>
      <th>Workout_Type</th>
      <th>Water_Intake (liters)</th>
      <th>Workout_Frequency (days/week)</th>
      <th>Experience_Level</th>
      <th>BMI</th>
      <th>Intensity_Score</th>
      <th>indeks_hr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.422343</td>
      <td>0.950847</td>
      <td>0.681493</td>
      <td>-0.098545</td>
      <td>0.010081</td>
      <td>0.922970</td>
      <td>-0.303555</td>
      <td>1.264598</td>
      <td>1.495690</td>
      <td>1.338485</td>
      <td>1.455967</td>
      <td>0.743295</td>
      <td>1.609784</td>
      <td>0.794278</td>
      <td>0.754222</td>
      <td>-0.486320</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.600965</td>
      <td>-1.051694</td>
      <td>0.049316</td>
      <td>-1.508604</td>
      <td>-0.076726</td>
      <td>0.504494</td>
      <td>0.515749</td>
      <td>0.127098</td>
      <td>-0.082284</td>
      <td>-0.439462</td>
      <td>-0.877898</td>
      <td>0.743295</td>
      <td>0.257176</td>
      <td>1.064652</td>
      <td>-0.200072</td>
      <td>-0.609901</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.548964</td>
      <td>-1.051694</td>
      <td>-0.271491</td>
      <td>-0.490228</td>
      <td>-1.118414</td>
      <td>-1.518142</td>
      <td>-1.122858</td>
      <td>-0.427068</td>
      <td>-0.838243</td>
      <td>-1.328435</td>
      <td>-0.544488</td>
      <td>0.743295</td>
      <td>0.257176</td>
      <td>-0.030361</td>
      <td>-0.034673</td>
      <td>0.765174</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.123928</td>
      <td>0.950847</td>
      <td>-0.974433</td>
      <td>-0.176881</td>
      <td>0.878155</td>
      <td>1.411193</td>
      <td>-0.849757</td>
      <td>-1.943735</td>
      <td>-1.370351</td>
      <td>0.449512</td>
      <td>-0.877898</td>
      <td>-0.352502</td>
      <td>-1.095432</td>
      <td>-0.976669</td>
      <td>-1.668821</td>
      <td>-0.078618</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.056137</td>
      <td>0.950847</td>
      <td>-1.309393</td>
      <td>0.528148</td>
      <td>0.704540</td>
      <td>0.992716</td>
      <td>0.788850</td>
      <td>-1.797902</td>
      <td>-1.282278</td>
      <td>0.449512</td>
      <td>0.289035</td>
      <td>-0.352502</td>
      <td>-1.095432</td>
      <td>-1.580503</td>
      <td>-1.656842</td>
      <td>-0.523715</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-7951055c-15e8-4640-8565-3afba0cde354')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-7951055c-15e8-4640-8565-3afba0cde354 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-7951055c-15e8-4640-8565-3afba0cde354');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>





```python
# Pembuatan DataFrame untuk menyimpan hasil evaluasi model

hasil_evaluasi_model = pd.DataFrame(columns=["Model", "R2 Score", "Adjusted R2", "RMSE", "MAE", "MSE", "Explained Variance"])
hasil_evaluasi_model.head()
```





  <div id="df-2c9b684c-32f4-4c65-9d04-0cebfe6365e8" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>R2 Score</th>
      <th>Adjusted R2</th>
      <th>RMSE</th>
      <th>MAE</th>
      <th>MSE</th>
      <th>Explained Variance</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-2c9b684c-32f4-4c65-9d04-0cebfe6365e8')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-2c9b684c-32f4-4c65-9d04-0cebfe6365e8 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-2c9b684c-32f4-4c65-9d04-0cebfe6365e8');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>

    </div>
  </div>




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




<style>#sk-container-id-1 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: #000;
  --sklearn-color-text-muted: #666;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-1 {
  color: var(--sklearn-color-text);
}

#sk-container-id-1 pre {
  padding: 0;
}

#sk-container-id-1 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-1 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-1 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-1 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-1 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-1 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-1 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-1 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-1 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-1 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-1 label.sk-toggleable__label {
  cursor: pointer;
  display: flex;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
  align-items: start;
  justify-content: space-between;
  gap: 0.5em;
}

#sk-container-id-1 label.sk-toggleable__label .caption {
  font-size: 0.6rem;
  font-weight: lighter;
  color: var(--sklearn-color-text-muted);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-1 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-1 div.sk-label label.sk-toggleable__label,
#sk-container-id-1 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-1 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-1 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-1 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-1 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 0.5em;
  text-align: center;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-1 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-1 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-1 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-1 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>RandomForestRegressor(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>RandomForestRegressor</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.RandomForestRegressor.html">?<span>Documentation for RandomForestRegressor</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></div></label><div class="sk-toggleable__content fitted"><pre>RandomForestRegressor(random_state=42)</pre></div> </div></div></div></div>



### K-Nearest Neighbors

`K-Nearest Neighbors (KNN)` adalah teknik analisis data yang sangat mudah dipahami dan tidak memerlukan tahap pelatihan yang kompleks. Metode ini bekerja dengan menentukan `k` data terdekat dengan titik data yang akan diprediksi melalui metrik jarak seperti Euclidean. Prediksi dihasilkan dari rata-rata atau mode dari `k` neighbor tersebut. `KNN` cocok untuk dataset kecil karena sifatnya yang sederhana dan transparan serta fleksibel terhadap berbagai distribusi data. Namun, algoritma ini kurang efisien pada dataset besar karena kompleksitas perhitungan jarak dan sensitif terhadap noise serta ketidakseimbangan data.

Untuk model `K-Nearest Neighbors`, diimplementasikan dengan jumlah `n_neighbors` sebesar 10.


```python
# Train model KNN
knn_model = KNeighborsRegressor(n_neighbors=10)
knn_model.fit(fitur_train, target_train)
```




<style>#sk-container-id-2 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: #000;
  --sklearn-color-text-muted: #666;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-2 {
  color: var(--sklearn-color-text);
}

#sk-container-id-2 pre {
  padding: 0;
}

#sk-container-id-2 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-2 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-2 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-2 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-2 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-2 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-2 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-2 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-2 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-2 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-2 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-2 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-2 label.sk-toggleable__label {
  cursor: pointer;
  display: flex;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
  align-items: start;
  justify-content: space-between;
  gap: 0.5em;
}

#sk-container-id-2 label.sk-toggleable__label .caption {
  font-size: 0.6rem;
  font-weight: lighter;
  color: var(--sklearn-color-text-muted);
}

#sk-container-id-2 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-2 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-2 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-2 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-2 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-2 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-2 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-2 div.sk-label label.sk-toggleable__label,
#sk-container-id-2 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-2 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-2 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-2 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-2 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-2 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-2 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-2 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 0.5em;
  text-align: center;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-2 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-2 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-2 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-2 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>KNeighborsRegressor(n_neighbors=10)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>KNeighborsRegressor</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.KNeighborsRegressor.html">?<span>Documentation for KNeighborsRegressor</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></div></label><div class="sk-toggleable__content fitted"><pre>KNeighborsRegressor(n_neighbors=10)</pre></div> </div></div></div></div>



### Support Vector Regressor
`Support Vector Regression (SVR)` adalah teknik analisis regresi yang menggunakan konsep dari `Support Vector Machine (SVM)` untuk memodelkan hubungan data. Dengan mencari `hyperplane` optimal dalam ruang berdimensi tinggi, SVR dapat memprediksi nilai target dengan efektif. Melalui penggunaan kernel seperti linear, polinomial, atau `RBF`, algoritma ini mampu menangani hubungan non-linear yang kompleks. `SVR` sangat efisien dalam menangani data berdimensi tinggi dan memiliki daya tahan terhadap noise. Namun, algoritma ini kurang efisien untuk dataset besar karena membutuhkan banyak perhitungan, dan hasilnya sulit diinterpretasi karena sangat bergantung pada pemilihan kernel dan parameter yang tepat seperti `C`, `epsilon`, dan `gamma`.

Untuk `Model Optimasi Pengeluaran Energi`, diimplementasikan dengan menggunakan `Support Vector Regression` yang dikonfigurasi dengan parameter standar. Spesifiknya, parameter `C` diatur ke 100 dan `epsilon` diatur ke 0.1 untuk meningkatkan akurasi prediksi dalam melakukan regresi.


```python
# Train Model SVR
svr_model = SVR(kernel='rbf', C=100, epsilon=0.1)
svr_model.fit(fitur_train, target_train)
```




<style>#sk-container-id-3 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: #000;
  --sklearn-color-text-muted: #666;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-3 {
  color: var(--sklearn-color-text);
}

#sk-container-id-3 pre {
  padding: 0;
}

#sk-container-id-3 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-3 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-3 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-3 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-3 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-3 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-3 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-3 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-3 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-3 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-3 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-3 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-3 label.sk-toggleable__label {
  cursor: pointer;
  display: flex;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
  align-items: start;
  justify-content: space-between;
  gap: 0.5em;
}

#sk-container-id-3 label.sk-toggleable__label .caption {
  font-size: 0.6rem;
  font-weight: lighter;
  color: var(--sklearn-color-text-muted);
}

#sk-container-id-3 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-3 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-3 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-3 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-3 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-3 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-3 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-3 div.sk-label label.sk-toggleable__label,
#sk-container-id-3 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-3 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-3 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-3 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-3 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-3 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-3 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-3 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 0.5em;
  text-align: center;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-3 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-3 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-3 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-3 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-3" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>SVR(C=100)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" checked><label for="sk-estimator-id-3" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>SVR</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.svm.SVR.html">?<span>Documentation for SVR</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></div></label><div class="sk-toggleable__content fitted"><pre>SVR(C=100)</pre></div> </div></div></div></div>



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

    Parameter Optimal: {'C': 1, 'epsilon': 0.5, 'gamma': 'scale'}
    Skor Terbaik: -0.2370920120332281



    
![png](output_121_1.png)
    


Berdasarkan hasil GridSearch, parameter model terbaik yang diperoleh adalah nilai C sama dengan 1, epsilon sebesar 0.5 dan nilai gamma dengan pengaturan 'scale'.


```python
# Mendefinisikan dan melatih model SVR dengan parameter terbaik
svr_reg = SVR(kernel='rbf', C=1, epsilon=0.5, gamma='scale')
svr_reg.fit(fitur_train, target_train)
```




<style>#sk-container-id-4 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: #000;
  --sklearn-color-text-muted: #666;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-4 {
  color: var(--sklearn-color-text);
}

#sk-container-id-4 pre {
  padding: 0;
}

#sk-container-id-4 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-4 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-4 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-4 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-4 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-4 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-4 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-4 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-4 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-4 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-4 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-4 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-4 label.sk-toggleable__label {
  cursor: pointer;
  display: flex;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
  align-items: start;
  justify-content: space-between;
  gap: 0.5em;
}

#sk-container-id-4 label.sk-toggleable__label .caption {
  font-size: 0.6rem;
  font-weight: lighter;
  color: var(--sklearn-color-text-muted);
}

#sk-container-id-4 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-4 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-4 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-4 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-4 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-4 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-4 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-4 div.sk-label label.sk-toggleable__label,
#sk-container-id-4 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-4 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-4 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-4 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-4 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-4 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-4 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-4 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 0.5em;
  text-align: center;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-4 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-4 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-4 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-4 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-4" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>SVR(C=1, epsilon=0.5)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-4" type="checkbox" checked><label for="sk-estimator-id-4" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>SVR</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.svm.SVR.html">?<span>Documentation for SVR</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></div></label><div class="sk-toggleable__content fitted"><pre>SVR(C=1, epsilon=0.5)</pre></div> </div></div></div></div>



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

    
    Model Performance (RF):
                               0
    Model                     RF
    R2 Score            0.902046
    Adjusted R2         0.887641
    RMSE                0.300591
    MAE                 0.235834
    MSE                 0.090355
    Explained Variance  0.907891



    
![png](output_132_1.png)
    


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

    Fitting 5 folds for each of 80 candidates, totalling 400 fits


    Best Parameters (KNN): {'metric': 'euclidean', 'n_neighbors': 4, 'weights': 'distance'}
    
    Model Performance (KNN Tuned & Scaled):
                                           0
    Model               KNN (Tuned & Scaled)
    R2 Score                        0.822085
    Adjusted R2                     0.795921
    RMSE                            0.405109
    MAE                              0.32197
    MSE                             0.164113
    Explained Variance              0.833304



    
![png](output_135_2.png)
    


Model ini tidak sebagus model sebelumnya namun masih cukup bagus di Adjusted Rsquared sebesar 0.8365 dan R2 Score sebesar 0.822085, sementara untuk nilai MSE di atas 0.1 yaitu 0.164113 pada model ini.

### SVR


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error,
    explained_variance_score
)

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

    
    Model Performance (SVR Tuned & Scaled):
                                           0
    Model               SVR (Tuned & Scaled)
    R2 Score                        0.888236
    Adjusted R2                     0.871801
    RMSE                            0.321082
    MAE                             0.242121
    MSE                             0.103094
    Explained Variance              0.889767



    
![png](output_138_1.png)
    


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

                      Model  R2 Score  Adjusted R2      RMSE       MAE       MSE  \
    0                    RF  0.902046     0.887641  0.300591  0.235834  0.090355   
    1  KNN (Tuned & Scaled)  0.822085     0.795921  0.405109  0.321970  0.164113   
    2  SVR (Tuned & Scaled)  0.888236     0.871801  0.321082  0.242121  0.103094   
    
       Explained Variance  
    0            0.907891  
    1            0.833304  
    2            0.889767  



    
![png](output_141_1.png)
    


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

    
    Evaluasi Performa Model (Random Forest):
                                    0
    Model               Random Forest
    R2 Score                 0.902046
    Adjusted R2              0.887641
    RMSE                     0.300591
    MAE                      0.235834
    MSE                      0.090355
    Explained Variance       0.907891



    
![png](output_145_1.png)
    


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
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # garis diagonal ideal
plt.title("Prediksi vs Nilai Aktual (KNN)")
plt.xlabel("Aktual")
plt.ylabel("Prediksi")
plt.grid(True)
plt.show()
```

    
    Evaluasi Kinerja Model (KNN):
                                          0
    Model               K-Nearest Neighbors
    R2 Score                       0.822085
    Adjusted R2                    0.795921
    RMSE                           0.405109
    MAE                             0.32197
    MSE                            0.164113
    Explained Variance             0.833304



    
![png](output_148_1.png)
    


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

    
    Evaluasi Model SVR:
                                                0
    Model               Support Vector Regression
    R2 Score                             0.888236
    Adjusted R2                          0.871801
    RMSE                                 0.321082
    MAE                                  0.242121
    MSE                                  0.103094
    Explained Variance                   0.889767



    
![png](output_151_1.png)
    


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


    
![png](output_154_0.png)
    


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

# Akhir


```python
# Instalasi nbconvert jika belum tersedia
!pip install -q nbconvert

# Konversi notebook ke markdown, hasil file akan disimpan di /content
!jupyter nbconvert --to markdown /content/gambar.ipynb --output-dir=/content

# Kompres folder output bernama "gambar_files" menjadi zip di /content
!zip -r /content/gambar_files.zip /content/gambar_files
```

    [NbConvertApp] WARNING | pattern '/content/gambar.ipynb' matched no files
    This application is used to convert notebook files (*.ipynb)
            to various other formats.
    
            WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.
    
    Options
    =======
    The options below are convenience aliases to configurable class-options,
    as listed in the "Equivalent to" description-line of the aliases.
    To see all configurable class-options for some <cmd>, use:
        <cmd> --help-all
    
    --debug
        set log level to logging.DEBUG (maximize logging output)
        Equivalent to: [--Application.log_level=10]
    --show-config
        Show the application's configuration (human-readable format)
        Equivalent to: [--Application.show_config=True]
    --show-config-json
        Show the application's configuration (json format)
        Equivalent to: [--Application.show_config_json=True]
    --generate-config
        generate default config file
        Equivalent to: [--JupyterApp.generate_config=True]
    -y
        Answer yes to any questions instead of prompting.
        Equivalent to: [--JupyterApp.answer_yes=True]
    --execute
        Execute the notebook prior to export.
        Equivalent to: [--ExecutePreprocessor.enabled=True]
    --allow-errors
        Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.
        Equivalent to: [--ExecutePreprocessor.allow_errors=True]
    --stdin
        read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'
        Equivalent to: [--NbConvertApp.from_stdin=True]
    --stdout
        Write notebook output to stdout instead of files.
        Equivalent to: [--NbConvertApp.writer_class=StdoutWriter]
    --inplace
        Run nbconvert in place, overwriting the existing notebook (only
                relevant when converting to notebook format)
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory=]
    --clear-output
        Clear output of current file and save in place,
                overwriting the existing notebook.
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --ClearOutputPreprocessor.enabled=True]
    --coalesce-streams
        Coalesce consecutive stdout and stderr outputs into one stream (within each cell).
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --CoalesceStreamsPreprocessor.enabled=True]
    --no-prompt
        Exclude input and output prompts from converted document.
        Equivalent to: [--TemplateExporter.exclude_input_prompt=True --TemplateExporter.exclude_output_prompt=True]
    --no-input
        Exclude input cells and output prompts from converted document.
                This mode is ideal for generating code-free reports.
        Equivalent to: [--TemplateExporter.exclude_output_prompt=True --TemplateExporter.exclude_input=True --TemplateExporter.exclude_input_prompt=True]
    --allow-chromium-download
        Whether to allow downloading chromium if no suitable version is found on the system.
        Equivalent to: [--WebPDFExporter.allow_chromium_download=True]
    --disable-chromium-sandbox
        Disable chromium security sandbox when converting to PDF..
        Equivalent to: [--WebPDFExporter.disable_sandbox=True]
    --show-input
        Shows code input. This flag is only useful for dejavu users.
        Equivalent to: [--TemplateExporter.exclude_input=False]
    --embed-images
        Embed the images as base64 dataurls in the output. This flag is only useful for the HTML/WebPDF/Slides exports.
        Equivalent to: [--HTMLExporter.embed_images=True]
    --sanitize-html
        Whether the HTML in Markdown cells and cell outputs should be sanitized..
        Equivalent to: [--HTMLExporter.sanitize_html=True]
    --log-level=<Enum>
        Set the log level by value or name.
        Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
        Default: 30
        Equivalent to: [--Application.log_level]
    --config=<Unicode>
        Full path of a config file.
        Default: ''
        Equivalent to: [--JupyterApp.config_file]
    --to=<Unicode>
        The export format to be used, either one of the built-in formats
                ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf']
                or a dotted object name that represents the import path for an
                ``Exporter`` class
        Default: ''
        Equivalent to: [--NbConvertApp.export_format]
    --template=<Unicode>
        Name of the template to use
        Default: ''
        Equivalent to: [--TemplateExporter.template_name]
    --template-file=<Unicode>
        Name of the template file to use
        Default: None
        Equivalent to: [--TemplateExporter.template_file]
    --theme=<Unicode>
        Template specific theme(e.g. the name of a JupyterLab CSS theme distributed
        as prebuilt extension for the lab template)
        Default: 'light'
        Equivalent to: [--HTMLExporter.theme]
    --sanitize_html=<Bool>
        Whether the HTML in Markdown cells and cell outputs should be sanitized.This
        should be set to True by nbviewer or similar tools.
        Default: False
        Equivalent to: [--HTMLExporter.sanitize_html]
    --writer=<DottedObjectName>
        Writer class used to write the
                                            results of the conversion
        Default: 'FilesWriter'
        Equivalent to: [--NbConvertApp.writer_class]
    --post=<DottedOrNone>
        PostProcessor class used to write the
                                            results of the conversion
        Default: ''
        Equivalent to: [--NbConvertApp.postprocessor_class]
    --output=<Unicode>
        Overwrite base name use for output files.
                    Supports pattern replacements '{notebook_name}'.
        Default: '{notebook_name}'
        Equivalent to: [--NbConvertApp.output_base]
    --output-dir=<Unicode>
        Directory to write output(s) to. Defaults
                                      to output to the directory of each notebook. To recover
                                      previous default behaviour (outputting to the current
                                      working directory) use . as the flag value.
        Default: ''
        Equivalent to: [--FilesWriter.build_directory]
    --reveal-prefix=<Unicode>
        The URL prefix for reveal.js (version 3.x).
                This defaults to the reveal CDN, but can be any url pointing to a copy
                of reveal.js.
                For speaker notes to work, this must be a relative path to a local
                copy of reveal.js: e.g., "reveal.js".
                If a relative path is given, it must be a subdirectory of the
                current directory (from which the server is run).
                See the usage documentation
                (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow)
                for more details.
        Default: ''
        Equivalent to: [--SlidesExporter.reveal_url_prefix]
    --nbformat=<Enum>
        The nbformat version to write.
                Use this to downgrade notebooks.
        Choices: any of [1, 2, 3, 4]
        Default: 4
        Equivalent to: [--NotebookExporter.nbformat_version]
    
    Examples
    --------
    
        The simplest way to use nbconvert is
    
                > jupyter nbconvert mynotebook.ipynb --to html
    
                Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf'].
    
                > jupyter nbconvert --to latex mynotebook.ipynb
    
                Both HTML and LaTeX support multiple output templates. LaTeX includes
                'base', 'article' and 'report'.  HTML includes 'basic', 'lab' and
                'classic'. You can specify the flavor of the format used.
    
                > jupyter nbconvert --to html --template lab mynotebook.ipynb
    
                You can also pipe the output to stdout, rather than a file
    
                > jupyter nbconvert mynotebook.ipynb --stdout
    
                PDF is generated via latex
    
                > jupyter nbconvert mynotebook.ipynb --to pdf
    
                You can get (and serve) a Reveal.js-powered slideshow
    
                > jupyter nbconvert myslides.ipynb --to slides --post serve
    
                Multiple notebooks can be given at the command line in a couple of
                different ways:
    
                > jupyter nbconvert notebook*.ipynb
                > jupyter nbconvert notebook1.ipynb notebook2.ipynb
    
                or you can specify the notebooks list in a config file, containing::
    
                    c.NbConvertApp.notebooks = ["my_notebook.ipynb"]
    
                > jupyter nbconvert --config mycfg.py
    
    To see all available configurables, use `--help-all`.
    


    	zip warning: name not matched: /content/gambar_files
    
    zip error: Nothing to do! (try: zip -r /content/gambar_files.zip . -i /content/gambar_files)


# Referensi

- Gough, A., et al. (2018). Personalized Fitness: Trends in the Digital Fitness Industry. *Journal of Health & Wellness*.

- McAuley, E., et al. (2011). Social Support and Self-Efficacy in Exercise. *Health Psychology*.

- World Health Organization. (2020). *Physical Activity*. Retrieved from [WHO](https://www.who.int/news-room/fact-sheets/detail/physical-activity).

- Tan, J. S. A., Che Embi, Z., & Hashim, N. (2024). Comparison of Machine Learning Methods for Calories Burn Prediction. *Journal of Informatics and Web Engineering*, 3(1), 182-191. [https://doi.org/10.33093/jiwe.2024.3.1.12](https://doi.org/10.33093/jiwe.2024.3.1.12)

- Kadam, A., Shrivastava, A., Pawar, S. K., Patil, V. H., Michaelson, J., & Singh, A. (n.d.). *Calories Burned Prediction Using Machine Learning*. IEEE. Retrieved from [Calories Burn Prediction](https://hossainlab.github.io/projects/Calories_Burnt/02_Calories%20Burnt%20Prediction.html)

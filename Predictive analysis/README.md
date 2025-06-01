
# Laporan Proyek Machine Learning - Sandy Tirta Yudha

## Domain Proyek

Meningkatkan efektivitas latihan di pusat kebugaran telah menjadi perhatian utama dalam mendukung kesehatan masyarakat masa kini, khususnya terkait efisiensi dalam membakar kalori. Memahami secara mendalam jenis-jenis aktivitas yang mampu membakar kalori secara optimal tidak hanya penting bagi individu yang ingin mencapai target kebugaran pribadi, tetapi juga berdampak besar pada kesehatan populasi secara umum. Berdasarkan data dari World Health Organization (WHO, 2020), aktivitas fisik yang cukup berperan penting dalam menurunkan risiko berbagai penyakit kronis. Sayangnya, sebagian besar penduduk dunia masih belum mencapai standar aktivitas fisik yang dianjurkan. Terbatasnya waktu dalam kehidupan modern memperumit situasi ini, sehingga diperlukan pemahaman yang lebih komprehensif mengenai efektivitas berbagai jenis latihan dalam mengoptimalkan pembakaran kalori dalam durasi yang terbatas.

Gough et al. (2018) menemukan bahwa masyarakat kini semakin cenderung memilih program latihan yang mampu memberikan hasil maksimal dengan durasi yang lebih singkat. Pergeseran ini mencerminkan kebutuhan akan efisiensi dalam berolahraga, terutama di tengah keterbatasan waktu yang dihadapi banyak orang di era modern. Oleh karena itu, penting untuk mengetahui jenis latihan yang paling efektif dalam membakar kalori dalam waktu yang terbatas. Selain faktor efisiensi, aspek psikososial juga berperan penting dalam keberhasilan program kebugaran. McAuley et al. (2011) menyoroti bahwa motivasi, rasa percaya diri, dan dukungan sosial berkontribusi besar terhadap seberapa intens dan konsisten seseorang menjalani latihan. Dengan demikian, efektivitas latihan tidak hanya ditentukan oleh faktor fisik semata, tetapi juga oleh kondisi mental dan sosial yang menyertainya.

Dalam skala kesehatan masyarakat secara keseluruhan, memahami seberapa efektif berbagai jenis latihan gym dalam membakar kalori memiliki peran strategis dalam merancang intervensi kesehatan yang lebih tepat sasaran. Hal ini menjadi semakin penting seiring dengan meningkatnya kasus penyakit akibat gaya hidup pasif, seperti obesitas, diabetes tipe 2, dan gangguan jantung. Dengan memanfaatkan wawasan mengenai efektivitas tiap jenis latihan, program kebugaran dapat disusun secara lebih optimal guna menyesuaikan dengan keterbatasan waktu dan sumber daya yang sering dihadapi oleh masyarakat saat ini. Oleh karena itu, penelitian yang mendalami efisiensi pembakaran kalori dalam aktivitas kebugaran bukan hanya berguna untuk meningkatkan hasil latihan individu, tetapi juga berkontribusi dalam mendukung kebijakan kesehatan publik yang bertujuan menurunkan prevalensi penyakit kronis.

Pemanfaatan algoritma machine learning memungkinkan analisis dan identifikasi aktivitas gym yang paling efisien dalam mendukung tujuan kebugaran. Beberapa algoritma yang digunakan antara lain k-Nearest Neighbors (KNN), Random Forest, dan Boosting. Algoritma KNN mampu memberikan saran jenis latihan yang sesuai dengan profil dan karakteristik masing-masing individu. Sementara itu, Random Forest memproses berbagai variabel untuk menghasilkan prediksi yang lebih akurat terkait jumlah kalori yang terbakar. Di sisi lain, Boosting terus menyempurnakan hasil prediksi dengan mempelajari pola kesalahan sebelumnya, sehingga meningkatkan akurasi model secara keseluruhan. Melalui pendekatan ini, pusat kebugaran dapat menyediakan rekomendasi latihan yang bersifat personal, membantu individu mencapai target kebugaran mereka secara lebih efektif, serta mendorong gaya hidup sehat secara luas dalam masyarakat. Data yang digunakan diambil dari kaggle yang bisa diakses dari link [Berikut](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data).

Dataset ini menyediakan informasi menyeluruh mengenai kondisi fisik individu yang berlatih di pusat kebugaran. Data mencakup elemen demografis seperti `Usia` dan `jenis_kelamin`, serta indikator komposisi tubuh seperti `berat_badan`, `tinggi_badan`, `BMI`, dan `persentase_lemak`. Selain itu, terdapat juga metrik kebugaran jantung seperti `Max_BPM`, `Avg_BPM`, dan `esting_BPM`. Nilai `BMI` dan `persentase_lemak` digunakan untuk mengidentifikasi komposisi tubuh, di mana `persentase_lemak` dianggap lebih akurat dalam menilai kadar lemak tubuh, khususnya pada individu dengan otot yang dominan.

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

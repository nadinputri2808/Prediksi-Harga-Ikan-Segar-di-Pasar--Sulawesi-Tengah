# =====================================================
# PREDIKSI HARGA IKAN SEGAR DI SULAWESI TENGAH
# METODE : REGRESI LINEAR BERGANDA
# =====================================================

# 1. IMPORT LIBRARY
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =====================================================
# 2. MEMBACA DATASET
# =====================================================

df = pd.read_csv("dataset_harga_ikan_sulteng.csv")

print("5 Data Pertama")
print(df.head())

print("\nInformasi Dataset")
print(df.info())

print("\nStatistik Deskriptif")
print(df.describe())

# =====================================================
# 3. VISUALISASI DATA
# =====================================================

plt.figure(figsize=(8,5))
sns.histplot(df["Harga_Rp"], bins=15, kde=True)
plt.title("Distribusi Harga Ikan")
plt.xlabel("Harga (Rp)")
plt.ylabel("Frekuensi")
plt.show()

# =====================================================
# 4. MENENTUKAN FITUR DAN TARGET
# =====================================================

X = df.drop(["Harga_Rp", "Kategori_Harga"], axis=1)
y = df["Harga_Rp"]

# =====================================================
# 5. IDENTIFIKASI KOLOM KATEGORIK
# =====================================================

categorical_features = [
    'Jenis_Ikan',
    'Cuaca',
    'Stok',
    'Permintaan',
    'Lokasi_Pasar'
]

numerical_features = ['Berat_Kg']

# =====================================================
# 6. PREPROCESSING
# =====================================================

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ],
    remainder='passthrough'
)

# =====================================================
# 7. MEMBANGUN MODEL REGRESI
# =====================================================

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regression', LinearRegression())
])

# =====================================================
# 8. SPLIT DATA TRAINING DAN TESTING
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# 9. TRAINING MODEL
# =====================================================

model.fit(X_train, y_train)

# =====================================================
# 10. PREDIKSI
# =====================================================

y_pred = model.predict(X_test)

# =====================================================
# 11. EVALUASI MODEL
# =====================================================

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)

print("\nHASIL EVALUASI MODEL")
print("MAE  :", round(mae,2))
print("RMSE :", round(rmse,2))
print("R²   :", round(r2,4))

# =====================================================
# 12. TABEL HASIL PREDIKSI
# =====================================================

hasil = pd.DataFrame({
    'Harga Aktual': y_test,
    'Harga Prediksi': y_pred
})

print("\nPerbandingan Aktual dan Prediksi")
print(hasil.head(10))

# =====================================================
# 13. GRAFIK AKTUAL VS PREDIKSI
# =====================================================

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color='red'
)

plt.xlabel("Harga Aktual")
plt.ylabel("Harga Prediksi")
plt.title("Aktual vs Prediksi Harga Ikan")
plt.show()

# =====================================================
# 14. ANALISIS KOEFISIEN REGRESI
# =====================================================

ohe = model.named_steps['preprocessor']

feature_names = (
    ohe.named_transformers_['cat']
    .get_feature_names_out(categorical_features)
)

feature_names = list(feature_names)
feature_names.append("Berat_Kg")

coef = model.named_steps['regression'].coef_

coef_df = pd.DataFrame({
    "Variabel": feature_names,
    "Koefisien": coef
})

coef_df = coef_df.sort_values(
    by="Koefisien",
    ascending=False
)

print("\nKoefisien Regresi")
print(coef_df)

# =====================================================
# 15. VISUALISASI PENGARUH VARIABEL
# =====================================================

plt.figure(figsize=(12,8))

sns.barplot(
    data=coef_df.head(15),
    x="Koefisien",
    y="Variabel"
)

plt.title("15 Variabel Paling Berpengaruh")
plt.show()

# =====================================================
# 16. CONTOH PREDIKSI DATA BARU
# =====================================================

data_baru = pd.DataFrame({
    'Jenis_Ikan':['Tuna'],
    'Berat_Kg':[8],
    'Cuaca':['Cerah'],
    'Stok':['Sedikit'],
    'Permintaan':['Tinggi'],
    'Lokasi_Pasar':['Palu']
})

prediksi_harga = model.predict(data_baru)

print("\nPrediksi Harga Ikan Baru")
print("Rp {:,.0f}".format(prediksi_harga[0]))
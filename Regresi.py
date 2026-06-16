# ==========================================
# IMPORT LIBRARY
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================
# MEMBACA DATA
# ==========================================

df = pd.read_csv('penerima_manfaat_bersih.csv', encoding='latin1')

# Melihat data awal
print("5 Data Pertama")
print(df.head())

print("\nNama Kolom:")
print(df.columns)

# ==========================================
# MENGHAPUS BARIS TOTAL (JIKA ADA)
# ==========================================

df = df.dropna()

# ==========================================
# MENGUBAH KOLOM NUMERIK
# ==========================================

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

# ==========================================
# MENENTUKAN FITUR DAN TARGET
# ==========================================

X = df.iloc[:, 1:4]

y = df.iloc[:, 4]

# ==========================================
# SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# MEMBUAT MODEL
# ==========================================

model = LinearRegression()

model.fit(X_train, y_train)

# ==========================================
# PREDIKSI
# ==========================================

y_pred = model.predict(X_test)

# ==========================================
# EVALUASI MODEL
# ==========================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nHASIL EVALUASI")
print("MAE  =", mae)
print("MSE  =", mse)
print("RMSE =", rmse)
print("R²   =", r2)

# ==========================================
# KOEFISIEN REGRESI
# ==========================================

print("\nKoefisien Regresi")

for fitur, coef in zip(X.columns, model.coef_):
    print(f"{fitur}: {coef}")

print("Intercept:", model.intercept_)

# ==========================================
# VISUALISASI 1
# AKTUAL VS PREDIKSI
# ==========================================

plt.figure(figsize=(8,5))

plt.scatter(y_test, y_pred)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)

plt.xlabel("Nilai Aktual")
plt.ylabel("Nilai Prediksi")
plt.title("Aktual vs Prediksi")

plt.show()

# ==========================================
# VISUALISASI 2
# PENGARUH MASING-MASING VARIABEL
# ==========================================

importance = pd.DataFrame({
    'Variabel': X.columns,
    'Koefisien': model.coef_
})

plt.figure(figsize=(8,5))

plt.bar(
    importance['Variabel'],
    importance['Koefisien']
)

plt.xlabel("Variabel")
plt.ylabel("Koefisien")
plt.title("Pengaruh Variabel terhadap Realisasi Anggaran")

plt.show()

# ==========================================
# VISUALISASI 3
# REALISASI VS PREDIKSI
# ==========================================

hasil = pd.DataFrame({
    'Aktual': y_test,
    'Prediksi': y_pred
})

hasil = hasil.reset_index(drop=True)

plt.figure(figsize=(10,5))

plt.plot(hasil['Aktual'], marker='o', label='Aktual')
plt.plot(hasil['Prediksi'], marker='s', label='Prediksi')

plt.title('Perbandingan Aktual dan Prediksi')
plt.xlabel('Data')
plt.ylabel('Nilai')

plt.legend()

plt.show()
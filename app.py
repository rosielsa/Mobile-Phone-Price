import streamlit as st
import pandas as pd
import joblib

# Load model yang sudah disimpan
model = joblib.load('mobilephoneprice.pkl')

# Judul aplikasi
st.title('Prediksi Kategori Harga Smartphone')

# Deskripsi aplikasi
st.write("Masukkan spesifikasi smartphone di bawah ini untuk memprediksi kategori harganya:")

# Form inputan data dari user
new_battery_power = st.number_input("Kapasitas baterai (mAh)", min_value=500.0, max_value=2000.0, value=1000.0)
new_fc = st.number_input("Kamera depan (MP)", min_value=0.0, max_value=20.0, value=5.0)
new_pc = st.number_input("Kamera belakang (MP)", min_value=0.0, max_value=20.0, value=10.0)
new_ram = st.number_input("RAM (MB)", min_value=256.0, max_value=4000.0, value=2000.0)
new_int_memory = st.number_input("Memori Internal (GB)", min_value=2.0, max_value=64.0, value=32.0)

# Tombol prediksi
if st.button('Prediksi Harga'):
    # Buat DataFrame dari input
    new_data_df = pd.DataFrame(
        [[new_battery_power, new_fc, new_pc, new_ram, new_int_memory]],
        columns=['battery_power', 'fc', 'pc', 'ram', 'int_memory']
    )

    # Prediksi harga
    predicted_code = model.predict(new_data_df)[0]

    # Mapping hasil prediksi ke label harga
    label_mapping = {0: 'Murah', 1: 'Menengah', 2: 'Mahal', 3: 'Premium'}
    predicted_label = label_mapping.get(predicted_code, 'Tidak diketahui')

    # Tampilkan hasil
    st.success(f"Prediksi kategori harga smartphone adalah: **{predicted_label}**")

import streamlit as st
import pandas as pd 
import numpy as np
import datetime

# Judul Aplikasi
st.image("Pentachem.jpg")
st.title("Absensi Karyawan")
st.header("PT. PENTA CHEMICALS INDONESIA")
st.header("Supply Chain Departement")
st.text("JI. Industri Selatan 1. Blok OO No.3G & KK No.5A. Kawasan Industri JABABEKA Phase II")

# Fungsi untuk menyimpan data ke CSV
def save_data(df):
    df.to_csv('absensi.csv', mode='w', header=False, index=False)

# Formulir untuk mencatat kehadiran
with st.form(key='absensi_form'):
    nama = st.text_input("Nama Karyawan")
    tanggal_masuk = st.date_input("Tanggal Masuk", datetime.date.today())
    tanggal_pulang = st.date_input("Tanggal Pulang", datetime.date.today())
    hadir = st.radio("Status Kehadiran", ('Hadir', 'Tidak Hadir', 'Ijin', 'Sakit', 'Cuti'))

    # Input jam masuk
    jam_masuk = st.time_input("Jam Masuk", datetime.time(8, 0))  # Default jam masuk jam 8 pagi
    
    # Input jam pulang
    jam_pulang = st.time_input("Jam Pulang", datetime.time(17, 0))  # Default jam pulang jam 5 sore
    
    # Menghitung durasi lembur
    jam_masuk_dt = datetime.datetime.combine(datetime.date.today(), jam_masuk)
    jam_pulang_dt = datetime.datetime.combine(datetime.date.today(), jam_pulang)
    
    # Menghitung jam lembur (jika jam pulang lebih dari jam 17:00)
    lembur = max(0, (jam_pulang_dt - jam_masuk_dt).seconds / 3600 - 9)  # Menghitung lembur jika lebih dari 9 jam kerja
    keterangan_lembur = st.text_input("Keterangan Lembur:")

    submit_button = st.form_submit_button(label='Kirim')

    if submit_button:
        # Menyimpan data ke dalam DataFrame
        data = {
            'Nama': [nama],
            'Tanggal Masuk': [tanggal_masuk],
            'Tanggal Pulang': [tanggal_pulang],
            'Kehadiran': [hadir],
            'Jam Masuk': [jam_masuk],
            'Jam Pulang': [jam_pulang],
            'Durasi Lembur (jam)': [lembur],
            'Keterangan Lembur': keterangan_lembur
        }
        df = pd.DataFrame(data)

        # Menyimpan ke file CSV
        try:
            existing_data = pd.read_csv('absensi.csv', names=['Nama', 'Tanggal Masuk', 'Tanggal Pulang', 'Kehadiran', 'Jam Masuk', 'Jam Pulang', 'Durasi Lembur (jam)', 'Keterangan Lembur'])
            df = pd.concat([existing_data, df], ignore_index=True)
        except FileNotFoundError:
            pass  # Jika file tidak ada, kita akan membuat file baru

        save_data(df)
        st.success("Data absensi berhasil disimpan!")

# Menampilkan data absensi
st.subheader("Data Absensi")
try:
    absensi_data = pd.read_csv('absensi.csv', names=['Nama', 'Tanggal Masuk', 'Tanggal Pulang', 'Kehadiran', 'Jam Masuk', 'Jam Pulang', 'Durasi Lembur (jam)', 'Keterangan Lembur'])
    st.write(absensi_data)

    # Fitur Koreksi Data
    st.subheader("Koreksi Data Absensi")
    index_to_edit = st.selectbox("Pilih entri untuk dikoreksi", absensi_data.index)

    if st.button("Edit"):
        selected_row = absensi_data.iloc[index_to_edit]
        new_nama = st.text_input("Nama Karyawan", value=selected_row['Nama'])
        new_tanggal_masuk = st.date_input("Tanggal Masuk", value=pd.to_datetime(selected_row['Tanggal Masuk']))
        new_tanggal_pulang = st.date_input("Tanggal Pulang", value=pd.to_datetime(selected_row['Tanggal Pulang']))
        new_hadir = st.radio("Status Kehadiran", ('Hadir', 'Tidak Hadir', 'Ijin', 'Sakit', 'Cuti'), index=['Hadir', 'Tidak Hadir', 'Ijin', 'Sakit', 'Cuti'].index(selected_row['Kehadiran']))
        new_jam_masuk = st.time_input("Jam Masuk", value=pd.to_datetime(selected_row['Jam Masuk']).time())
        new_jam_pulang = st.time_input("Jam Pulang", value=pd.to_datetime(selected_row['Jam Pulang']).time())

    # Menghitung durasi lembur baru
    new_jam_masuk_dt = datetime.datetime.combine(datetime.date.today(), new_jam_masuk)
    new_jam_pulang_dt = datetime.datetime.combine(datetime.date.today(), new_jam_pulang)
    new_lembur = max(0, (new_jam_pulang_dt - new_jam_masuk_dt).seconds / 3600 - 9)

    if st.button("Simpan Perubahan"):
        # Memperbarui DataFrame dengan nilai baru
        absensi_data.at[index_to_edit, 'Nama'] = new_nama
        absensi_data.at[index_to_edit, 'Tanggal Masuk'] = new_tanggal_masuk
        absensi_data.at[index_to_edit, 'Tanggal Pulang'] = new_tanggal_pulang
        absensi_data.at[index_to_edit, 'Kehadiran'] = new_hadir
        absensi_data.at[index_to_edit, 'Jam Masuk'] = new_jam_masuk
        absensi_data.at[index_to_edit, 'Jam Pulang'] = new_jam_pulang
        absensi_data.at[index_to_edit, 'Durasi Lembur (jam)'] = new_lembur

        # Menyimpan kembali ke file CSV
        save_data(absensi_data)
        st.success("Perubahan berhasil disimpan!")
        
        # Fitur untuk mengunduh data ke CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Unduh Data Absensi",
            data=csv,
            file_name='absensi_data.csv',
            mime='text/csv',
        )

except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat data absensi: {e}")

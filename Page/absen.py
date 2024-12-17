import csv
from datetime import datetime
import streamlit as st

def tampilkan_menu():
    print("=== Aplikasi Absensi ===")
    print("1. Absen Masuk")
    print("2. Absen Keluar")
    print("3. Lihat Daftar Absensi")
    print("4. Keluar")

def absen_masuk(nama):
    waktu_masuk = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('absensi.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, waktu_masuk, "Masuk"])
    print(f"{nama} telah absen masuk pada {waktu_masuk}")

def absen_keluar(nama):
    waktu_keluar = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('absensi.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, waktu_keluar, "Keluar"])
    print(f"{nama} telah absen keluar pada {waktu_keluar}")

def lihat_absensi():
    try:
        with open('absensi.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nDaftar Absensi:")
            for row in reader:
                print(f"Nama: {row[0]}, Waktu: {row[1]}, Tipe: {row[2]}")
    except FileNotFoundError:
        print("Belum ada data absensi.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama: ")
            absen_masuk(nama)
        elif pilihan == '2':
            nama = input("Masukkan nama: ")
            absen_keluar(nama)
        elif pilihan == '3':
            lihat_absensi()
        elif pilihan == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import streamlit as st

class AplikasiAbsensi:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Absensi")
        
        # Label dan Entry untuk Nama
        self.label_nama = tk.Label(root, text="Nama:")
        self.label_nama.pack(pady=10)
        
        self.entry_nama = tk.Entry(root)
        self.entry_nama.pack(pady=10)
        
        # Tombol Absen Masuk
        self.btn_absen_masuk = tk.Button(root, text="Absen Masuk", command=self.absen_masuk)
        self.btn_absen_masuk.pack(pady=5)
        
        # Tombol Absen Keluar
        self.btn_absen_keluar = tk.Button(root, text="Absen Keluar", command=self.absen_keluar)
        self.btn_absen_keluar.pack(pady=5)
        
        # Tombol Lihat Daftar Absensi
        self.btn_lihat_absensi = tk.Button(root, text="Lihat Daftar Absensi", command=self.lihat_absensi)
        self.btn_lihat_absensi.pack(pady=5)
        
        # Tombol Keluar
        self.btn_keluar = tk.Button(root, text="Keluar", command=root.quit)
        self.btn_keluar.pack(pady=5)

    def absen_masuk(self):
        nama = self.entry_nama.get()
        if nama:
            waktu_masuk = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('absensi.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nama, waktu_masuk, "Masuk"])
            messagebox.showinfo("Info", f"{nama} telah absen masuk pada {waktu_masuk}")
            self.entry_nama.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")

    def absen_keluar(self):
        nama = self.entry_nama.get()
        if nama:
            waktu_keluar = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('absensi.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nama, waktu_keluar, "Keluar"])
            messagebox.showinfo("Info", f"{nama} telah absen keluar pada {waktu_keluar}")
            self.entry_nama.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")

    def lihat_absensi(self):
        try:
            with open('absensi.csv', mode='r') as file:
                reader = csv.reader(file)
                absensi = "\n".join([f"Nama: {row[0]}, Waktu: {row[1]}, Tipe: {row[2]}" for row in reader])
                messagebox.showinfo("Daftar Absensi", absensi)
        except FileNotFoundError:
            messagebox.showwarning("Peringatan", "Belum ada data absensi.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiAbsensi(root)
    root.mainloop()
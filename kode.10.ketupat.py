# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com


# Menginput diagonal dan sisi
diago1 = float(input('Tulis Diagonal 1 : '))
diago2 = float(input('Tulis Diagonal 2 : '))
sisi = float(input('Tulis Sisi  : '))

# Hitung Luas dan Keliling layang-layang
luas = (diago1 * diago2) / 2 
keliling = 4*sisi

#Menampilkan Hasil Perhitungan
print('Luas Belah Ketupat adalah %0.2f' %luas)
print('keliling Belah Ketupat adalah %0.2f' %keliling)

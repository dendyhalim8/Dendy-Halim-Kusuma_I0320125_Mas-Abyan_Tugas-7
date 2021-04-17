teks = "soal 1 : menggunakan fungsi string"
print(teks)
print("_"*50)
#fungsi capitalize
capitalize = teks.capitalize()
print("Mengganti awalan menjadi huruf menjadi kapital")
print(capitalize)
print("_"*50)
#fungsi center
center = capitalize.center(50," ")
print("Meletakkan teks di center")
print(center)
print("_"*50)
#fungsi count
count = teks.count(" ")
print("Menghitung jumlah spasi pada teks")
print(count)
print("_"*50)
#fungsi len
len = len(teks)
print("Menghitung jumlah karakter pada teks")
print(len)
print("_"*50)
#fungsi replace
replace = center.replace("Soal","Latihan")
print("Merubah isi dari teks")
print(replace)
print("_"*50)
#fungsi upper
upper = replace.upper()
print("Membuat semua huruf pada teks menjadi kapital")
print(upper)
print("_"*50)
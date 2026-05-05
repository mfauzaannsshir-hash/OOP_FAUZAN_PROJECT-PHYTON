# CONTOH STRUKTUR PENCABANGAN IF
# Input data dari pengguna
nilai_ujian = float(input("masukan nilai ujian siswa "))


# struktur kontrol percabangan majemuk
if nilai_ujian >=90:
   predikat= "Sangat baik(A)"
elif nilai_ujian >=75:
   predikat= "Baik(B)"
elif nilai_ujian >= 60:
  predikat= "Cukup(C)"
else:
  predikat="kurang(D)-Memelukan Remedial"

# menampilkan hasil keputusan 
print ("hasil evaluasi:", predikat)
daya = 90

# Yang akan terus berjalan selama daya belum mencapai 100%
while daya < 100:
    print("Mengisi daya... posisi:", daya, "%")
    daya += 2  # Menambah daya setiap putaran

print("Baterai Penuh!")
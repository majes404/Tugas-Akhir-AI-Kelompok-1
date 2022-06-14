def bahaya(tebal,hujan,miring):
    
    if (tebal >= 2.5 and hujan <= 50 and miring >= 60):
        print("aman")
    elif (tebal >= 2.5 and hujan > 50 and miring >= 60):
        print("aman")
    elif (tebal < 2.5 and hujan > 50 and miring >= 60):
        print("rawan longsor")
    elif (tebal >= 2.5 and hujan > 50 and miring < 60):
        print("rawan longsor")        
    elif tebal <= 1 and hujan >= 80 and miring <= 45:
        print("akan terjadi longsor")
    elif tebal <= 1 and hujan < 80 and miring <= 45:
        print("akan terjadi longsor")
    elif tebal <= 0 and hujan >= 0 and miring <= 0:
        print("Masukkan data kembali")

    

print('             daftar terjadinya tanah longsor         ')
print('=====================================================')
print(' ketebalan_tanah    curah_hujan      kemiringan_tanah')
print("=====================================================")

tebalTanah = int(input("Masukkan ketebalan tanah (M):"))
curahHujan = int(input("Masukkan curah hujan /per jam(mm) :"))
kemiringan = int(input("Masukkan tingkat kemiringan :"))
bahaya(tebalTanah,curahHujan,kemiringan)
ulang = input("Diulang y/t :")
while ulang == "y":
    print('             daftar terjadinya tanah longsor         ')
    print('=====================================================')
    print(' ketebalan_tanah    curah_hujan      kemiringan_tanah')
    print("=====================================================")
    tebalTanah = int(input("Masukkan ketebalan tanah (M):"))
    curahHujan = int(input("Masukkan curah hujan /per jam(mm) :"))
    kemiringan = int(input("Masukkan tingkat kemiringan :"))
    bahaya(tebalTanah,curahHujan,kemiringan)
    if ulang == "t":
        break
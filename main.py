#kalkulator sederhana python
print('\n')
print("=========Kalkulator Sederhana Python=========")
print('\n')
print("""Pilih apa yang kamu mau :
1. Penambahan
2. Pengurangan
3. Perkalian
4. Pembagian
""")


#tanya
tanyaUser = input("Pilih nomor : ")
print("\n")
if tanyaUser == "1":
    #nilai pertama
    input_user1 = int(input("Masukkan nilai pertama: "))

    #nilai kedua
    input_user2 = int(input("Masukkan nilai kedua: "))

    #hasil
    total_hasil = input_user1 + input_user2
    print("hasil: ",total_hasil)

elif tanyaUser == "2":
    #nilai pertama
    input_user1 = int(input("Masukkan nilai pertama: "))

    #nilai kedua
    input_user2 = int(input("Masukkan nilai kedua: "))

    #hasil
    total_hasil = input_user1 - input_user2
    print("hasil: ",total_hasil)

elif tanyaUser == "3":
    #nilai pertama
    input_user1 = int(input("Masukkan nilai pertama: "))

    #nilai kedua
    input_user2 = int(input("Masukkan nilai kedua: "))
    
    #hasil
    total_hasil = input_user1 * input_user2
    print("hasil: ",total_hasil)


elif tanyaUser == "4":
    #nilai pertama
    input_user1 = int(input("Masukkan nilai pertama: "))

    #nilai kedua
    input_user2 = int(input("Masukkan nilai kedua: "))

    #hasil
    total_hasil = input_user1 / input_user2
    print("hasil: ",total_hasil)

elif tanyaUser != "1" or tanyaUser != "2" or tanyaUser != "3" or tanyaUser != "4":
    print("Maaf nomor yang kamu masukkan salah!")
    exit
    





                

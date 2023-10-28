mobil =['sedan','mobil','mercedes','4000 cc']
mobil.append('fanta black')
mobil.append('4 buah ban')
mobil.append('2 milyar')
mobil.remove('mobil')

print(mobil)

pilih = input("Masukkan pilihan: ")
match pilih:
    case "1":
        print("sisi*sisi")
    case"2":
        print("22/7*phi*r*r") 
    case"3":
        print("1/2*alas*tinggi") 
    case _:
        print('masukan kembali pilihan')

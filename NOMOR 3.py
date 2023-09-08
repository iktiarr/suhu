print("NAMA: IKTIAR RAMADANI\nNIM: 230441100053")
print(" ")
print("soal nomor 1 < kelvin ke celcius >")
print(" ")
indeks = {
    "kelvin ": "k"
}

for i in indeks :
    print("satuan suhu diketahui:", i, "\nindeks               : ", indeks[i])
    print(" ")
    
suhu = float(input("masukkan suhu kelvin   : ",))
satuan = input("masukkan indeks diatas : ")
print(" ")

if (satuan == "k"):
    print (suhu, "derajat kelvin : ", "derajat")
    print ("rumus kelvin ke celcius\ncelcius = (kelvin-273)")
    print (" ")
    print ("jawaban:")
    print ("celcius = ", (suhu-273), "derajat")
    print (" ")
    print ("jadi hasilnya adalah = ", (suhu-273), "derajat celcius")
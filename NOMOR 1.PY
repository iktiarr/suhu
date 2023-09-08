print("NAMA: IKTIAR RAMADANI\nNIM: 230441100053")
print(" ")
print("soal nomor 1 < celcius ke fahrenheit >")
print(" ")
indeks = {
    "celcius   ": "c"
}

for i in indeks :
    print("satuan suhu diketahui:", i, "\nindeks               : ", indeks[i])
    print(" ")
    
suhu = float(input("masukkan suhu celcius   : ",))
satuan = input("masukkan indeks diatas  : ")
print(" ")

if (satuan == "c"):
    print (suhu, "derajat celcius : ", "derajat")
    print ("rumus celcius ke fahrenheit\nfahrenheit = (celcius * 9/5) + 32")
    print (" ")
    print ("jawaban:")
    print ("fahrenheit = ", (suhu*9/5)+32, "derajat")
    print (" ")
    print ("jadi hasilnya adalah = ", (suhu*9/5)+32, "derajat fahrenheit")
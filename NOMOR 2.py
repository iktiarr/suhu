print("NAMA: IKTIAR RAMADANI\nNIM: 230441100053")
print(" ")
print("soal nomor 1 < fahrenheit ke celcius >")
print(" ")
indeks = {
    "fahrenheit ": "f"
}

for i in indeks :
    print("satuan suhu diketahui:", i, "\nindeks               : ", indeks[i])
    print(" ")
    
suhu = float(input("masukkan suhu fahrenheit: ",))
satuan = input("masukkan indeks diatas  : ")
print(" ")

if (satuan == "f"):
    print (suhu, "derajat fahrenheit : ", "derajat")
    print ("rumus fahrenheit ke celcius\ncelcius = 5/9* (fahrenheit - 32)")
    print (" ")
    print ("jawaban:")
    print ("celcius = ", 5/9* (suhu-32), "derajat")
    print (" ")
    print ("jadi hasilnya adalah = ", 5/9* (suhu-32), "derajat celcius")
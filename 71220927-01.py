#input
jam_awl=int(input("Masukan_awal = "))
menit_awl=int(input("menit_awal = "))
print("")
jam_akhr=int(input("jam_akhir = "))
menit_akhr=int(input("menit_akhir = "))

#Proses
jamawal=jam_awl*60
jamakhr=jam_akhr*60

if menit_awl < menit_akhr:
    hasil=(jamakhr-jamawal)+(menit_akhr-menit_awl)
else:
    hasil=(jamakhr-jamawal)+(60+(menit_akhr-menit_awl))

print("")
#Output
print("selisih antara",str(jam_awl)+":"+str(menit_awl),"dan",str(jam_akhr)+":"+str(menit_akhr),"adalah", hasil,"menit")








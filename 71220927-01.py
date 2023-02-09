#input
jam_awl=int(input("Masukan_awal = "))
menit_awl=int(input("menit_awal = "))
print("")
jam_akhr=int(input("jam_akhir = "))
menit_akhr=int(input("menit_akhir = "))

#Proses
jamawal=jam_awl*60
jamakhr=jam_akhr*60
waktu_awal=jamawal+menit_awl
waktu_akhir=jamakhr+menit_akhr
selisih=waktu_awal-waktu_akhir

print("")
#Output
print("selisihnya adalah",selisih,"menit")




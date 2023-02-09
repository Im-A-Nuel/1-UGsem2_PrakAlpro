#input
a=int(input("n = "))

#proses
uph_bruto = a * 80000
pjk = uph_bruto *5/100
upah_netto = uph_bruto - pjk

#output
print('Upah karyawan sebelum pajak: Rp. ', uph_bruto)
print("Pajak yang harus dibayar: Rp. ", pjk)
print("Penghasilan bersih yang diterima: Rp. ", upah_netto)

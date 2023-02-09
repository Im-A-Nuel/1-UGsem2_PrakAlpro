#input
x=(input("x = "))

#proses
if "/" not in x:
    x=int(x)
else:
    a=x.split("/")
    p=float(a[0])
    q=float(a[1])
    x=p/q


f=(3)*x**3 - (12)*x**2 + 7/15*x - 22/7
#output
print('Hasilnya adalah ', f)

n=int(input('Nhap so giai thua can tinh: '))
def giaithua(n):
    if n==0 or n==1:
        return 1
    else:
        return n*giaithua(n-1)
print("Ket qua so gia thua la : ", giaithua(n))

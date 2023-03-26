def hitung_kata(kalimat,kata):
    kalimat.lower()
    kata.lower()
    kalimat = kalimat.replace('.','')
    kalimat= kalimat.replace(',','')
    kalimat=kalimat.replace('!','')
    kalimat=kalimat.replace('?','')
    kalimat.split()
    hitung = kalimat.count(kata)
    print(f'terdapat {hitung} kata {kata} dalam kalimat')

kalimat = input('Masukan Kalimat : ')
kata = input('Masukan Kata yang ingin di hitung : ')
hitung_kata(kalimat,kata)
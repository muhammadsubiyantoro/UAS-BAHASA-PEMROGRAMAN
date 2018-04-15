def tambah ():
    print ('\t1.Penjumlahan')

    a = int(input('\tMasukan nilai X = '))
    b = int(input('\tMasukan nilai Y = '))
    c = a+b
    print('\tx+y=',c)
    tanya()

def kurang ():
    print ('\t2.Pengurangan')

    a = int(input('\tMasukan nilai X = '))
    b = int(input('\tMasukan nilai Y = '))
    c = a-b
    print('\tx-y=',c)
    tanya()

def bagi ():
    print ('\t3.Pembagian')

    a = int(input('\tMasukan nilai X = '))
    b = int(input('\tMasukan nilai Y = '))
    c = a/b
    print('\tx/y=',c)
    tanya()

def kali ():
    print ('\t4.Perkalian')

    a = int(input('\tMasukan nilai X = '))
    b = int(input('\tMasukan nilai Y = '))
    c = a*b
    print('\tx*y=',c)
    tanya()

def tanya ():
    tanya = input("\n\tKembali Ke menu Kalkulator (y/t) ?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah Input..........!!!")

def menu() :
    print('\n\t===============================')
    print('\tProgram Kalkulator Sederhana')
    print('\t===============================')
    print('\t1. Penjumlahan')
    print('\t2. Pengurangan')
    print('\t3. Pembagian')
    print('\t4. Perkalian')
    print('\t===============================')
    print('\tSilahkan Pilih -4')
    print(' ')
    pil = input('\tMasukkan pilihan : ')
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
        print('\tMaaf, Input yang anda masukkan salah')
        print('\tCoba ulangi kembali')
        tanya()

menu()
    

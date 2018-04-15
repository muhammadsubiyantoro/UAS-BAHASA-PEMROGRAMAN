import getpass

def login():
    print('\n\t================================')
    print('\n\t-----Pilihan-----')
    print('\t1.Penilaian')
    print('\t2.Pembayaran Mahasiswa')
    print('\t3.Kalkulator')

    pilih = input ('\n\tSilahkan pilih : ')
    if pilih == '1':
        from Perhitungan.Penilaian_Mahasiswa import tt
    elif pilih == '2':
        from Perhitungan.Pembayaran_Mahasiswa import Pembayaran
    elif pilih == '3':
        from Perhitungan.Kalkulator import menu
    else:
        exit
    tanya()

def tanya():
    tanya = input('\nKembali ke menu (y/t) : ')
    if tanya == 'y':
        login()
    elif tanya == 't':
        exit
    else:
        print('\n\tSalah Input.....!!!!!')

username = input ('\nUsername : ')
password = getpass.getpass()

print('==============================')
if username == 'Biyant' and password == '12345678910':
    login()

else:
    print('MAAF PASSWORD DAN USERNAME ANDA SALAH.....!!!')
    

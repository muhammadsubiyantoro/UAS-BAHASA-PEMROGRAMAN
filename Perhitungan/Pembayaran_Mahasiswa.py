def Pembayaran () :
    print ("\n=========================================================")
    nama = input ("\nmasukan nama : ")
    nim = input ("\nmasukan NIM : ")
    semester = input ("\nmasukan semester :")
    print ("\n\t-----pilihan pembayaran-----")
    print ("\t1. pembayaran spp")
    print ("\t2. pembayaran uts")
    print ("\t3.pembayaran uas")
    print ("\t4.pembayaran spp & uts")
    print ("\t5.pembayaran spp & uas")
    pilih = input ("\n\tsilahkan pilih : ")
    if pilih == "1" :
        spp()
    elif pilih == "2" :
        uts()
    elif pilih == "3" :
        uas()
    elif pilih == "4" :
        spp_uts()
    elif pilih == "5" :
        spp_uas()
    else:
        exit
        tanya ()
def tanya():
    tanya = input('\n\tKembali ke menu pembayaran (y/t) ?')
    if tanya == 'y':
        Pembayaran()
        
    elif tanya == 't':
        exit
    else:
            print('\n\tSalah Input..........!!!!!')
            
def spp () :
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 5000000 * bulan
    print ("========================================")
    print ("\tottal yang harus dibayar Rp.5000000 * ",bulan," = Rp. ",total)
    tanya()

def uas () :
    matkul_uas = int(input("\n\tjumlah mata kuliah = "))
    matkul_uas = float(matkul_uas)
    total = 500000 * matkul_uas
    print ("========================================")
    print ("\ttotal yang harus di bayar Rp.5000000 * ",matkul_uas," = Rp. ",total)
    tanya()
    
def uts () :
    matkul_uts = int(input("\n\tjumlah mata kuliah ="))
    matkul_uts = float(matkul_uts)
    total = 5000000 * matkul_uts
    print ("========================================")
    print ("\ttotal yang harus di bayar Rp.5000000 * ",matkul_uts," = Rp. ",total)
    tanya()
    
def  spp_uas():
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    matkul  = int(input("\n\jumlah mata kuliah = "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 5000000 * bulan
    bayar_uas = 500000 * matkul
    total = total_spp + bayar_uas + 5000
    print ("\ttotal bayar spp Rp. 5000000 * ",bulan," = Rp. ",total_spp)
    print ("\ttotal bayar uas Rp. 500000 * ",matkul," = Rp. ",bayar_uas)
    print ("\tbiaya tambahan server sebesar Rp. 5000")
    print ("=======================================")
    print ("\ttotal yang harus di bayar", total)
    tanya()
    
def spp_uts() :
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    matkul  = int(input("\n\jumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 5000000 * bulan
    bayar_uts = 500000 * matkul
    total = total_spp + bayar_uts + 5000
    print ("\ttotal bayar spp Rp. 5000000 * ",bulan," = Rp. ",total_spp)
    print ("\ttotal bayar uas Rp. 500000 * ",matkul," = Rp. ",bayar_uts)
    print ("\tbiaya tambahan server sebesar Rp. 5000")
    print ("=======================================")
    print ("\ttotal yang harus di bayar", total)
    tanya()
    
Pembayaran()

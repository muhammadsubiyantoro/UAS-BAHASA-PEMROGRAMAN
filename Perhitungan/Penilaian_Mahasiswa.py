import texttable as tt 
import getpass



def menu():
    print("=======================================")
    print("\n\t-----penilaian mahasiswa-----")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []


    x = [[]]
   
    jawab = "y"

    tab = tt.Texttable()
    while (jawab == 'y'):
        nama.append(input("masukan nama: "))
        nim.append(input("masukan nim: "))
        tugas = int(input("nilai tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("nilai uts: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("nilai uas: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("tambah data [y/t]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['1','1','1','r','r','r','r'])
    tab.header(['no','nama','nim','nilai tugas','nilai uts','nilai uas','nilai akhir'])
    print (tab.draw())

nilai_mahasiswa()

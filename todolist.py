import datetime
import json
import os

if os.path.exists("tasks.json"):
    with open("tasks.json","r") as file:
        tasks=json.load(file)
else:
    tasks=[]

def todolist():
    while True:
        try:
            pilihan=int(input(" 1. melihat daftar\n 2. menambah daftar\n 3. menghapus daftar\n 4. keluar\nMasukkan angka sesuai kebutuhan:"))
        except :
            print("\nmasukkan angka yang sesuai!\n")
            continue
        print("\n")
        if(pilihan==1):
            if (len(tasks)==0):
                print("\nkegiatan kosong\n")
            else:
                print("DAFTAR KEGIATAN")

                sekarang=datetime.datetime.now()

                for i,value in enumerate(tasks):
                    deadline=datetime.datetime.strptime(value["deadline"],"%Y-%m-%d %H:%M")
                    if(sekarang>deadline):
                        status="TERLEWAT!"
                    else:
                        status="BELUM TERLEWAT"
                    
                    print(f"{i+1}.")
                    print("nama kegiatan: ",value["kegiatan"])
                    print("tanggal kegiatan: ",value["tanggalKegiatan"])
                    print("deadline: ",value["deadline"])
                    print(f"status: {status}\n")
        elif(pilihan==2):
            namaKegiatan=input("masukkan nama kegiatan: ")
            tanggal=input("masukkan tanggal dilaksanakan (YYYY-MM-DD HH:MM): ")
            try:
                tanggalKegiatan=datetime.datetime.strptime(tanggal, "%Y-%m-%d %H:%M")
                tanggalTelat=input("masukkan tanggal deadline (YYYY-MM-DD HH:MM): ")
                try:
                    deadline=datetime.datetime.strptime(tanggalTelat, "%Y-%m-%d %H:%M")
                    dataBaru={
                        "kegiatan":namaKegiatan,
                        "tanggalKegiatan":tanggalKegiatan.strftime("%Y-%m-%d %H:%M"),
                        "deadline":deadline.strftime("%Y-%m-%d %H:%M")
                    }
                    tasks.append(dataBaru)
                    print("\n")
                except:
                    print("format waktu salah!\n")
            except:
                print("format waktu salah!\n")
        elif(pilihan==3):
            hapus=True
            while hapus:
                if (len(tasks)==0):
                    print("\nkegiatan kosong\n")
                else:
                    print("daftar kegiatan: ")
                    for i,value in enumerate(tasks):
                        print (f"{i+1}. nama kegiatan: ",value["kegiatan"])
                    print("0. kembali")

                    try:
                        nomor=int(input("\nmasukkan nomor kegiatan: "))
                    except:
                        print("\nmasukkan angka yang sesuai!\n")
                        continue
                    if (nomor>=1 and nomor<=len(tasks)):
                        tasks.pop(nomor-1)
                        print("kegiatan berhasil dihapus!\n")
                        break
                    elif(nomor==0):
                        print("kembali.\n")
                        break
                    else:
                        print("\nmasukkan nomor yang sesuai!\n")
        elif(pilihan==4):
            with open("tasks.json","w") as file:
                json.dump(tasks,file,indent=4)
            print("daftar disimpan. terimakasih")
            break
        else:
            print("\nmasukkan angka yang sesuai!\n")

print("TO DO LIST SEDERHANA")
todolist()
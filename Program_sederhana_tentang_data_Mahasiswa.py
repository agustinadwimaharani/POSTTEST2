print("Buatlah Data Mahasiswa dengan minimal 5 variabel inputan. contoh:\n 1. Nama \n 2. Nim \n 3. dan seterusnya \n Gunakan tipe data STR,INT,dan Float (wajib di pakai semua) \n Simpan data mahasiswa di dalam list")


nama = str (input("nama: "))
nim = int (input("nim: "))
ip = float (input("ip: "))
prodi = str (input("prodi: "))
fakultas = str (input("fakultas: "))

list = [nama,nim,prodi,ip,fakultas]

print(list)

print("\n")

#dictionary

mahasiswa1 = {"nama": "Agustina Dwi Maharani",
              "nim": 2109106037, 
              "ip": 3.75, 
              "prodi": "informatika", 
              "fakultas": "teknik"
              }

mahasiswa2 = {"nama": "nabila endina",
              "nim": 2109106038, 
              "ip": 3.75,
              "prodi": "informatika", 
              "fakultas": "teknik"
              }

mahasiswa3 =  {"nama": "jeffrey pratama", 
               "nim": 2109106214, 
               "ip": 3.7, 
               "prodi": "arsitektur", 
               "fakultas": "teknik"
               }

mahasiswa4 = {"nama": "wonwoo adytama", 
              "nim": 2109106217, 
              "ip": 3.85, 
              "prodi": "teknik sipil", 
              "fakultas": "teknik"
              }

mahasiswa5 = {"nama": "jaemin junandra", 
              "nim": 2109107037, 
              "ip": 3.75, 
              "prodi": "teknik sipil", 
              "fakultas": "teknik"
              }

memberlist = {2109106037:mahasiswa1, 2109106038:mahasiswa2, 2109106038:mahasiswa3, 2109106217:mahasiswa4, 2109107037:mahasiswa5}

print(mahasiswa1)
print(mahasiswa2)
print(mahasiswa3)
print(mahasiswa4)
print(mahasiswa5)


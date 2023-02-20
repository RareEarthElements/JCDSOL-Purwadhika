list_mobil = [
    {
        'merk': 'Pagani',
        'stock': 25,
        'harga': '1000000'
    },
    {
        'merk': 'Peugeot',
        'stock': 35,
        'harga': '1500000'
    },
    {
        'merk': 'Porsche',
        'stock': 45,
        'harga': '2000000'
    }
]


rental = []

def menampilkan_daftar_mobil():
    print('\n\ndaftar mobil\n')
    print('Index\t| Merk   \t| Stock  \t| Harga / hari')
    for i in range (len(list_mobil)):
      print(f"{i}\t| {list_mobil[i]['merk']}  \t| {list_mobil[i]['stock']}  \t\t| {list_mobil[i]['harga']}  ")

def menambahkan_mobil():
    while(True):
      nama_mobil = input('\nMasukan merk mobil: ')
      
      mobil_duplikat = False
      for i in range (len(list_mobil)):
        if(nama_mobil == list_mobil[i]['merk']):
          mobil_duplikat = True

      if(mobil_duplikat == False):
        stock_mobil = int(input('Masukan stock mobil: '))
        harga_mobil = int(input('Masukan harga rental mobil/hari: '))
        list_mobil.append ({
            'merk': nama_mobil, 
            'stock': stock_mobil, 
            'harga': harga_mobil
        })
        print('Mobil berhasil ditambahkan')
        break
      else:
        print('Mobil sudah ada di database')

   
def menghapus_mobil():
    menampilkan_daftar_mobil()
    index_mobil = int(input('Masukan index mobil rental yang ingin dihapus: '))
    if(index_mobil > len(list_mobil) - 1):
      print("mobil tidak ada dalam database")
    else:
      del list_mobil[index_mobil]
      print("mobil berhasil dihapus")

    menampilkan_daftar_mobil()

def update_mobil():
  while(True):

    menampilkan_daftar_mobil()
    
    input_index_mobil = int(input("Masukan index mobil: "))
    
    if(input_index_mobil > len(list_mobil) - 1):
      print("data mobil tidak tersedia")
    else:
      input_stock = int(input("masukan data stock terbaru: "))
      input_harga = int(input("masukan data harga terbaru: "))

      list_mobil[input_index_mobil]['stock'] = input_stock
      list_mobil[input_index_mobil]['harga'] = input_harga

      print("data berhasil diupdate")
      menampilkan_daftar_mobil()
      break

def menampilkan_menu_daftar_mobil_rental():
  while(True):
    pilihan_menu = input ('''
      Pilih menu yang ingin ditampilkan
      
      List Menu:
      1. Report seluruh data
      2. Report data tertentu
      3. Kembali ke menu utama
      
      tekan angka Menu yang ingin dijalankan: ''')
    if(pilihan_menu == '1'):
      menampilkan_daftar_mobil()
    elif(pilihan_menu == '2'):
      input_nama_mobil = input('''
        Masukan nama merek mobil yang diinginkan:  
        ''')

      mobil_ada = False
      for i in range (len(list_mobil)):
        if(input_nama_mobil == list_mobil[i]['merk']):
          print('Index\t| Merk   \t| Stock  \t| Harga / hari')
          print(f"{i}\t| {list_mobil[i]['merk']}  \t| {list_mobil[i]['stock']}  \t\t| {list_mobil[i]['harga']}  ")
          mobil_ada = True
          break
      if(mobil_ada == False):
        print("\nMobil tidak tersedia, silahkan cek di menu 1")
      
    elif(pilihan_menu == '3'):
      break
    else:
      print('\nMenu yang anda pilih tidak tersedia, silahkan masukan input yang benar')

def menampilkan_menu_create_data_mobil_rental():
  while(True):
    pilihan_menu = input ('''
      Pilih menu yang ingin ditampilkan
      
      List Menu:
      1. Tambahkan data
      2. Kembali ke menu utama
      
      tekan angka Menu yang ingin dijalankan: ''')
    if(pilihan_menu == '1'):
      menambahkan_mobil()
    elif(pilihan_menu == '2'):
      break
    else:
      print('\nMenu yang anda pilih tidak tersedia, silahkan masukan input yang benar')

def menampilkan_menu_delete_data_mobil_rental():
  while(True):
    pilihan_menu = input ('''
      Pilih menu yang ingin ditampilkan
      
      List Menu:
      1. Delete data
      2. Kembali ke menu utama
      
      tekan angka Menu yang ingin dijalankan: ''')
    if(pilihan_menu == '1'):
      menghapus_mobil()
    elif(pilihan_menu == '2'):
      break
    else:
      print('\nMenu yang anda pilih tidak tersedia, silahkan masukan input yang benar')

def menampilkan_menu_update_data_mobil_rental():
  while(True):
    pilihan_menu = input ('''
      Pilih menu yang ingin ditampilkan
      
      List Menu:
      1. Update data
      2. Kembali ke menu utama
      
      tekan angka Menu yang ingin dijalankan: ''')
    if(pilihan_menu == '1'):
      update_mobil()
    elif(pilihan_menu == '2'):
      break
    else:
      print('\nMenu yang anda pilih tidak tersedia, silahkan masukan input yang benar')


while(True):

    pilihan_menu = input ('''
        Selamat Datang di Rental Mobil
        
        List Menu:
        1. Menampilkan Daftar Mobil Rental
        2. Menambah Data Mobil Rental
        3. Menghapus Data Mobil Rental
        4. Update data Mobil
        5. Keluar dari Program
        
        tekan angka Menu yang ingin dijalankan: ''')
   
    if(pilihan_menu == '1'):
        menampilkan_menu_daftar_mobil_rental()
    elif(pilihan_menu == '2'):
        menampilkan_menu_create_data_mobil_rental()
    elif(pilihan_menu == '3'):
        menampilkan_menu_delete_data_mobil_rental()
    elif(pilihan_menu == '4'):
        menampilkan_menu_update_data_mobil_rental()
    elif(pilihan_menu == '5'):
        break
    else:
        print('\nMenu yang anda pilih tidak tersedia, silahkan masukan input yang benar')

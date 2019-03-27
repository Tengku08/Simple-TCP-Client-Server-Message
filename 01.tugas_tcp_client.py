# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
ip = '#ip'
# definisikan port dari server yang akan terhubung
port = #dns


# definisikan ukuran buffer untuk mengirimkan pesan
buffer = 1024

# definisikan pesan yang akan disampaikan
pesan = input("==> ")

# buat socket TCP)
s = socket.socket()

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((ip,port))

# kirim pesan ke server
while pesan != 'q':
    s.send(pesan.encode())
    pesan = input("==> ")


# terima pesan dari server
    data = s.recv(buffer).decode()

# tampilkan pesan/reply dari server
    print(data)

# tutup koneksi
s.close()


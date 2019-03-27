# import library socket karena akan menggunakan IPC socket
import socket               


# definisikan alamat IP binding  yang akan digunakan 
ip = "#ip server"
print ("Socket berhasil dibuat")


# definisikan port number binding  yang akan digunakan 
port = #dns


# definisikan ukuran buffer untuk mengirimkan pesan
buffer = 1024


# buat socket bertipe TCP
s = socket.socket()         
print ("socket dalam state mendengarkan")       

# lakukan bind
s.bind((ip, port))
pesan = "socket bind ke alamat " + ip + " dan port " + str(port)
print (pesan)

# server akan listen menunggu hingga ada koneksi dari client
s.listen(5)     


# lakukan loop forever
while True:
	# menerima koneksi
        print (pesan)
        c, addr = s.accept()
        
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
        print ('Mendapat koneksi dari', addr)
    
	
	# menerima data berdasarkan ukuran buffer
        data = c.recv(1024).decode()
	
	# menampilkan pesan yang diterima oleh server menggunakan print
        print("from connected  user: " + str(data))        
	
	# mengirim kembali data yang diterima dari client kepada client
        print("sending: " + str(data))
        c.send(data.encode())    

# tutup koneksi	

c.close()

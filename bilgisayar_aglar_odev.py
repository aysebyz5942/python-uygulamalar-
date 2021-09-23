import socket

HOST = "localhost"
PORT = 8000
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
print "%s:%d server başlatıldı." % (HOST,PORT)
print "Kullanıcı bekleniyor."
s.listen(1) #dinleme
baglanti,adres = soket.accept()
print "Bir bağlantı kabul edildi.",adres
baglanti.send("Hoşgeldiniz efendim , hoşgeldiniz.")
data = baglanti.recv(1024)
print data
soket.close()
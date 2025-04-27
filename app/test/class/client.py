import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("client starting --------->")

host = socket.gethostname()
port = 6000

print(host)

cs.connect((host, port))
msg = input("write message to server: ")

cs.send(bytes(msg.encode("ascii")))

data = cs.recv(1024).decode()
print(f'Message from server: {data}')

msg = input("Write Message to server: ")
while msg.lower() != "bye":
    cs.send(bytes(msg.encode("ascii")))

    data = cs.recv(1024).decode()
    print(f'Message from server: {data}')

    msg = input("message from 1 to 9 to server or type bye to quit")

cs.close()


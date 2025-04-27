import socket

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Starting Server")

host = socket.gethostname()
port = 6000
print(host)

ss.bind((host, port))

conn, addr = ss.recvfrom(1024)

print(f'Client Address: {addr}')
print(f'Client Message: {conn}')

data = conn.decode()

print(f'Message from Server: {data}')

msg = input(f"Message to client ------->")
msg = str.encode(msg)
while msg.lower() != "bye":
    ss.sendto(msg, (addr))

ss.close()
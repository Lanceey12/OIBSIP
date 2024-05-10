import socket

#Internet connection from client
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

#listen to client request/message
server.listen()

#Accept incoming connections
client, addr = server.accept()

done = False

while not done:
    msg = (client.recv(1024).decode('utf-8'))
    if msg == 'quit':
        done = True
    else:
        print(msg)
    client.send(input("Message: ").encode('utf-8'))

client.close()
server.close()

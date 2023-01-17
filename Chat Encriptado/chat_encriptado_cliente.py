import socket
import base64
#HOST = "94.62.26.37"
HOST = "172.20.10.13"
#HOST = "82.154.241.75"
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("-----------Chat-----------")
print(f"Connected to 85.244.99.66")
key = input("Insert the key for the encrypt: ")
while True:
    enc = []
    dec = []

    #receber mensagem
    c = client.recv(1024).decode("utf-8")
    print(c)
    encrypt2 = c
    m = base64.urlsafe_b64decode(encrypt2).decode()
    for i in range(len(m)):
        key_c = key[(i % len(key))//10]
        dec.append(chr((256 + ord(m[i]) - ord(key_c)) % 256))
    print("Decrypted message:\n" + "".join(dec))

    #enviar memsagem
    m = str(input("Message: "))
    for i in range(len(m)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(m[i]) + ord(key_c)) % 256))
    encrypt1 = base64.urlsafe_b64encode("". join(enc).encode()).decode()
    client.send(encrypt1.encode("utf-8"))

from tkinter import *
import socket
import base64








#HOST = "94.62.26.37"
HOST = "10.90.25.171"
#HOST = "82.154.241.75"
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("-----------Chat-----------")
print(f"Connected to 85.244.99.66")

def enviar(mensagem):
    client.send(mensagem.encode("utf-8"))

while True:
    menu_inicial = Tk()
    menu_inicial.title("Primeira app")

    menu_inicial.resizable(True,True)
    menu_inicial['bg'] = "black"
    enc = []
    dec = []
    key = input("Insert the key for the encrypt: ")
    #receber mensagem
    c = client.recv(1024).decode("utf-8")
    print(c)
    p = str(input("Do you want do decrypt the message? [Y/N]: "))
    if p in "Yy":
        key = input("Insert the key for the encrypt: ")
        encrypt2 = c
        m = base64.urlsafe_b64decode(encrypt2).decode()
        for i in range(len(m)):
            key_c = key[i % len(key)]
            dec.append(chr((256 + ord(m[i]) - ord(key_c)) % 256))
        print("Decrypted message:\n" + "".join(dec))
    if p in "Nn":
        pass
    #enviar memsagem
    m = str(input("Message: "))
    for i in range(len(m)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(m[i]) + ord(key_c)) % 256))
    encrypt1 = base64.urlsafe_b64encode("". join(enc).encode()).decode()
    btn = Button(menu_inicial, text="Enviar", command=lambda: enviar(encrypt1))
    btn.pack()
    menu_inicial.mainloop()



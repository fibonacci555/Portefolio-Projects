import PySimpleGUI as sg
import socket
import base64
HOST = "194.210.59.198"
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


sg.theme("Reddit")
layout=[
    [sg.Text("Connected")],
    [sg.Text("Encrypt key"),sg.Input(key='key')],
    [sg.Button("Ok")]
]


#create the window
window=sg.Window("Cliente",layout)


while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == "Ok":
        key = values['key']
        break

window.close()
print(key)

def send_message(msg,key):
    enc=[]
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(key_c)) % 256))
    encrypt1 = base64.urlsafe_b64encode("". join(enc).encode()).decode()
    client.send(encrypt1.encode("utf-8"))

def receive_message(key):
    dec = []
    c = client.recv(1024).decode("utf-8")
    m = base64.urlsafe_b64decode(c).decode()
    for i in range(len(m)):
        key_c = key[ (i % len(key)) // 10 ]
        dec.append(chr((256 + ord(m[ i ]) - ord(key_c)) % 256))
    return dec




sg.theme("Reddit")
layout=[
    [sg.Text("Mensagem"),sg.Input(key='msg')],
    [sg.Output(size=(30,20))],
    [sg.Button("Enviar")]
]


#create the window
window=sg.Window("Cliente",layout)
#create an event loop
while True:
    event , values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event =="Enviar":
        send_message(values["msg"],key)
        print(f'Tu: {values["msg"]}')
    try:
        print(f'Servidor: {receive_message(key)}')
    except:
        pass
    if event == sg.WIN_CLOSED:
        break

window.close()
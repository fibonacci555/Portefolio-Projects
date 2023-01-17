import PySimpleGUI as sg
import socket
import base64

HOST = "192.168.1.181"
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
client, adress = server.accept()


sg.theme("Reddit")
layout = [
[ sg.Text(f"Connected to {adress}")],
    [ sg.Text("Encrypt key") , sg.Input(key='key') ] ,
    [ sg.Button("Ok") ]
]

# create the window
window = sg.Window("Servidor" , layout)

while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == "Ok":
        key = values[ 'key' ]
        break

window.close()

print(key)
def send_message( msg , key ):
    enc = [ ]
    for i in range(len(msg)):
        key_c = key[ i % len(key) ]
        enc.append(chr((ord(msg[ i ]) + ord(key_c)) % 256))
    encrypt1 = base64.urlsafe_b64encode("".join(enc).encode()).decode()
    client.send(encrypt1.encode("utf-8"))


def receive_message( key ):
    dec = [ ]
    c = client.recv(1024).decode("utf-8")
    m = base64.urlsafe_b64decode(c).decode()
    for i in range(len(m)):
        key_c = key[ (i % len(key)) // 10 ]
        dec.append(chr((256 + ord(m[ i ]) - ord(key_c)) % 256))
    return dec


sg.theme("Reddit")
layout = [
    [ sg.Text("Mensagem") , sg.Input(key='msg') ] ,
    [ sg.Output(size=(30 , 20)) ] ,
    [ sg.Button("Enviar") ]
]

# create the window
window = sg.Window("Servidor" , layout)
# create an event loop
while True:
    event , values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event == "Enviar":
        send_message(values[ "msg" ] , key)
        print(f'Tu: {values[ "msg" ]}')
    if event == sg.WIN_CLOSED:
        break
    try:
        print(f'Cliente: {receive_message(key)}')
    except:
        pass
window.close()
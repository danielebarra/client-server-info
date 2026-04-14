import socket

HOST = "127.0.0.1"  # Inserire l'indirizzo IP del server
PORT = 65400        # Inserire il port del server

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print("la creazione del socket è fallita, sto uscendo...", e)
    exit(1)

print('socket creato')

while KeyboardInterrupt:
    try:
        client.connect((HOST,PORT))
        break
    except Exception as e:
        print("connessione fallita: ", e)
        print("ritento la connessione.. Ctrl + C per terminare")
        

print('connessione effettuata')

while True:
    while True:
        x = int(input("Inserisci un numero: "))
        
        msg = x.to_bytes(length=((max(x.bit_length(), 1) + 7) // 8), byteorder="little")
        
        try:
            client.sendall(msg)
        except Exception as e:
            print('operazione di send fallita:', e)
            exit(1)
            
        if x == 0:
            break

    try: 
        blocco = client.recv(1024)
        break
    except Exception as e:
        print('operazione di recv fallita:', e)
        exit(1)

testo = blocco.decode("ascii")
print("risposta ricevuta dal server:", testo)
client.close()
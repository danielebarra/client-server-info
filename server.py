import socket

HOST = ""          # 127.0.0.1 è localhost
PORT = 65400       # Porta su cui il server si pone in listen (da 1024 a 65535)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print("la creazione del socket è fallita, sto uscendo...", e)
    exit(1)

print("socket creato")

try:
    s.bind((HOST, PORT))
except Exception as e:
    print("binding fallito:", e)
    exit(1)

print("binding del socket con", (HOST, PORT), "avvenuto con successo")

try:
    s.listen()
except Exception as e:
    print("operazione di listen fallita:", e)
    exit(1)

while True:
    try:
        print("in attesa del client...")
        conn, addr = s.accept()
        print("connesso con il client", addr)
        
        somma = 0
        
    except Exception as e:
        print("connessione fallita:", e)
        exit(1)

    while True:
        try:
            blocco = conn.recv(1024)
            
            if not blocco:
                conn.close()
                print("il client", addr, "ha chiuso la connessione")
                break
            
            x = int.from_bytes(blocco, byteorder="little")
            
            print("ricevuto dal client il messaggio:", x)
            
            somma += x
            
            if x == 0:
                break
            
        except Exception as e:
            conn.close()
            print("connessione chiusa forzatamante dal client", addr)
            break
        
    if x == 0:
        msg = ("La somma dei numeri inseriti e' " + str(somma))
        print(msg)
        conn.sendall(bytes(msg, "ascii"))
        break
        
    

s.close()

print("chiusura del socket e terminazione del server")
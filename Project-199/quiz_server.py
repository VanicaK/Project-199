import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="127.0.0.1"
port=8000
clientsList=[]
questions=["Absoule zero is _____ degrees C \n A -132 \n B -500 \n C -273 \n D -379", "Which number is not a prime number? \n A 97 \n B "]
answers=["D"]

server.bind((ip,port))
server.listen()

def remove(con):
    if con in clientsList:
        clientsList.remove(con)

print("Server connected")
def broadcastm(msg,con):
    for client in clientsList:
        if client!= con:
            try:
                client.send(msg.encode("utf-8"))
            except:
                remove(client)


def clientThread(con,address):
    con.send("Welcome to the game!".encode("utf-8"))
    while True:
        try:
            messages=con.receive((2048).decode("utf-8"))
            if messages:
                messagetosend="<"+address + ">" +messages
                broadcastm(messagetosend,con)
            else:
                remove(con)
        except:
            continue
        
def getrandomq(conn):
    randn=random.randitn(0,len(questions)-1)
    randans=answers[randn]
    randq=questions[randn]
    conn.send(randq.encode('utf-8'))

while True:
    con,address=server.accept()
    clientsList.append(con)
    newthread=Thread(target=clientThread,args=(con,address))
    newthread.start()



    

    




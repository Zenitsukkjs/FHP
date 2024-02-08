#########################################################################################
import os , socket , threading , json , requests
from time import sleep
#########################################################################################


#########################################################################################
def __ClientSockt__():
    while(True):
            
        try:
            global ClientSockt
            ClientSockt = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            ClientSockt.connect((Host , Port))
            print(f"Conectado > {Host} : {Port}")
            data =  ClientSockt.recv(1024)
            if data :
                print(data)
                break
            else:pass
            
        except:pass
#########################################################################################


#########################################################################################
def __Start__():
    threading.Thread( target= __ClientSockt__ ).start()
if __name__ == "__main__":
    __Start__()
#########################################################################################
IP = "0.tcp.sa.ngrok.io"
PORT = 14161

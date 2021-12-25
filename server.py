

#importing all needed Lib
import socket, time, threading, json

PERIOD = 0.2
PORT = 8888
SERVER = ""
MAX_QUEUE = 30
MAX_MSG_SIZE = 1024

threads = []

#create a socket as Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to range 8888 and accept any request from any client in the LAN
sock.bind((SERVER,PORT))

#Maximun Queue lenght (buffer size)
sock.listen(MAX_QUEUE)

def connectionHandler (connection , addressIP):
    while True:        
        try:
            #Recisved data and saved to RecievedData and the maximun number of bytes is 1024
            recievedData = connection.recv(MAX_MSG_SIZE)
            
            #Any thing can be done as a request handle
            #the requset  is a Question
            #decoding data
            decodedData  = recievedData.decode("UTF-8")
            
            #get the original data from the JSON msg
            pureData = json.loads(decodedData)
            print("--------------------------------")
            print(pureData)
            print("--------------------------------")
            # print( "Base_Rotation_Angle : " +str(pureData["Base_Rotation_Angle"]))
            # print('Base_Leg_Angle : '+str(pureData["Base_Leg_Angle"]))
            # print("Elbow_Angle : "+str(pureData["Elbow_Angle"]))
            # print("Terminal_Mode : "+str(pureData["Terminal_Mode"]))

            
            #Acknolage msg
            connection.sendall(b"Q is sent Succesfully")
            
        except Exception as ex:
            print(ex)
            if (not connection or not recievedData):
                break
    
    #close connection
    connection.close()
    
    #sleep thread
    time.sleep(PERIOD)
    
while True:
    
    #accept the connection
    connection , addressIP = sock.accept()
     
    #Connection , Adderss to threads
    thread=threading.Thread(target=connectionHandler , args=(connection, addressIP))
    
    threads.append(threading.Thread)
    thread.start()
sock.close()
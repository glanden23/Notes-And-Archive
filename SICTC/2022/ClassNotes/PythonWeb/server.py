import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

#object      = class.constructor()
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#                                  ipv4,       streaming
#              help deal when we have 2 address being used
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind((IP,PORT))
serverSocket.listen()

#list of all of the sockets
socketsList = [serverSocket]
#dictionary of the clients
clients={}

print(f'Listening for connections on {IP}:{PORT}...')

#we're going to start telling it what to do
def receiveMessage(clientSocket):
     try:
          messageHeader = clientSocket.recv(HEADER_LENGTH)
          #checking if our client loses connection
          if not len(messageHeader):
               return False
          messageLength = int(messageHeader.decode('utf-8').strip())
          #adding to a dictionary of information
          return {'header':messageHeader,'data':clientSocket.recv(messageLength)}
     except:
          #if we hit the except something went wrong

          #have the client exit
          return False

while True:    #cheat to get something to run until you say break
     readSocket, _, exceptionSocket = select.select(socketsList,[],socketsList)

     #use for loops to iterate through a list
     for notifiedSocket in readSocket:
          #if the notified socket is our server socket, we have a new connection
          if notifiedSocket==serverSocket:
               clientSocket,clientAddress = serverSocket.accept()     #getting the address
               user = receiveMessage(clientSocket)
               if user is False:
                    continue
               #if all good add the socket
               socketsList.append(clientSocket)
               #if all good add the client
               clients[clientSocket]=user
               print('Accepted new connection from {}:{}, username: {}'.format(*clientAddress, user['data'].decode('utf-8')))
          else:
               message = receiveMessage(notifiedSocket)
               if message is False:
                    print('Closed connection from: {}'.format(clients[notifiedSocket]['data'].decode('utf-8')))
                    socketsList.remove(notifiedSocket)
                    del clients[notifiedSocket]

                    continue
               user = clients[notifiedSocket]
               print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

               #for each clientSocket in the client dictionary
               for clientSocket in clients:
                    if clientSocket != notifiedSocket:
                         #we send info back to the user
                         clientSocket.send(user['header'] + user['data'] + message['header'] + message['data'])

     #second list in select.select
     #_

     #Not completely necessary but good practice
     for notifiedSocket in exceptionSocket:
          socketsList.remove(notifiedSocket)
          del clients[notifiedSocket]

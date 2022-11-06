#https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
import socket
import errno
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234
myUsername = input("Username: ")

#creating the socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting to the interwebs
clientSocket.connect((IP,PORT))

#we do not want any messages blocked
clientSocket.setblocking(False)

#putting together our message
username = myUsername.encode('utf-8')
usernameHeader = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
clientSocket.send(usernameHeader + username)

while True:
     message = input(f'{myUsername} > ') #> is alignment
     if message:
          message=message.encode('utf-8')
          messageHeader = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
          clientSocket.send(messageHeader + message)
          try:
               while True:
                    usernameHeader = clientSocket.recv(HEADER_LENGTH)
                    #just like in the server check to see the header length
                    if not len(usernameHeader):
                         print("Connection closed")
                         sys.exit()
                    
                    usernameLength = int(usernameHeader.decode('utf-8').strip())
                    username = clientSocket.recv(usernameLength).decode('utf-8')

                    messageHeader = clientSocket.recv(HEADER_LENGTH)
                    messageLength = int(messageHeader.decode('utf-8').strip())
                    message = clientSocket.recv(messageLength).decode('utf-8')

                    print(f'{username} > {message}')
          except IOError as e:
               # This is normal on non blocking connections - when there are no incoming data, error is going to be raised
               # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
               # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
               # If we got different error code - something happened
               if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()

               # We just did not receive anything
               continue
          except Exception as e:
               # Any other exception - something happened, exit
               print('Reading error: '.format(str(e)))
               sys.exit()


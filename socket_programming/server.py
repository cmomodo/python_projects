
# Importing the socket module.
import socket
from dict import general_response,covid_rules

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5002 # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        
       # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        # check if the user input matches the general response
        for k,v in general_response.items():
                if data == k:
                    data = v  # print(v)
                

        #check if the user is trying to get info about covid travel
        # for a,b in covid_rules.items():
        #     if data == a:
        #         data = b
                
        # data = input(' -> ')
        conn.send(data.encode())  # send data to the client
        
    ''' message = input(str("Me : ")) #asks for a text input.
        if message == "[bye]": #if the message == bye
            conn.send(message.encode()) #sends the messages.
            print("\n") #prints the response
            break #breaks the code
        conn.send(message.encode()) '''

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()


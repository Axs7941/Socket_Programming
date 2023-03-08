import socket
import threading
import os
import argparse


MAX_QUEUE_SIZE = 5

def handle_request(client_socket, client_address, filename, active_threads):
    # print client details 
    print(f"Client details: HOST={client_address[0]}, Socket Family= {client_socket.family}, Socket Type={client_socket.type}, Protocol={client_socket.proto}, Timeout = {client_socket.gettimeout()},filename = {filename}")

    #receive  request from client 
    request= client_socket.recv(1024).decode()
    #if request == 0:
    if not request:
        return
    
    #get filename
    request_lines = request.split('\n')
    request_line = request_lines[0]
    if filename =='':
        print("-#"*50)
        filename = request_line.split()[1].strip('/')
        print(filename)
        print("-#"*50)

    if not filename:
        filename = 'index.html'

    #find file and read file 
    try: 
        with open(filename, 'rb') as f:
            content = f.read()
        status_line = 'HTTP/1.1 200 OK\r\n'
        headers= 'Content-Type: text/html: charset= utf-8\r\n'
        response = status_line + headers + '\r\n' + content.decode()
    except FileNotFoundError:
        status_line = 'HTTP/1.1 404 Not Found\r\n'
        headers = 'Content-Type: text\html; charset=utf\r\n'
        response = status_line + headers + '\r\n' + '<h1> 404 Not Found </h1>'

    #response for client
    client_socket.sendall(response.encode())

    #close the socket
    client_socket.close()

    #print active threads
    active_threads -= 1
    print(f"Number of active connections: {active_threads}") 

def run_server(port,filename):
    #create the socket and bind port with ip 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost',port))
        server_socket.listen(MAX_QUEUE_SIZE)

        print(f'Server is listening on port {port}')

        active_thread = 0 
        #loop for server 
        while True:
            #client connect 
            client_socket, client_address = server_socket.accept()
            print(f"Received connection from {client_address}")
            #start thread 
            t = threading.Thread(target = handle_request, args=(client_socket,client_address,filename,active_thread))
            t.start()

            #increment the thread count 
            active_thread += 1
            print(f"Number of active connections:{active_thread}")


if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('-p','--port', type=int, default=8080, help='the port number to listen on')
    parser.add_argument('-f','--filename', type=str, default='', help='the name of file to serve')
    args=parser.parse_args()

    run_server(args.port, args.filename)


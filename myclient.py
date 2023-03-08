import socket
import sys
import time


#check for arguments 
if len(sys.argv)!= 4:
    print("To run: python3 myclient.py ip_address port_number filename")
    sys.exit(1)

#cmg arg 
ip_address= sys.argv[1]
port_number= int(sys.argv[2]) 
filename = sys.argv[3]

#TCP/IP socket and connect to server 
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address,port_number))

#get server details 
server_hostname = socket.gethostname()
server_family = socket.AF_INET
server_type=socket.IPPROTO_TCP
server_timeout = client_socket.gettimeout()
server_peername= client_socket.getpeername()

#print server details at client terminal 
print(f"SERVER HOSTNAME: {server_hostname}")
print(f"SERVER SCOKET FAMILY: {server_family}")
print(f"SERVER SOCKET TYPE: {server_type}")
print(f"SERVER TIMEOUT: {server_timeout}")
print(f"SERVER peername: {server_peername}")

# Http get message for server 
request= f"GET /{filename} HTTP/1.1\r\nHost: {ip_address}:{port_number}\r\n\r\n"

#to get RTT in microseconds: START TIME
start_time = time.time()

#send request to server
client_socket.sendall(request.encode())

#receive the response from server
response = client_socket.recv(1024).decode()

#Calculate RTT: END TIME - START TIME 
response_time = time.time()-start_time

#print resposne 
print(response)
print(f"RTT: {response_time:.6f} microseconds")

#close the client socket 
#commenting the below code avoids client from being disconnected 
client_socket.close()


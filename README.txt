README file 

This code consists of a simple client-server program that enables the server to send a file to a client that requests it. The server listens for client requests on a specified port and sends the file requested by the client. The client sends a request for the file by specifying the IP address and port number of the server, and the name of the file to be received.


Running the code

The code requires Python version 3.x or higher. The server and client needs to be in the same folder and on the same device. 

To run the server, open a terminal window and navigate to the directory where the myserver.py file is located. Then run the following command.

python3 server.py  -p [port]

where [port] is the port number on which the server listens for requests. Once you have run the command open browser and enter get request in format 127.0.0.1:[port]/filename. Can be tried using multiple browser at the same time on multiple tabs and the server terminal shows the active client details on each request. 

To run the client, open another terminal window and navigate to the directory where the myclient.py file is located. Then run the following command:

Python3 myclient.py [server_IP_address] [server_port] [file_name]

where [server_IP_address] is the IP address of the server, [server_port] is the port number on which the server is listening, and [file_name] is the name of the file to be requested from the server and client shows server details.











Code Documentation

Server Code 


The server code consists of two functions and a main block. The handle_request() function is called when a client sends a request for a file to the server. The function receives the request from the client, parses it, and extracts the name of the file to be served. If the file exists, the function reads its contents and sends a response to the client. If the file does not exist, the function sends an error message to the client. 

The run_server() function creates a TCP socket and binds it to the server's address and port. It listens for incoming client connections and spawns a new thread to handle each request. The function takes two arguments: the port number on which the server listens for requests.

The main block of the server code parses the command line arguments, and calls the run_server() function with the specified port number and file name.

Client Code

The client code consists of a single function that sends a request to the server for a specified file. The function creates a TCP socket, connects to the server, and sends a request message containing the name of the file to be received. The function then receives the response from the server and saves the contents of the file to disk. 

The RTT time is displayed in microseconds 

Limitations and future work 

This code has several limitations. First, it only serves static files, and does not support dynamic content. Second, it does not support secure connections. Third, it has limited error handling capabiliites.

Future work could include adding support for dynamic content, secure connections, and better error handling. 

References

•	Python documentation: https://docs.python.org/3/library/socket.htm
•	Socket programming in Python: https://realpython.com/python-sockets/


Author
This code was written by Abhyudai Singh 

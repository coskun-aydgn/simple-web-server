from socket import *

def main():
    """
    Simple web server that listens for HTTP GET requests 
    and responds with a file's content or a 404 error.
    """

    # Create a TCP socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Define server address and port
    server_ip = '10.0.0.1'  # Localhost
    port = 8000  # Server port

    # Bind the socket to the address and port
    serverSocket.bind((server_ip, port))

    # Start listening for connections
    serverSocket.listen(1)

    print("Web server is running...")

    while True:
        # Accept client connection
        conn, addr = serverSocket.accept()
        print(f"Connection from {addr}")

        # Receive the HTTP request from the client
        request = conn.recv(1024).decode()
        print(f"Received request:\n{request}")

        try:
            # Extract filename from request
            filename = request.split()[1][1:]  # "/index.html" -> "index.html"

            # Open and read the file
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            # Construct HTTP response
            response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + content

        except FileNotFoundError:
            # If file not found, return 404 error
            response = "HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=utf-8\n\n<h1>404 Not Found</h1><p>File not found.</p>"

        # Send response to the client
        conn.send(response.encode())

        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()

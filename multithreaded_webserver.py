from socket import *
import threading  # For handling multiple clients at the same time

def handle_client(client_socket):
    """
    This function handles a single client request.
    It reads the HTTP request, finds the requested file,
    and sends back the response.
    """
    try:
        # Get the request from the client
        request = client_socket.recv(1024).decode()
        print("Client Request:\n", request)

        # Extract the filename from the request (first line)
        filename = request.split()[1][1:]  # "/index.html" -> "index.html"

        try:
            # Open and read the file
            with open(filename, "r", encoding="utf-8") as f:
                file_content = f.read()

            # Create the HTTP response
            response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + file_content

        except FileNotFoundError:
            # If file is not found, send a 404 response
            response = "HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=utf-8\n\n<h1>404 Not Found</h1><p>File not found.</p>"

        # Send the response to the client
        client_socket.send(response.encode())
        print(f"Sending response to client:\n{response}")  # ✅ FIXED indentation

    except Exception as e:
        print("Error handling client:", e)

    finally:
        # Close the connection
        client_socket.close()

def main():
    """
    This function creates a web server that listens for connections.
    Each new client request is handled in a separate thread.
    """
    server_socket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
    server_ip = '127.0.0.1'  # Localhost
    port = 8000  # Port where the server will listen

    # Bind the socket to the IP and port
    server_socket.bind((server_ip, port))

    # Start listening for connections
    server_socket.listen(5)  # Maximum 5 clients can wait in queue

    print("Multithreaded Web Server is running...")

    while True:
        # Accept new client connection
        client_socket, client_address = server_socket.accept()
        print("New connection from:", client_address)

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()  # Run the thread

if __name__ == "__main__":
    main()

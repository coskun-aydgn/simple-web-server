from socket import *
import sys

def main():
    """
    Connects to a web server, sends an HTTP GET request, and prints the response.
    """

    # Define server details
    server_ip = '10.0.0.1'  # Localhost IP
    port = 8000  # Server port

    # Create a TCP socket
    client_sd = socket(AF_INET, SOCK_STREAM)

    try:
        # Connect to the server
        client_sd.connect((server_ip, port))

        # Get the requested file from command line (default: index.html)
        filename = "index.html"
        if len(sys.argv) == 2:
            filename = sys.argv[1].split("/")[-1]  # Extract only the filename

        # Create the HTTP GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}:{port}\r\n\r\n"

        # Send the request
        client_sd.send(request.encode())

        # Receive the response
        received_data = client_sd.recv(4096).decode()

        # Print the server response
        print("===== Server Response =====")
        print(received_data)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the connection
        client_sd.close()

if __name__ == '__main__':
    main()

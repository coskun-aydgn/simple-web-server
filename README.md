README – Simple & Multithreaded Web Server & Client (Mininet)
=============================================================

This project includes a simple HTTP server (single-threaded and multithreaded) 
and a web client implemented in Python using socket programming. It is tested 
and run inside Mininet using virtual hosts (h1, h2).

Files Included
--------------
| File                          | Description                             |
|------------------------------|-----------------------------------------|
| webserver.py                 | Single-threaded server.                 |
| multithreaded_webserver.py   | Multithreaded server using threads.     |
| webclient.py                 | Sends HTTP GET request to the server.   |
| index.html                   | Static HTML file served by the server.  |
| README.md                    | Documentation and instructions.         |

How to Run (Inside Mininet)
---------------------------

Prerequisites:
- Mininet is installed.
- Files are transferred to /home/vboxuser/Documents/datanetverk/.

Step-by-step:
1. Start Mininet:
   sudo mn

2. Open terminals:
   mininet> xterm h1 h2

3. On h1 (Server side):
   cd /home/vboxuser/Documents/datanetverk/
   python3 webserver.py
   # or
   python3 multithreaded_webserver.py

4. On h2 (Client side):
   cd /home/vboxuser/Documents/datanetverk/
   python3 webclient.py 10.0.0.1

To request a missing file:
   python3 webclient.py 10.0.0.1 missing.html

Function Documentation
----------------------

webserver.py / multithreaded_webserver.py

main()
------
Starts the HTTP web server.
- Binds to a given IP address and port (e.g., 10.0.0.1:8000 in Mininet)
- Listens for incoming client connections.
- Handles each client request (multi-threaded in the advanced version).
- Returns: None
- Handles exceptions for file access and socket errors.

handle_client(client_socket)
----------------------------
Handles the HTTP request from a single client.
- Parameters: client_socket
- Returns: Sends HTML content or 404 error message.
- Handles decoding errors and file-not-found.

webclient.py

main()
-----
Sends a GET request to the web server.
- Parameters: IP address of the server as command-line argument
- Returns: None
- Handles connection and decoding errors.

Screenshots
-----------
Make sure to attach:
- Web server terminal (e.g., h1)
- Web client terminal (e.g., h2)
- Ping or telnet confirmation (optional)

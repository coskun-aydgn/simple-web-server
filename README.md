# Simple Web Server and Client

This project contains two versions of a simple HTTP web server and a client written in Python using socket programming.

## Features
- Handles basic HTTP GET requests.
- Serves static HTML files.
- Returns `404 Not Found` for missing files.
- Supports both **Single-Threaded** and **Multithreaded** server versions.

## Server Versions
- **Single-Threaded Server (`webserver.py`)**  
  - Supports only one client at a time.
  - Processes requests sequentially.
- **Multithreaded Server (`multithreaded_webserver.py`)**  
  - Supports multiple clients simultaneously.
  - Uses threading to handle concurrent connections.

## Files
- `webserver.py` - The basic web server that handles one client at a time.
- `multithreaded_webserver.py` - The advanced web server that supports multiple clients.
- `webclient.py` - The client that sends HTTP GET requests.
- `index.html` - Sample HTML file to be served.

## How to Run

### 1️⃣ Start the Web Server
Choose either the **Single-Threaded** or **Multithreaded** server.

#### **Single-Threaded Server**
```sh
python webserver.py
✅ Expected output:

Web server is running...

#### **Multithreaded Server**

python multithreaded_webserver.py

✅ Expected output:

Multithreaded Web Server is running...

2️⃣ Run the Web Client
To request index.html:

python webclient.py index.html
To request a specific file:

python webclient.py test.html
To request a missing file:

python webclient.py missing.html

✅ Expected response:

HTTP/1.1 404 Not Found
Content-Type: text/html; charset=utf-8

<h1>404 Not Found</h1><p>File not found.</p>
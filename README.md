# Simple Web Server and Client

This project contains a simple HTTP web server and a client written in Python using socket programming.

## Features
- Handles basic HTTP GET requests.
- Serves static HTML files.
- Supports multiple file requests.
- Returns `404 Not Found` for missing files.

## Files
- `webserver.py` - The web server that listens for HTTP requests.
- `webclient.py` - The client that sends HTTP GET requests.
- `index.html` - Sample HTML file to be served.

## How to Run

### 1️⃣ Start the Web Server
```sh
python webserver.py

Expected output: "Web server is running..."
###2️⃣ Run the Web Client
- To request index.html:
	python webclient.py
- To request a specific file:
	python webclient.py test.html
- To request a missing file:
	python webclient.py missing.html
- Expected response:
	HTTP/1.1 404 Not Found
	Content-Type: text/html; charset=utf-8

	<h1>404 Not Found</h1><p>File not found.</p>


from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import webbrowser

# Define the hostname and port number for the server
hostName = "localhost"
serverPort = 8080

# Create a class to handle HTTP requests
class MyServer(BaseHTTPRequestHandler):
    # Define the response to a GET request
    def do_GET(self):
        # Send a 200 OK response
        self.send_response(200)
        # Set the content type to HTML
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Write the HTML content to the response
        self.wfile.write(bytes('''
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="UTF-8" />
                        <title>Aashir</title>
                        <link rel="stylesheet" type="text/css" href="F:/projects/style.css" />
                        <script src="F:/projects/script.js" charset="utf-8"></script>
                    </head>
                    <body>
                        <h1>Hello World!</h1>
                        <p>I ❤ CSS</p>
                    </body>
                </html>
        ''', "utf-8"))

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the HTTPServer class
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Open the server URL in the default web browser
        webbrowser.open(f'http://{hostName}:{serverPort}')
        # Keep the server running to handle requests
        webServer.serve_forever()
    except KeyboardInterrupt:
        # If a keyboard interrupt (Ctrl+C) is received, stop the server
        pass

    # Close the server
    webServer.server_close()
    print("Server stopped.")

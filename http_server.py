import socketserver

class MyHTTPRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        print(data)

        f = open("index.html", 'r')

        self.wfile.write("HTTP/1.1 200 OK\r\n".encode('ascii'))
        self.wfile.write("Content-Type: text/html; charset=utf-8\r\n".encode('ascii'))
        self.wfile.write("\r\n".encode('ascii'))
        self.wfile.write(f.read().encode('ascii'))

        f.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 0

    server = socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler)
    ip, port = server.server_address

    ip, port = server.server_address
    print("IP: %s" % ip)
    print("Port: %s" % port)

    server.serve_forever()

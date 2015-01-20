import time
import socket
import threading
import socketserver

class MyHTTPRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        print(data)
        
        cur_thread = threading.currentThread()
        print("Current thread:", cur_thread.getName())

        f = open("index.html", 'r')

        self.wfile.write("HTTP/1.1 200 OK\r\n".encode('ascii'))
        self.wfile.write("Content-Type: text/html; charset=utf-8\r\n".encode('ascii'))
        self.wfile.write("\r\n".encode('ascii'))
        self.wfile.write(f.read().encode('ascii'))

        f.close()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 0

    server = ThreadedHTTPServer((HOST, PORT), MyHTTPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print("Server loop running in thread:", server_thread.getName())
    print("IP: %s" % ip)
    print("Port: %s" % port)

    time.sleep(60)

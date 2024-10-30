import socketserver
from service import process_data

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            self.data = self.request.recv(1024).strip()
            print(f"Received from {self.client_address[0]}: {self.data.decode()}")
            all_values= self.data
            all_values = all_values.decode('utf-8')
            all_values = all_values.split(' ')        
            formated_val = all_values[0].replace('\r\n', ' ')
            print(formated_val,'formated_val-----------------formated_val')
            obj = process_data(formated_val)
            print(obj)
            if obj:
                response = f"+{obj}\r\n"
                self.request.sendall(response.encode('utf-8'))

            response = "+OK\r\n"
            print(response.encode('utf-8'),"here response is getting")
            self.request.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            error_response = f"-ERR {str(e)}\r\n"
            self.request.sendall(error_response.encode('utf-8'))
        
if __name__ == "__main__":  
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Server listening on {HOST}:{PORT}")
        server.serve_forever() #program waits here to listen

import socket

HOST = '0.0.0.0'  # All interfaces
PORT = 8000       # Choose your port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}") 
            data = conn.recv(2**25).decode('utf-8')  # Receive request (optional)
            print("Received:", data) # Log the received data

            conn.sendall(b'HTTP/1.1 200 OK\\r\\nContent-Type: text/plain\\r\\n\\r\\nSuccess!')  # Send response



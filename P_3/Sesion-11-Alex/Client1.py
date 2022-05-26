import socket
class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def __str__(self):
        return f" Connection to SERVER at: {self.server_ip}, PORT: {self.server_port}"

    def ping(self):
        print("OK")

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server_ip, self.server_port))

        s.send(str.encode(msg))

        response = s.recv(2048).decode("utf-8")
        s.close()

        return response

    def debug_talk(self, msg):
        import termcolor
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server_ip, self.server_port))

        print("To Server: ", end="")
        termcolor.cprint(msg, "blue")
        msg_bytes = str.encode(msg)
        s.send(msg_bytes)
        response = s.recv(2048).decode("utf-8")
        print("From Server: ", end="")
        termcolor.cprint(response, "green")

        s.close()
        return response
import socket
website = input("Enter website URL: ")
ip = socket.gethostbyname(website)

print(f"IP Adress : {ip}")
import socket
def get_Host_name_IP(host_name): 
    try: 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname : ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
site = input("Enter Site:")
get_Host_name_IP(site)
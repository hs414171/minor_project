import socket
import requests
import json
def get_Host_name_IP(host_name): 
    try: 
        host_ip = socket.gethostbyname(host_name) 
        return host_ip
        # print("Hostname : ",host_name) 
        # print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
def get_location(ip):
    ip_address = ip
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    return result

site = input("Enter Site:")
ip_addr = get_Host_name_IP(site)

print(ip_addr)
print(get_location(ip_addr))
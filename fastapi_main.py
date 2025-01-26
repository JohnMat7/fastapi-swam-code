from fastapi import FastAPI , Request
import socket
#import docker 
import uvicorn

app = FastAPI()

def get_server_ip():
    hostname = socket.gethostname()    
    client_ip_address = socket.gethostbyname(hostname)
    return client_ip_address


def get_client_ip(request):
    client_ip = request.client.host
    return client_ip

@app.get('/hit-request')
async def read_client_ip(request : Request):
    client_ip_address = get_client_ip(request)
    server_ip_address = get_server_ip()
    return {
        "Client IP address is : ": client_ip_address,
        "Server IP address is : ": server_ip_address
        }




if __name__ == "__main__":
    uvicorn.run( "fastapi_main:app" , host="0.0.0.0" , port=6999 , reload=True)
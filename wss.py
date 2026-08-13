from websockets.sync.server import serve
from websockets.sync.server import server
#setup
print("WS Server by Sol S")

#meta
meta_name="Example WS server"
meta_version="1.0"
meta_owner="Admin"
def echo(ws):
    global meta_owner
    global meta_name
    global meta_version
    while True:
        f=ws.recv()
        print("Got: ", f)
        if f=="meta":
            X="meta Name: "+meta_name+" \n Version: "+meta_version+" \n Owner: "+meta_owner
            ws.send(X)
        else:
            ws.server.broadcast(f)
serve(echo, "0.0.0.0", 6752).serve_forever()

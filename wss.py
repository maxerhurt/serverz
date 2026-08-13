from websocket_server import WebsocketServer

def z(client, server, message):
    server.send_message_to_all(message)

srv=WebsocketServer(host='0.0.0.0', port=6752)
srv.set_fn_message_received(z)
srv.run_forever()

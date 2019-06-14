import pickle
import json
import zmq
import socket as s

MyIp = s.gethostbyname(s.gethostname()) # 192.168.1.102
print(MyIp)
Port = 43000
def run_daemon():
    memory = {}
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://' + MyIp + ':' + str(Port))

    while True:
        try:
            command, key, data = pickle.loads(socket.recv())
            if command == 'set':
                memory[key] = data
                print("key: " + key)
                print("data: " + data)
                socket.send(b'ok')
            elif command == 'get':
                result = memory.get(key, None)
                print(result)
                socket.send(pickle.dumps(result))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    run_daemon()

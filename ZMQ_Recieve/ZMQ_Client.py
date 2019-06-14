import zmq
import pickle

class SuperCacher:
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect('tcp://127.0.0.1:43000')

    def get(self, key):
        self.socket.send(pickle.dumps(('get', key, None)))
        return pickle.loads(self.socket.recv())

    def set(self, key, data):
        self.socket.send(pickle.dumps(('set', key, data)))
        return self.socket.recv() == b'ok'


cache = SuperCacher()
print(cache.set('key', '142'))
print(cache.set('134', '145'))
print(cache.get('key'))

print(cache.get('134'))
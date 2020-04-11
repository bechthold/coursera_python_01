# https://www.coursera.org/learn/diving-in-python/programming/aG3x3/kliient-dlia-otpravki-mietrik
# возможно не реализованы все случаи аозникновения исключения ClientError
import socket
import time


class ClientError(Exception):
    pass


class ClientSocketError(ClientError):
    pass


class ClientProtocolError(ClientError):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientSocketError('error create connection ', err)
    
    def _read(self):
        data = b''
        
        while not data.endswith(b'\n\n'):
            try:
                data += self.connection.recv(1024)
            except socket.error as err:
                raise ClientSocketError('error recv data', err)
            
        decoded_data = data.decode()
        
        status, payload = decoded_data.split('\n', 1)
        payload = payload.strip()
        
        if status == 'error':
            raise ClientProtocolError(payload)
        
        return payload
    
    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        
        try:
            self.connection.sendall(
                f'put {key} {value} {timestamp}\n'.encode()
                )
        except socket.error as err:
            raise ClientSocketError('error send data', err)
        
        self._read()   
        
    def get(self, key):
        # отправка запроса на сервер
        # проверка, что имя метрики состоит из одного слова
        if len(key.split()) != 1:
            raise ClientError
        try:
            self.connection.sendall(
                f'get {key}\n'.encode()
                )
        except socket.error as err:
            raise ClientSocketError('error send data', err)
       
        # получение ответа и преобразование к строковому типу
        payload = self._read()
        
        data = {}
        
        if payload == '':
            return data
            
        # разбиваем полученную строку на список строк по символу \n
        for row in payload.split('\n'):
            metric_key, metric_value, timestamp = row.split()
            if metric_key not in data:
                data[metric_key] = []
            data[metric_key].append((int(timestamp), float(metric_value)))
            
        return data
            
    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientSocketError('error close connection', err)

        
if __name__ == '__main__':
    client = Client("127.0.0.1", 8887, timeout=5)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
     
    print(client.get("*"))
 
    client.close()

import asyncio


class Storage:
    '''Класс для хранения данных'''
    
    def __init__(self):
        # словарь для хранения метрик
        self._data = {}
    
    def put(self, key, value, timestamp):
        '''Сохраняет значения в словарь, возвращает статус выполнения'''
        if key not in self._data:
            self._data[key] = {}
            
        self._data[key][timestamp] = value
        
    def get(self, key):
        '''Получает данные из словаря, возвращает нужные данные, если запрос не *'''
        data = self._data
        
        if key != '*':
            data = {
                key: data.get(key, {})
            }
            
        result = {}
        for key, timestamp_data in data.items():
            result[key] = sorted(timestamp_data.items()) 
        
        return result

    
class ParseError(ValueError):
    pass


class Parser:
    '''Класс для реаоизации протокола'''
    
    def encode(self, responses):
        '''Преобразует ответ сервера в строку для передачи клиенту'''
        rows = []
        
        for response in responses:
            if not response:
                continue
            
            for key, values in response.items():
                for timestamp, value in values:
                    rows.append(f'{key} {value} {timestamp}')
        
        result = 'ok\n'
        
        if rows:
            result += '\n'.join(rows) + '\n'
            
        return result + '\n'
        
    def decode(self, data):
        parts = data.split('\n')

        command = []
        for part in parts:
            if not part:
                continue
            
            try:
                method, params = part.strip().split(' ', 1)
                if method == 'put':
                    key, value, timestamp = params.split()
                    command.append(
                        (method, key, float(value), int(timestamp))
                    )
                elif method == 'get':
                    key = params
                    command.append(
                        (method, key)
                    )
                else:
                    raise ValueError('unknown method')             
                    
            except ValueError:
                raise ParseError('wrong command') 
        
        return command
    
class ExecutorError:
    pass
    
class Executor:
    '''Класс реализует метод, который щнает, как выполнять команды сервера'''
    
    def __init__(self, storage):
        self.storage = storage
        
    def run(self, method, *params):
        if method == 'put':
            return self.storage.put(*params)
        elif method == 'get':
            return self.storage.get(*params)
        else: 
            raise ExecutorError('Unsupported method')
        
class EchoServerClientProtocol(asyncio.Protocol):
    '''Коасс реализации сервера на asyncio'''
    
    storage = Storage()
    
    def __init__(self):
        super().__init__()
        
        self.parser = Parser()
        self.executor = Executor(self.storage)
        self._buffer = b''
        
    def process_data(self, data):
        '''Обработка входной команды сервера'''
        
        commands = self.parser.decode(data)
        
        responses = []
        for command in commands:
            resp = self.executor.run(*command)
            responses.append(resp)
        
        return self.parser.encode(responses)
    
    def connection_made(self, transport):
        self.transport = transport
        
    def data_received(self, data):
        '''Метод вызывается при получении данных в сокете'''
        self._buffer += data
        try:
            decoded_data = self._buffer.decode()
        except UnicodeDecodeError:
            return 
        
        if not decoded_data.endswith('\n'):
            return
        
        self._buffer = b''
        
        try:
            resp = self.process_data(decoded_data)
        except (ExecutorError, ParseError) as err:
            self.transport.write(f'error\n{err}\n\n'.encode())
            return
        self.transport.write(resp.encode())
        
def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        EchoServerClientProtocol, host, port
    )
    
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except (KeyboardInterrupt):
        pass
    
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    
if __name__ == '__main__':
    run_server('127.0.0.1', 8888)
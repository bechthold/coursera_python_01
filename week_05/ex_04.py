#===============================================================================
# class MyRangeIterator:
#     def __init__(self, top):
#         self.top = top
#         self.current = 0
#          
#     def __iter__(self):
#         return self
#      
#     def __next__(self):
#         if self.current >= self.top:
#             raise StopIteration
#          
#         current = self.current
#         self.current += 1
#         return current
#  
# if __name__ == '__main__':    
#     counter = MyRangeIterator(3)
#     for it in counter:
#         print(it)
#===============================================================================

#===============================================================================
# def my_range_generator(top):
#     current = 0
#     while current < top:
#         yield current
#         current += 1
#         
# counter = my_range_generator(3)
# for it in counter:
#     print(it)
#===============================================================================


#===============================================================================
# def grep(pattern):
#     print('stert grep')
#     while True:
#         line = yield
#         if pattern in line:
#             print(line)
#             
# g = grep('python')
# next(g) #g.send(None)
# g.send('golang is better?')
# g.send('python is simple!')
#===============================================================================

#===============================================================================
# # сопрограммы, вызов метода close()
# def grep(pattern):
#     print('start grep')
#     try:
#         while True:
#             line = yield
#             if pattern in line:
#                 print(line)
#     except GeneratorExit:
#         print('stop grep')
#         
# g = grep('python')
# next(g)
# g.send('python is the best!')
# #g.close() #завершает подпрограмму вызовом исключения GeneratorExit
# #можно послать в сопрограмму исключение методом throw
# g.throw(RuntimeError, 'something wrong')
#===============================================================================

#===============================================================================
# def grep(pattern):
#     print("start grep")
#     while True:
#         line = yield
#         if pattern in line:
#             print(line)
# 
# def grep_python_coroutine():
#     g = grep("python")
#     yield from g
# 
# g = grep_python_coroutine()  # is g coroutine?
# g.send(None)
# g.send("python wow!")
#===============================================================================

#===============================================================================
# def chain(x_iterable, y_iterable):
#     yield from x_iterable
#     yield from y_iterable
#     
# def the_same_chain(x_iterable, y_iterable):
#     for x in x_iterable:
#         yield x
#         
#     for y in y_iterable:
#         yield y
# 
# a = [1, 2, 3]
# b = (4, 5)
# for x in chain(a, b):
#     print(x)
#===============================================================================

#===============================================================================
# import asyncio
# 
# @asyncio.coroutine
# def hello_world():
#     while True:
#         print('Hello world!')
#         yield from asyncio.sleep(1.0)
#         
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world())
# loop.close()
#===============================================================================

#===============================================================================
# import asyncio
# 
# async def hello_world():
#     while True:
#         print('Hello world!')
#         await asyncio.sleep(1.0)
#         
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world())
# loop.close()
#===============================================================================

#===============================================================================
# # asyncio, tcp сервер
# 
# import asyncio
# 
# async def handle_echo(reader, writer):
#     data = await reader.read(1024)
#     message = data.decode()
#     addr = writer.get_extra_info("peername")
#     print("received %r from %r" % (message, addr))
#     writer.close()
#     
# loop = asyncio.get_event_loop()
# coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
# server = loop.run_until_complete(coro)
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
# 
# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()
#===============================================================================

#===============================================================================
# # asyncio, tcp клиент
# 
# import asyncio
# 
# async def tcp_echo_client(message, loop):
#     reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)
# 
#     print("send: %r" % message)
#     writer.write(message.encode())
#     writer.close()
# 
# loop = asyncio.get_event_loop()
# message = "hello World!"
# loop.run_until_complete(tcp_echo_client(message, loop))
# loop.close()
#===============================================================================

#===============================================================================
# ### asyncio.Future, аналог concurrent.futures.Future
# 
# import asyncio
# 
# async def slow_operation(future):
#     await asyncio.sleep(1)
#     future.set_result("Future is done!")
# 
# loop = asyncio.get_event_loop()
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# 
# loop.run_until_complete(future)
# print(future.result())
# loop.close()
#===============================================================================

#===============================================================================
# ### asyncio.Task, запуск нескольких корутин
# 
# import asyncio
# 
# async def sleep_task(num):
#     for i in range(5):
#         print(f"process task: {num} iter: {i}")
#         await asyncio.sleep(1)
#     
#     return num
# 
# # ensure_future or create_task
# loop = asyncio.get_event_loop()
# 
# task_list = [loop.create_task(sleep_task(i)) for i in range(2)]
# loop.run_until_complete(asyncio.wait(task_list))
#===============================================================================

# loop.run_in_executor, запуск в отдельном потоке

import asyncio
from urllib.request import urlopen

# a synchronous function
def sync_get_url(url):
    return urlopen(url).read()

async def load_url(url, loop=None):
    future = loop.run_in_executor(None, sync_get_url, url)
    response = await future
    print(len(response))

loop = asyncio.get_event_loop()
loop.run_until_complete(load_url("https://google.com", loop=loop))









#===============================================================================
# #сервер
# import socket
# 
# with socket.socket() as sock:
#     sock.bind(('', 10001))
#     sock.listen()
#     while True:
#         conn, addr = sock.accept()
#         conn.settimeout(5) #timeout := None| 0 | gt 0
#         with conn:
#             while True:
#                 try:
#                     data = conn.recv(1024)
#                 except socket.timeout:
#                     print('Close connection by timeout')
#                     break
#             
#             if not data:
#                 break
#             print(data.decode('utf8'))
#===============================================================================

#===============================================================================
# #клиент
# import socket
# 
# with socket.create_connection(('127.0.0.1', 10001), 5) as sock:
#     sock.settimeout(2)
#     try:
#         sock.sendall('ping'.encode('utf8'))
#     except socket.timeout:
#         print('send data timeout')
#     except socket.error as ex:
#         print('send data error: ', ex)
#===============================================================================

#===============================================================================
# import socket
# print(issubclass(BrokenPipeError, socket.error))
#===============================================================================

#===============================================================================
# import socket
# import threading
# 
# def process_request(conn, addr):
#     print('connected client: ', addr)
#     with conn:
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print(data.decode('utf8'))
# 
# with socket.socket() as sock:
#     sock.bind(('', 10001))
#     sock.listen()
#     while True:
#         conn, addr = sock.accept()
#         th = threading.Thread(target=process_request, args=(conn, addr))
#         th.start()
#===============================================================================

#===============================================================================
# import socket
# 
# with socket.socket() as sock:
#     sock.bind(('', 10001))
#     sock.listen()
#     #создание нескольких процессов
#     while True:
#         #accept распределится "равномерно" между процессами
#         conn, addr = sock.accept()
#         #поток для обработки соединения
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print(data.decode('utf8'))
#===============================================================================

#===============================================================================
# #обработка нескольких соединений, процессы и потоки                
# import socket
# import threading
# import multiprocessing
# import os
# 
# def process_request(conn, addr):
#     print('connected client: ', addr)
#     with conn:
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print(data.decode('utf8'))
#             
# def worker(sock):
#     while True:
#         conn, addr = sock.accept()
#         print('pid', os.getpid())
#         th = threading.Thread(target=process_request, args=(conn, addr))
#         th.start()
#         
# if __name__ == '__main__':
#     with socket.socket() as sock:
#         sock.bind(('', 10001))
#         sock.listen()
#         
#         worker_count = 3
#         workers_list = [multiprocessing.Process(target=worker, args=(sock, ))
#                         for _ in range(worker_count)]
#         
#         for w in workers_list:
#             w.start()
#             
#         for w in workers_list:
#             w.join()
#===============================================================================

#===============================================================================
# #неблокирующий ввод/вывод (epoll работает только в Linux)
# import socket
# import select
# 
# sock = socket.socket()
# sock.bind(('', 10001))
# sock.listen()
# 
# #как обработать запросы для conn1 и conn2
# #одновременно без потоков?
# conn1, addr = sock.accept()
# conn2, addr = sock.accept()
#     
# conn1.setblocking(0)      
# conn2.setblocking(0)
# 
# epoll = select.epoll()
# epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)      
# epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)
# 
# conn_map = {
#     conn1.fileno(): conn1,
#     conn2.fileno(): conn2,
# }
# 
# #цикл обработки событий в epoll
# while True:
#     events = epoll.poll(1)
#     for fileno, event in events:
#         if event & select.EPOLLIN:
#             data = conn_map[fileno].recv(1024)
#             print(data.decode('utf8'))
#         elif event & select.EPOLLOUT:
#             conn_map[fileno].send('ping'.encode('utf8')) 
#===============================================================================
    
 


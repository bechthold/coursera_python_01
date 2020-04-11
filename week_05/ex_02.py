#===============================================================================
# from queue import Queue
# from threading import Thread
# 
# 
# def worker(q, n):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print('process data: ', n, item)
# 
#         
# if __name__ == '__main__':
#     q = Queue(5)
#     th1 = Thread(target=worker, args=(q, 1))
#     th2 = Thread(target=worker, args=(q, 2))
#     th1.start(); th2.start()
#     
#     for i in range(50):
#         q.put(i)
#         
#     q.put(None); q.put(None)
#     th1.join(); th2.join()
#===============================================================================

#===============================================================================
# import threading
# 
# 
# class Point(object):
# 
#     def __init__(self):
#         self.mutex = threading.RLock()
#         self._x = 0
#         self._y = 0
#         
#     def get(self):
#         with self._mutex:
#             return (self._x, self._y)
#         
#     def set(self, x, y):
#         with self._mutex:
#             self._x = x 
#             self._y = y 
#===============================================================================

#===============================================================================
# from threading import Thread
# import time
# 
# def count(n):
#     while n > 0:
#         n -= 1
#         
# t0 = time.time()
# count(100_000_000)
# count(100_000_000)
# 
# print(time.time() - t0)
# 
# t0 = time.time()
# th1 = Thread(target=count, args=(100_000_000, ))
# th2 = Thread(target=count, args=(100_000_000, ))
# th1.start(); th2.start()
# th1.join(); th2.join()
# 
# print(time.time() - t0)
#===============================================================================
            

